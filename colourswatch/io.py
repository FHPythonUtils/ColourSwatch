""" do file io """

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from os.path import exists
from shlex import split
from defusedxml.ElementTree import parse
from defusedxml.minidom import parseString
from gimpformats.GimpGplPalette import GimpGplPalette
from metprint import LogType, Logger, FHFormatter
from colormath.color_objects import sRGBColor, CMYKColor, LabColor
import yaml

from colourswatch.colourswatch import ColourSwatch, Colour

def prettify(elem, indent="\t", doctype="<?xml version=\"1.0\" encoding=\"utf-8\"?>"):
	"""Return a pretty-printed XML string for the Element.  """
	rough_string = ElementTree.tostring(elem, 'utf-8')
	reparsed = parseString(rough_string)
	reparsed = reparsed.toprettyxml(indent=indent).split("\n")[1:]
	reparsed.insert(0, doctype)
	return "\n".join(reparsed)

def extNotRecognised(fileName):
	""" Output the file extension not recognised error """
	exts = ["gpl", "yaml", "colors", "spl", "skp", "soc", "txt", "acbl", "xml", "pal", "hpl"]
	Logger(FHFormatter()).logPrint("File extension is not recognised for file: " +
	fileName + "! Must be " + "one of \"" + ", \"".join(exts) + "\"", LogType.ERROR)

def openColourSwatch(file):
	"""Open a colour swatch file into a layer image object
	Args:
		file (string): path/ filename
	Returns:
		ColourSwatch: a colour swatch object
	"""
	functionMap = {"gpl": openSwatch_GPL, "yaml": openSwatch_YAML,
	"colors": openSwatch_COLOR, "spl": openSwatch_SPL, "skp": openSwatch_SKP,
	"soc": openSwatch_SOC, "txt": openSwatch_TXT, "acbl": openSwatch_ACBL,
	"xml": openSwatch_XML, "pal": openSwatch_CDPAL, "hpl": openSwatch_HPL}
	if not exists(file):
		Logger(FHFormatter()).logPrint(file + " does not exist", LogType.ERROR)
		raise FileExistsError
	fileExt = file.split(".")[-1].lower()
	if fileExt not in functionMap:
		extNotRecognised(file)
		raise ValueError
	return functionMap[fileExt](file)

def saveColourSwatch(fileName, colourSwatch):
	"""Save a colour swatch to a file
	Args:
		fileName (string): path/ filename
		colourSwatch (ColourSwatch): the colour swatch to save
	"""
	functionMap = {"gpl": saveSwatch_GPL, "yaml": saveSwatch_YAML,
	"colors": saveSwatch_COLOR, "spl": saveSwatch_SPL, "skp": saveSwatch_SKP,
	"soc": saveSwatch_SOC, "txt": saveSwatch_TXT, "acbl": saveSwatch_ACBL,
	"xml": saveSwatch_XML, "pal": saveSwatch_CDPAL, "hpl": saveSwatch_HPL}
	fileExt = fileName.split(".")[-1].lower()
	if fileExt not in functionMap:
		extNotRecognised(fileName)
		raise ValueError
	return functionMap[fileExt](fileName, colourSwatch)


def getColourFromLine(line, lineno, colourSpaceSize=3, colourSpace=sRGBColor, divider=255):
	""" getColourFromLine """
	parts = line.split(None)
	return Colour(" ".join(parts[colourSpaceSize:]) if len(parts) > colourSpaceSize
	else "colour{}".format(lineno),
	colour=colourSpace(*[float(col)/divider for col in parts[:colourSpaceSize]]),
	nameNull=len(parts) <= colourSpaceSize)


def getSwatchFromFileName(file, colours):
	""" getSwatchFromFileName """
	return ColourSwatch(file.replace("\\", "/").split("/")[-1].split(".")[0], colours)

def getWriteOutColour(colour, convertType=int, multiplier=255):
	""" getWriteOutColour """
	return [convertType(col * multiplier) for col in colour]


### GPL ###
def openSwatch_GPL(file):
	""" Open a .GPL into a colour swatch """
	project = GimpGplPalette(file)
	colours = []
	for index, colour in enumerate(project.colors):
		colours.append(Colour(project.colorNames[index] if
		project.colorNames[index] is not None else "colour{}".format(index),
		colour=sRGBColor(colour[0], colour[1], colour[2], True),
		nameNull=project.colorNames[index] is None))
	return ColourSwatch(project.name, colours=colours)

def saveSwatch_GPL(fileName, colourSwatch):
	""" Save a colour swatch as .GPL """
	project = GimpGplPalette()
	project.name = colourSwatch.name
	project.colors = [getWriteOutColour(colour.toRGB().get_value_tuple())
	for colour in colourSwatch.colours]
	project.colorNames = [colour.name if not colour.nameNull else None
	for colour in colourSwatch.colours]
	project.save(fileName)


### YAML ###
def openSwatch_YAML(file):
	""" Open a .YAML into a colour swatch """
	with open(file) as fileData:
		project = yaml.safe_load(fileData.read())
		swatchName = project.pop("scheme") if "scheme" in project else project.pop("name")
		swatchAuthor = project.pop("author")
	return ColourSwatch(swatchName, colours=[Colour(key,
	colour=sRGBColor(int(project[key][0:2], 16), int(project[key][2:4], 16),
	int(project[key][4:6], 16), True))
	for key in project], author=swatchAuthor)

def saveSwatch_YAML(fileName, colourSwatch):
	""" Save a colour swatch as .YAML """
	with open(fileName, "w") as fileData:
		yamldict = {"scheme": colourSwatch.name, "author": colourSwatch.author}
		for colour in colourSwatch.colours:
			yamldict[colour.name] = "".join(["{:02x}".format(colourPart)
			for colourPart in getWriteOutColour(colour.toRGB().get_value_tuple())])
		fileData.write(yaml.safe_dump(yamldict))


### COLOR ###
def openSwatch_COLOR(file):
	""" Open a .COLOR into a colour swatch """
	with open(file) as fileData:
		colours = []
		for lineno, line in enumerate(fileData.readlines()[1:]):
			colours.append(getColourFromLine(line, lineno))
	return getSwatchFromFileName(file, colours)


def saveSwatch_COLOR(fileName, colourSwatch):
	""" Save a colour swatch as .COLOR """
	with open(fileName, "w") as fileData:
		fileData.write("KDE RGB Palette\n" + "\n".join([" ".join(
			["{}".format(col) for col in getWriteOutColour(colour.toRGB().get_value_tuple())]
			) + "\t{}".format(colour.name)	for colour in colourSwatch.colours]) + "\n")


### SPL ###
def openSwatch_SPL(file):
	""" Open a .SPL into a colour swatch """
	with open(file) as fileData:
		colours = []
		for lineno, line in enumerate(fileData.readlines()[1:]):
			colours.append(getColourFromLine(line, lineno, divider=1))
	return getSwatchFromFileName(file, colours)

def saveSwatch_SPL(fileName, colourSwatch):
	""" Save a colour swatch as .SPL """
	with open(fileName, "w") as fileData:
		fileData.write("##Sketch RGBPalette 0\n" + "\n".join([" ".join(
			["{:.6f}".format(col) for col in getWriteOutColour(colour.toRGB().get_value_tuple(), float, 1)]
			) + "\t{}".format(colour.name)	for colour in colourSwatch.colours]) + "\n")


### SKP ###
def openSwatch_SKP(file):
	""" Open a .SKP into a colour swatch """
	with open(file) as fileData:
		xmlrep = parse(fileData).getroot()
		cType = xmlrep[0].attrib["type"]
		colours = []
		for colour in xmlrep[1:]:
			cName = colour.attrib["name"]
			if cType == "CMYK":
				cColour = CMYKColor(float(colour.attrib["c"]), float(colour.attrib["m"]),
				float(colour.attrib["y"]), float(colour.attrib["k"]))
			else:
				cColour = sRGBColor(float(colour.attrib["r"]), float(colour.attrib["g"]),
				float(colour.attrib["b"]))
			colours.append(Colour(cName, cColour))
	return ColourSwatch(xmlrep[0].attrib["name"], colours)


def saveSwatch_SKP(fileName, colourSwatch):
	""" Save a colour swatch as .SKP """
	with open(fileName, "w") as fileData:
		root = Element("palette")
		SubElement(root, "description", {"type": "CMYK", "name": colourSwatch.name})
		for colour in colourSwatch.colours:
			c, m, y, k = getWriteOutColour(colour.toCMYK().get_value_tuple(), float, 1)
			SubElement(root, "color", {"c": str(c), "m": str(m), "y": str(y),
			"k": str(k), "name": colour.name})
		fileData.write(prettify(root))


### SOC ###
def openSwatch_SOC(file):
	""" Open a .SOC into a colour swatch """
	with open(file) as fileData:
		xmlrep = parse(fileData).getroot()
		colours = []
		for colour in xmlrep:
			cName = colour.attrib["{http://openoffice.org/2000/drawing}name"]
			col = colour.attrib["{http://openoffice.org/2000/drawing}color"][1:]
			cColour = sRGBColor(int(col[0:2], 16), int(col[2:4], 16), int(col[4:6], 16), True)
			colours.append(Colour(cName, cColour))
	return getSwatchFromFileName(file, colours)


def saveSwatch_SOC(fileName, colourSwatch):
	""" Save a colour swatch as .SOC """
	with open(fileName, "w") as fileData:
		root = Element("office_color_table")
		for colour in colourSwatch.colours:
			SubElement(root, "draw_color", {"draw_name": colour.name, "draw_color":
			"#" + "".join(["{:02x}".format(col) for col in getWriteOutColour(colour.toRGB().get_value_tuple())])})
		fileData.write(prettify(root, indent=" ",
		doctype="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n").replace("<office_color_table>", "<office:color-table xmlns:office=\"http://openoffice.org/2000/office\" " +
		"xmlns:style=\"http://openoffice.org/2000/style\" " +
		"xmlns:text=\"http://openoffice.org/2000/text\" " +
		"xmlns:table=\"http://openoffice.org/2000/table\" " +
		"xmlns:draw=\"http://openoffice.org/2000/drawing\" " +
		"xmlns:fo=\"http://www.w3.org/1999/XSL/Format\" " +
		"xmlns:xlink=\"http://www.w3.org/1999/xlink\" " +
		"xmlns:dc=\"http://purl.org/dc/elements/1.1/\" " +
		"xmlns:meta=\"http://openoffice.org/2000/meta\" " +
		"xmlns:number=\"http://openoffice.org/2000/datastyle\" " +
		"xmlns:svg=\"http://www.w3.org/2000/svg\" " +
		"xmlns:chart=\"http://openoffice.org/2000/chart\" " +
		"xmlns:dr3d=\"http://openoffice.org/2000/dr3d\" " +
		"xmlns:math=\"http://www.w3.org/1998/Math/MathML\" " +
		"xmlns:form=\"http://openoffice.org/2000/form\" " +
		"xmlns:script=\"http://openoffice.org/2000/script\">").replace("office_color_table",
		"office:color-table").replace("draw_color", "draw:color").replace("draw_name", "draw:name"))


### TXT ###
def openSwatch_TXT(file):
	""" Open a .TXT into a colour swatch """
	with open(file) as fileData:
		colours = []
		for lineno, line in enumerate(fileData.readlines()):
			if line[0] != ";":
				colours.append(Colour("colour{}".format(lineno),
				colour=sRGBColor(int(line[0:2], 16), int(line[2:4], 16),
				int(line[4:6], 16), True), nameNull=True, alpha=int(line[6:8], 16)/255))
	return getSwatchFromFileName(file, colours)

def saveSwatch_TXT(fileName, colourSwatch):
	""" Save a colour swatch as .TXT """
	with open(fileName, "w") as fileData:
		fileData.write("; paint.net Palette File\n; Lines that start with a " +
		"semicolon are comments\n; Colors are written as 8-digit hexadecimal " +
		"numbers: aarrggbb\n; For example, this would specify green: FF00FF00\n; " +
		"The alpha ('aa') value specifies how transparent a color is. FF is " +
		"fully opaque, 00 is fully transparent.\n; A palette must consist of " +
		"ninety six (96) colors. If there are less than this, the remaining " +
		"color\n; slots will be set to white (FFFFFFFF). If there are more, " +
		"then the remaining colors will be ignored.\n" + "\n".join(
			["".join(["{:02X}".format(col) for col in getWriteOutColour(
				colour.toRGB().get_value_tuple())]) +
				"{:02X}".format(int(colour.alpha*255)) for colour in colourSwatch.colours]) + "\n")


### ACBL ###
def openSwatch_ACBL(file):
	""" Open a .ACBL into a colour swatch """
	with open(file) as fileData:
		xmlrep = parse(fileData).getroot()
		cType = xmlrep[1][0].attrib["ColorSpace"]
		colours = []
		for colour in xmlrep[2]:
			cName = colour.attrib["N"]
			cRawColour = [float(col) for col in colour[0].text.split(None)]
			if cType == "CMYK":
				cColour = CMYKColor(*cRawColour)
			elif cType == "RGB":
				cColour = sRGBColor(*cRawColour)
			else:
				cColour = LabColor(*cRawColour)
			colours.append(Colour(cName, cColour))
	return getSwatchFromFileName(file, colours)

def saveSwatch_ACBL(fileName, colourSwatch):
	""" Save a colour swatch as .ACBL """
	raise NotImplementedError


### XML ###
def openSwatch_XML(file):
	""" Open a .XML into a colour swatch """
	with open(file) as fileData:
		xmlrep = parse(fileData).getroot()
		colours = []
		for colour in xmlrep:
			cName = colour.attrib["NAME"]
			col = colour.attrib["RGB"][1:] if "RGB" in colour.attrib else colour.attrib["CMYK"][1:]
			cColour = sRGBColor(int(col[0:2], 16), int(col[2:4], 16), int(col[4:6], 16), True
			) if "RGB" in colour.attrib else CMYKColor(
			int(col[0:2], 16)/255, int(col[2:4], 16)/255,
			int(col[4:6], 16)/255, int(col[6:8], 16)/255)
			colours.append(Colour(cName, cColour))
	return ColourSwatch(xmlrep.attrib["Name"], colours)

def saveSwatch_XML(fileName, colourSwatch):
	""" Save a colour swatch as .XML """
	with open(fileName, "w") as fileData:
		root = Element("SCRIBUSCOLORS", {"Name": colourSwatch.name})
		for colour in colourSwatch.colours:
			SubElement(root, "COLOR", {"Spot": "0", "Register": "0",
			"NAME": colour.name, "RGB": "#" + "".join(["{:02x}".format(col
			) for col in getWriteOutColour(colour.toRGB().get_value_tuple())])})
		fileData.write(prettify(root, indent=" ", doctype="<?xml version=\"1.0\" encoding=\"UTF-8\"?>"))


### PaintShopPro PAL ###
def openSwatch_PSPPAL(file):
	""" Open a PaintShopPro .PAL into a colour swatch """
	with open(file) as fileData:
		colours = []
		for lineno, line in enumerate(fileData.readlines()[3:]):
			colours.append(getColourFromLine(line, lineno))
	return getSwatchFromFileName(file, colours)

def saveSwatch_PSPPAL(fileName, colourSwatch):
	""" Save a colour swatch as PaintShopPro .PAL """
	with open(fileName, "w") as fileData:
		fileData.write("JASC-PAL\n0100\n{}\n".format(len(colourSwatch.colours)) + "\n".join([" ".join(
			["{}".format(col) for col in getWriteOutColour(colour.toRGB().get_value_tuple())]
			) for colour in colourSwatch.colours]) + "\n")


### CorelDraw PAL ###
def openSwatch_CDPAL(file):
	""" Open a CorelDraw .PAL into a colour swatch """
	with open(file) as fileData:
		if fileData.readlines()[0].strip() == "JASC-PAL":
			return openSwatch_PSPPAL(file)
	with open(file) as fileData:
		colours = []
		for line in fileData.readlines():
			parts = split(line)
			colours.append(Colour(parts[0],	colour=CMYKColor(*[float(col)/100 for col in parts[1:5]])))
	return getSwatchFromFileName(file, colours)

def saveSwatch_CDPAL(fileName, colourSwatch):
	""" Save a colour swatch as CorelDraw .PAL """
	for colour in colourSwatch.colours:
		if colour.nameNull:
			return saveSwatch_PSPPAL(fileName, colourSwatch)
	with open(fileName, "w") as fileData:
		fileData.write("\n".join(["\"{}\"  ".format(colour.name) + "  ".join(
			["{:>3}".format(col) for col in
			getWriteOutColour(colour.toCMYK().get_value_tuple(), int, 100)])
			for colour in colourSwatch.colours]) + "\n")
	return True


### HPL ###
def openSwatch_HPL(file):
	""" Open a .HPL into a colour swatch """
	with open(file) as fileData:
		colours = []
		for lineno, line in enumerate(fileData.readlines()[3:]):
			colours.append(getColourFromLine(line, lineno))
	return getSwatchFromFileName(file, colours)

def saveSwatch_HPL(fileName, colourSwatch):
	""" Save a colour swatch as .HPL """
	with open(fileName, "w") as fileData:
		fileData.write("Palette\nVersion 4.0\n\n" + "\n".join([" ".join(
			["{}".format(col) for col in getWriteOutColour(colour.toRGB().get_value_tuple())]
			) for colour in colourSwatch.colours]) + "\n")
