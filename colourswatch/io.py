""" do file io """

# pylint: disable=invalid-name

from __future__ import annotations

import json
from math import ceil
from os.path import exists
from pathlib import Path
from re import findall
from shlex import split
from typing import Any, Iterable
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement

import swatch
import tomlkit
import yaml
from colormath.color_objects import CMYKColor, ColorBase, LabColor, sRGBColor
from defusedxml.ElementTree import parse
from defusedxml.minidom import parseString
from PIL import Image, ImageDraw

from colourswatch.colourswatch import Colour, ColourSwatch
from colourswatch.GimpGplPalette import GimpGplPalette


def prettify(
	elem: Element, indent: str = "\t", doctype: str = '<?xml version="1.0" encoding="utf-8"?>'
):
	"""Return a pretty-printed XML string for the Element."""
	rough_string = ElementTree.tostring(elem, "utf-8")
	reparsed = parseString(rough_string)
	reparsed = reparsed.toprettyxml(indent=indent).split("\n")[1:]
	reparsed.insert(0, doctype)
	return "\n".join(reparsed)


def extNotRecognised(fileName: str):
	"""Output the file extension not recognised error"""
	exts = ', "'.join(
		[
			"gpl",
			"yaml",
			"colors",
			"spl",
			"skp",
			"soc",
			"txt",
			"acbl",
			"xml",
			"pal",
			"hpl",
			"toml",
			"json",
			"ase",
			"png",
			"jpg",
			"webp",
			"svg",
		]
	)
	print(f'ERROR: File extension is not recognised for file: {fileName}! Must be one of "{exts}"')


def openColourSwatch(file: str) -> ColourSwatch:
	"""Open a colour swatch file into a layer image object

	Args:
		file (str): path/ filename

	Raises:
		FileExistsError: [description]
		ValueError: [description]

	Returns:
		ColourSwatch: a colour swatch object
	"""
	functionMap = {
		"gpl": openSwatch_GPL,
		"yaml": openSwatch_YAML,
		"colors": openSwatch_COLOR,
		"spl": openSwatch_SPL,
		"skp": openSwatch_SKP,
		"soc": openSwatch_SOC,
		"txt": openSwatch_TXT,
		"acbl": openSwatch_ACBL,
		"xml": openSwatch_XML,
		"pal": openSwatch_CDPAL,
		"hpl": openSwatch_HPL,
		"toml": openSwatch_TOML,
		"json": openSwatch_JSON,
		"png": openSwatch_PNG,
		"jpg": openSwatch_IMAGE,
		"webp": openSwatch_IMAGE,
		"ase": openSwatch_ASE,
		"svg": openSwatch_SVG,
	}
	if not exists(file):
		print(f"ERROR: {file} does not exist")
		raise FileExistsError
	fileExt = file.split(".")[-1].lower()
	if fileExt not in functionMap:
		extNotRecognised(file)
		raise ValueError
	return functionMap[fileExt](file)


def saveColourSwatch(fileName: str, colourSwatch: ColourSwatch) -> None:
	"""Save a colour swatch to a file

	Args:
		fileName (str): path/ filename
		colourSwatch (ColourSwatch): the colour swatch to save

	Raises:
		ValueError: [description]

	Returns:
		None: [description]
	"""
	functionMap = {
		"gpl": saveSwatch_GPL,
		"yaml": saveSwatch_YAML,
		"colors": saveSwatch_COLOR,
		"spl": saveSwatch_SPL,
		"skp": saveSwatch_SKP,
		"soc": saveSwatch_SOC,
		"txt": saveSwatch_TXT,
		"acbl": saveSwatch_ACBL,
		"xml": saveSwatch_XML,
		"pal": saveSwatch_CDPAL,
		"hpl": saveSwatch_HPL,
		"toml": saveSwatch_TOML,
		"json": saveSwatch_JSON,
		"png": saveSwatch_IMAGE,
		"jpg": saveSwatch_IMAGE,
		"webp": saveSwatch_IMAGE,
		"ase": saveSwatch_ASE,
		"svg": saveSwatch_SVG,
	}
	fileExt = fileName.split(".")[-1].lower()
	if fileExt not in functionMap:
		extNotRecognised(fileName)
		raise ValueError
	return functionMap[fileExt](fileName, colourSwatch)


def getColourFromLine(
	line: str,
	lineno: int,
	colourSpaceSize: int = 3,
	colourSpace: ColorBase = sRGBColor,
	divider: int = 255,
):
	"""getColourFromLine"""
	parts = line.split(None)
	return Colour(
		" ".join(parts[colourSpaceSize:]) if len(parts) > colourSpaceSize else f"colour{lineno}",
		colour=colourSpace(*[float(col) / divider for col in parts[:colourSpaceSize]]),
		nameNull=len(parts) <= colourSpaceSize,
	)


def getSwatchFromFileName(file: str, colours: list[Colour]):
	"""getSwatchFromFileName"""
	return ColourSwatch(file.replace("\\", "/").split("/")[-1].split(".")[0], colours)


def getWriteOutColour(
	colour: Iterable[Any], convertType: type = int, multiplier: int = 255
) -> list[Any]:
	"""getWriteOutColour"""
	return [convertType(col * multiplier) for col in colour]


### GPL ###
def openSwatch_GPL(file: str):
	"""Open a .GPL into a colour swatch"""
	project = GimpGplPalette(file)
	colours = []
	for index, colour in enumerate(project.colors):
		colours.append(
			Colour(
				project.colorNames[index]
				if project.colorNames[index] is not None
				else f"colour{index}",
				colour=sRGBColor(colour[0], colour[1], colour[2], True),
				nameNull=project.colorNames[index] is None,
			)
		)
	return ColourSwatch(project.name, colours=colours)


def saveSwatch_GPL(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .GPL"""
	project = GimpGplPalette()
	project.name = colourSwatch.name
	project.colors = [
		getWriteOutColour(colour.toRGB().get_value_tuple()) for colour in colourSwatch.colours
	]
	project.colorNames = [
		colour.name if not colour.nameNull else None for colour in colourSwatch.colours
	]
	project.save(fileName)


### YAML ###
def openSwatch_YAML(file: str) -> ColourSwatch:
	"""Open a .YAML into a colour swatch"""
	project = yaml.safe_load(Path(file).read_text(encoding="utf-8"))
	swatchName = project.pop("scheme") if "scheme" in project else project.pop("name")
	swatchAuthor = project.pop("author") if "author" in project else None
	return ColourSwatch(
		swatchName,
		colours=[
			Colour(
				key,
				colour=sRGBColor(
					int(project[key][0:2], 16),
					int(project[key][2:4], 16),
					int(project[key][4:6], 16),
					True,
				),
			)
			for key in project
		],
		author=swatchAuthor,
	)


def saveSwatch_YAML(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .YAML"""
	yamldict = {"scheme": colourSwatch.name, "author": colourSwatch.author}
	for colour in colourSwatch.colours:
		yamldict[colour.name] = "".join(colour.getRGB255Hex())
	Path(fileName).write_text(yaml.safe_dump(yamldict), encoding="utf-8")


### JSON ###
def openSwatch_JSON(file: str) -> ColourSwatch:
	"""Open a .JSON into a colour swatch"""
	project = json.loads(Path(file).read_text(encoding="utf-8"))
	swatchName = project.pop("scheme") if "scheme" in project else project.pop("name")
	swatchAuthor = project.pop("author") if "author" in project else None
	return ColourSwatch(
		swatchName,
		colours=[
			Colour(
				key,
				colour=sRGBColor(
					int(project[key][0:2], 16),
					int(project[key][2:4], 16),
					int(project[key][4:6], 16),
					True,
				),
			)
			for key in project
		],
		author=swatchAuthor,
	)


def saveSwatch_JSON(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .JSON"""
	jsondict = {"scheme": colourSwatch.name, "author": colourSwatch.author}
	for colour in colourSwatch.colours:
		jsondict[colour.name] = "".join(colour.getRGB255Hex())
	Path(fileName).write_text(json.dumps(jsondict, indent="\t"), encoding="utf-8")


### TOML ###
def openSwatch_TOML(file: str) -> ColourSwatch:
	"""Open a .TOML into a colour swatch"""
	project = tomlkit.loads(Path(file).read_text(encoding="utf-8"))
	swatchName = project.pop("scheme") if "scheme" in project else project.pop("name")
	swatchAuthor = project.pop("author") if "author" in project else None
	return ColourSwatch(
		swatchName,
		colours=[
			Colour(
				key,
				colour=sRGBColor(
					int(project[key][0:2], 16),
					int(project[key][2:4], 16),
					int(project[key][4:6], 16),
					True,
				),
			)
			for key in project
		],
		author=swatchAuthor,
	)


def saveSwatch_TOML(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .TOML"""
	tomldict = {"scheme": colourSwatch.name, "author": colourSwatch.author}
	for colour in colourSwatch.colours:
		tomldict[colour.name] = "".join(colour.getRGB255Hex())
	Path(fileName).write_text(tomlkit.dumps(tomldict), encoding="utf-8")


### COLOR ###
def openSwatch_COLOR(file: str) -> ColourSwatch:
	"""Open a .COLOR into a colour swatch"""
	colours = []
	for lineno, line in enumerate(Path(file).read_text(encoding="utf-8").splitlines(False)[1:]):
		colours.append(getColourFromLine(line, lineno))
	return getSwatchFromFileName(file, colours)


def saveSwatch_COLOR(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .COLOR"""
	Path(fileName).write_text(
		"KDE RGB Palette\n"
		+ "\n".join(
			[
				" ".join([str(col) for col in colour.getRGB255()]) + f"\t{colour.name}"
				for colour in colourSwatch.colours
			]
		)
		+ "\n",
		encoding="utf-8",
	)


### SPL ###
def openSwatch_SPL(file: str) -> ColourSwatch:
	"""Open a .SPL into a colour swatch"""
	colours = []
	for lineno, line in enumerate(Path(file).read_text(encoding="utf-8").splitlines(False)[1:]):
		colours.append(getColourFromLine(line, lineno, divider=1))
	return getSwatchFromFileName(file, colours)


def saveSwatch_SPL(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .SPL"""
	Path(fileName).write_text(
		"##Sketch RGBPalette 0\n"
		+ "\n".join(
			[
				" ".join(
					[
						f"{col:.6f}"
						for col in getWriteOutColour(colour.toRGB().get_value_tuple(), float, 1)
					]
				)
				+ f"\t{colour.name}"
				for colour in colourSwatch.colours
			]
		)
		+ "\n",
		encoding="utf-8",
	)


### SKP ###
def openSwatch_SKP(file: str) -> ColourSwatch:
	"""Open a .SKP into a colour swatch"""
	xmlrep = parse(file).getroot()
	cType = xmlrep[0].attrib["type"]
	colours = []
	for colour in xmlrep[1:]:
		cName = colour.attrib["name"]
		if cType == "CMYK":
			cColour = CMYKColor(
				float(colour.attrib["c"]),
				float(colour.attrib["m"]),
				float(colour.attrib["y"]),
				float(colour.attrib["k"]),
			)
		else:
			cColour = sRGBColor(
				float(colour.attrib["r"]), float(colour.attrib["g"]), float(colour.attrib["b"])
			)
		colours.append(Colour(cName, cColour))
	return ColourSwatch(xmlrep[0].attrib["name"], colours)


def saveSwatch_SKP(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .SKP"""
	root = Element("palette")
	SubElement(root, "description", {"type": "CMYK", "name": colourSwatch.name})
	for colour in colourSwatch.colours:
		c, m, y, k = getWriteOutColour(colour.toCMYK().get_value_tuple(), float, 1)
		SubElement(
			root,
			"color",
			{"c": str(c), "m": str(m), "y": str(y), "k": str(k), "name": colour.name},
		)
	Path(fileName).write_text(prettify(root), encoding="utf-8")


### SOC ###
def openSwatch_SOC(file: str) -> ColourSwatch:
	"""Open a .SOC into a colour swatch"""
	xmlrep = parse(file).getroot()
	colours = []
	for colour in xmlrep:
		cName = colour.attrib["{http://openoffice.org/2000/drawing}name"]
		col = colour.attrib["{http://openoffice.org/2000/drawing}color"][1:]
		cColour = sRGBColor(int(col[0:2], 16), int(col[2:4], 16), int(col[4:6], 16), True)
		colours.append(Colour(cName, cColour))
	return getSwatchFromFileName(file, colours)


def saveSwatch_SOC(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .SOC"""
	root = Element("office_color_table")
	for colour in colourSwatch.colours:
		SubElement(
			root,
			"draw_color",
			{
				"draw_name": colour.name,
				"draw_color": "#"
				+ "".join(
					[f"{col:02x}" for col in getWriteOutColour(colour.toRGB().get_value_tuple())]
				),
			},
		)
	Path(fileName).write_text(
		prettify(root, indent=" ", doctype='<?xml version="1.0" encoding="UTF-8"?>\n')
		.replace(
			"<office_color_table>",
			'<office:color-table xmlns:office="http://openoffice.org/2000/office" '
			+ 'xmlns:style="http://openoffice.org/2000/style" '
			+ 'xmlns:text="http://openoffice.org/2000/text" '
			+ 'xmlns:table="http://openoffice.org/2000/table" '
			+ 'xmlns:draw="http://openoffice.org/2000/drawing" '
			+ 'xmlns:fo="http://www.w3.org/1999/XSL/Format" '
			+ 'xmlns:xlink="http://www.w3.org/1999/xlink" '
			+ 'xmlns:dc="http://purl.org/dc/elements/1.1/" '
			+ 'xmlns:meta="http://openoffice.org/2000/meta" '
			+ 'xmlns:number="http://openoffice.org/2000/datastyle" '
			+ 'xmlns:svg="http://www.w3.org/2000/svg" '
			+ 'xmlns:chart="http://openoffice.org/2000/chart" '
			+ 'xmlns:dr3d="http://openoffice.org/2000/dr3d" '
			+ 'xmlns:math="http://www.w3.org/1998/Math/MathML" '
			+ 'xmlns:form="http://openoffice.org/2000/form" '
			+ 'xmlns:script="http://openoffice.org/2000/script">',
		)
		.replace("office_color_table", "office:color-table")
		.replace("draw_color", "draw:color")
		.replace("draw_name", "draw:name"),
		encoding="utf-8",
	)


### TXT ###
def openSwatch_TXT(file: str) -> ColourSwatch:
	"""Open a .TXT into a colour swatch"""
	colours = []
	for lineno, line in enumerate(Path(file).read_text(encoding="utf-8").splitlines(False)):
		if line[0] != ";":
			colours.append(
				Colour(
					f"colour{lineno}",
					colour=sRGBColor(
						int(line[0:2], 16), int(line[2:4], 16), int(line[4:6], 16), True
					),
					nameNull=True,
					alpha=int(line[6:8], 16) / 255,
				)
			)
	return getSwatchFromFileName(file, colours)


def saveSwatch_TXT(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .TXT"""
	Path(fileName).write_text(
		"; paint.net Palette File\n; Lines that start with a "
		+ "semicolon are comments\n; Colors are written as 8-digit hexadecimal "
		+ "numbers: aarrggbb\n; For example, this would specify green: FF00FF00\n; "
		+ "The alpha ('aa') value specifies how transparent a color is. FF is "
		+ "fully opaque, 00 is fully transparent.\n; A palette must consist of "
		+ "ninety six (96) colors. If there are less than this, the remaining "
		+ "color\n; slots will be set to white (FFFFFFFF). If there are more, "
		+ "then the remaining colors will be ignored.\n"
		+ "\n".join(
			[
				"".join(colour.getRGB255Hex(True)) + f"{int(colour.alpha * 255):02X}"
				for colour in colourSwatch.colours
			]
		)
		+ "\n",
		encoding="utf-8",
	)


### ACBL ###
def openSwatch_ACBL(file: str) -> ColourSwatch:
	"""Open a .ACBL into a colour swatch"""
	xmlrep = parse(file).getroot()
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


def saveSwatch_ACBL(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .ACBL"""
	raise NotImplementedError


### XML ###
def openSwatch_XML(file: str) -> ColourSwatch:
	"""Open a .XML into a colour swatch"""
	xmlrep = parse(file).getroot()
	colours = []
	for colour in xmlrep:
		cName = colour.attrib["NAME"]
		col = colour.attrib["RGB"][1:] if "RGB" in colour.attrib else colour.attrib["CMYK"][1:]
		cColour = (
			sRGBColor(int(col[0:2], 16), int(col[2:4], 16), int(col[4:6], 16), True)
			if "RGB" in colour.attrib
			else CMYKColor(
				int(col[0:2], 16) / 255,
				int(col[2:4], 16) / 255,
				int(col[4:6], 16) / 255,
				int(col[6:8], 16) / 255,
			)
		)
		colours.append(Colour(cName, cColour))
	return ColourSwatch(xmlrep.attrib["Name"], colours)


def saveSwatch_XML(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .XML"""
	root = Element("SCRIBUSCOLORS", {"Name": colourSwatch.name})
	for colour in colourSwatch.colours:
		SubElement(
			root,
			"COLOR",
			{
				"Spot": "0",
				"Register": "0",
				"NAME": colour.name,
				"RGB": "#"
				+ "".join(
					[f"{col:02x}" for col in getWriteOutColour(colour.toRGB().get_value_tuple())]
				),
			},
		)
	Path(fileName).write_text(
		prettify(root, indent=" ", doctype='<?xml version="1.0" encoding="UTF-8"?>'),
		encoding="utf-8",
	)


### PaintShopPro PAL ###
def openSwatch_PSPPAL(file: str) -> ColourSwatch:
	"""Open a PaintShopPro .PAL into a colour swatch"""
	colours = []
	for lineno, line in enumerate(Path(file).read_text(encoding="utf-8").splitlines(False)[3:]):
		colours.append(getColourFromLine(line, lineno))
	return getSwatchFromFileName(file, colours)


def saveSwatch_PSPPAL(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as PaintShopPro .PAL"""
	Path(fileName).write_text(
		f"JASC-PAL\n0100\n{len(colourSwatch.colours)}\n"
		+ "\n".join(
			[
				" ".join([f"{col}" for col in getWriteOutColour(colour.toRGB().get_value_tuple())])
				for colour in colourSwatch.colours
			]
		)
		+ "\n",
		encoding="utf-8",
	)


### CorelDraw PAL ###
def openSwatch_CDPAL(file: str) -> ColourSwatch:
	"""Open a CorelDraw .PAL into a colour swatch"""
	if Path(file).read_text(encoding="utf-8").splitlines(False)[0].strip() == "JASC-PAL":
		return openSwatch_PSPPAL(file)
	colours = []
	for line in Path(file).read_text(encoding="utf-8").splitlines(False):
		parts = split(line)
		colours.append(
			Colour(parts[0], colour=CMYKColor(*[float(col) / 100 for col in parts[1:5]]))
		)
	return getSwatchFromFileName(file, colours)


def saveSwatch_CDPAL(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as CorelDraw .PAL"""
	for colour in colourSwatch.colours:
		if colour.nameNull:
			return saveSwatch_PSPPAL(fileName, colourSwatch)
	Path(fileName).write_text(
		"\n".join(
			[
				f'"{colour.name}"  '
				+ "  ".join(
					[
						f"{col:>3}"
						for col in getWriteOutColour(colour.toCMYK().get_value_tuple(), int, 100)
					]
				)
				for colour in colourSwatch.colours
			]
		)
		+ "\n",
		encoding="utf-8",
	)
	return True


### HPL ###
def openSwatch_HPL(file: str) -> ColourSwatch:
	"""Open a .HPL into a colour swatch"""
	colours = []
	for lineno, line in enumerate(Path(file).read_text(encoding="utf-8").splitlines(False)[3:]):
		colours.append(getColourFromLine(line, lineno))
	return getSwatchFromFileName(file, colours)


def saveSwatch_HPL(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .HPL"""
	Path(fileName).write_text(
		"Palette\nVersion 4.0\n\n"
		+ "\n".join(
			[
				" ".join([f"{col}" for col in getWriteOutColour(colour.toRGB().get_value_tuple())])
				for colour in colourSwatch.colours
			]
		)
		+ "\n",
		encoding="utf-8",
	)


### ASE ###
def openSwatch_ASE(file: str) -> ColourSwatch:
	"""Open an .ase into a list of colour swatches"""
	project = swatch.parse(file)
	swatches = []
	for swtch in project:
		colours = []
		for colour in swtch["swatches"]:
			if colour["data"]["mode"] == "LAB":
				col = LabColor(*colour["data"]["values"])
			elif colour["data"]["mode"] == "RGB":
				col = sRGBColor(*colour["data"]["values"])
			elif colour["data"]["mode"] == "CMYK":
				col = CMYKColor(*colour["data"]["values"])
			else:
				col = sRGBColor(
					colour["data"]["values"][0],
					colour["data"]["values"][0],
					colour["data"]["values"][0],
				)
			colours.append(Colour(colour["name"], colour=col))
		swatches.append(ColourSwatch(swtch["name"], colours))
	return swatches


def saveSwatch_ASE(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .ase"""
	raise NotImplementedError


### IMAGE ###
def openSwatch_PNG(file: str) -> ColourSwatch:
	"""Open a .png into a colour swatch"""
	colours = []
	project = Image.open(file).convert("RGB")
	seen = set()
	pixels = list(project.getdata())
	rawColours = [x for x in pixels if x not in seen and not seen.add(x)]
	for rCol in rawColours:
		colours.append(
			Colour(
				f"colour{len(colours)}",
				colour=sRGBColor(rCol[0], rCol[1], rCol[2], True),
				nameNull=True,
			)
		)
	return getSwatchFromFileName(file, colours)


def openSwatch_IMAGE(file: str) -> ColourSwatch:
	"""open .jpg, .webp"""
	# Colours should be 16x16 px on a canvas with size 256x(16*ceil(colours/16)
	colours = []
	project = Image.open(file).convert("RGB")
	cols, rows = int(project.size[0] / 16), int(project.size[1] / 16)
	for row in range(rows):
		for col in range(cols):
			rCol = project.getpixel((col * 16 + 8, row * 16 + 8))
			colours.append(
				Colour(
					f"colour{len(colours)}",
					colour=sRGBColor(rCol[0], rCol[1], rCol[2], True),
					nameNull=True,
				)
			)
	return getSwatchFromFileName(file, colours)


def saveSwatch_IMAGE(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .png, .jpg, .webp"""
	# Colours should be 16x16 px on a canvas with size 256x(16*ceil(colours/16)
	colours = colourSwatch.colours
	rows = ceil(len(colours) / 16)
	image = Image.new("RGB", (256, 16 * rows), colours[-1].getRGB255())
	draw = ImageDraw.Draw(image)
	index = 0
	for row in range(rows):
		for col in range(16):
			draw.rectangle(
				[col * 16, row * 16, (col + 1) * 16, (row + 1) * 16],
				fill=colours[index].getRGB255(),
				width=0,
			)
			index += 1 if index < len(colours) - 1 else 0
	image.save(fileName)


### SVG ###
def openSwatch_SVG(file: str) -> ColourSwatch:
	"""Open a .svg into a colour swatch"""
	colours = []
	rCols = set()
	# get a list of colours #rgb, #rrggbb. rgb(r,g,b). rgb(r%,g%,b%)
	rColours = findall(
		r"(#......)|(#...)|rgb\((.*?,.*?,.*?)\)", Path(file).read_text(encoding="utf-8")
	)
	for rColour in rColours:
		if len(rColour[0]) > 0:  # #rrggbb
			col = (
				int(rColour[0][1:3], 16) / 255,
				int(rColour[0][3:5], 16) / 255,
				int(rColour[0][5:7], 16) / 255,
			)
		elif len(rColour[1]) > 0:  # #rgb
			col = (
				int(rColour[1][1], 16) / 16,
				int(rColour[1][2], 16) / 16,
				int(rColour[1][3], 16) / 15,
			)
		else:
			r, g, b = rColour[2].split(",")
			r, g, b = r.strip(), g.strip(), b.strip()
			if r[-1] == "%":  # rgb(r%,g%,b%)
				col = (int(r[:-1]) / 100, int(g[:-1]) / 100, int(b[:-1]) / 100)
			else:  # rgb(r,g,b)
				col = (int(r) / 255, int(g) / 255, int(b) / 255)
		if col not in rCols:
			rCols.add(col)
			colours.append(Colour(f"colour{len(colours)}", sRGBColor(col[0], col[1], col[2]), True))
	return getSwatchFromFileName(file, colours)


def saveSwatch_SVG(fileName: str, colourSwatch: ColourSwatch):
	"""Save a colour swatch as .svg"""
	colours = colourSwatch.colours
	rows = ceil(len(colours) / 16)
	colours[-1].toRGB()
	data = [
		(
			'<svg xmlns="http://www.w3.org/2000/svg" height="{0}" '
			+ 'width="256" version="1.1">\n\t<rect style="fill:#{1}" '
			+ 'height="{0}" width="256" x="0" y="0"/>'
		).format(rows * 16, "".join(colours[-1].getRGB255Hex()))
	]
	index = 0
	for row in range(rows):
		for col in range(16):
			colours[index].toRGB()
			data.append(
				'\t<rect style="fill:#{}" height="16" width="16" x="{}" y="{}"/>'.format(
					"".join(colours[index].getRGB255Hex()), col * 16, row * 16
				)
			)
			if index < len(colours) - 2:
				index += 1
			else:
				break
	data.append("</svg>\n")
	Path(fileName).write_text("\n".join(data), encoding="utf-8")
