""" hold colourswatch data and provide a series of helper methods such as the
ability to convert to to a pillow palette.
"""

#pylint: disable=too-few-public-methods
#pylint: disable=too-many-arguments

from colormath.color_conversions import convert_color
from colormath.color_objects import (
    LabColor,
	CMYKColor,
	HSVColor,
	HSLColor,
    sRGBColor,
)


class ColourSwatch:
	""" this represents a colour swatch """
	def __init__(self, name, colours=None, swatchId=None, description=None,
	swatchCopyright=None, author=None):
		self.id = swatchId
		self.name = name
		self.description = description
		self.copyright = swatchCopyright
		self.colours = colours if colours is not None else []
		self.author = author

	def toPILPalette(self):
		""" Convert the ColourSwatch object to a pil palette

		Usage:
		```python
		image = PIL.Image.new('P', (1, 1))
		image.putpalette(colourSwatch.toPILPalette())
		```
		"""
		pilPalette = []
		for colour in self.colours:
			pilPalette.extend(list(colour.getRGB255()))
		if len(pilPalette) < (256*3):
			pilPalette.extend([0] * (256*3 - len(pilPalette)))
		else:
			pilPalette = pilPalette[:256*3]
		return pilPalette

	def __repr__(self):
		""" get a string representation of the object """
		return "<ColourSwatch \"" + self.name + "\" colours:" + str(len(self.colours)) + ">"

	def __eq__(self, other):
		""" probably not ideal for getting equality - avoid using == """
		if len(self.colours) != len(other.colours):
			return False

class Colour:
	""" this represents a single colour within the colour swatch """
	def __init__(self, name, colour=None, nameNull=False, alpha=1.0):
		self.name = name
		self.nameNull = nameNull
		self.colour = colour
		self.alpha = alpha
		self.convertedColour = []

	def __repr__(self):
		""" get a string representation of the object """
		bConverted = self.convertedColour # do a backup of the convertedColour, we will need to restore
		self.toRGB()
		rString = "<Colour \"" + self.name + \
		"\" RGB:(hex=#" + "".join(self.convertedColourToHexTuple()) + ", dec=" + \
		", ".join(self.convertedColourToTuple()) + ")>"
		self.convertedColour = bConverted # and restore
		return rString

	def __eq__(self, other):
		""" equals """
		return self.toRGB() == other.toRGB()

	def toRGB(self):
		""" convert to rgb and dump a copy in self.convertedColour """
		self.convertedColour = convert_color(self.colour, sRGBColor)
		return self.convertedColour

	def toCMYK(self):
		""" convert to cmyk and dump a copy in self.convertedColour """
		self.convertedColour = convert_color(self.colour, CMYKColor)
		return self.convertedColour

	def toHSV(self):
		""" convert to hsv and dump a copy in self.convertedColour """
		self.convertedColour = convert_color(self.colour, HSVColor)
		return self.convertedColour

	def toHSL(self):
		""" convert to hsl and dump a copy in self.convertedColour """
		self.convertedColour = convert_color(self.colour, HSLColor)
		return self.convertedColour

	def toLAB(self):
		""" convert to lab and dump a copy in self.convertedColour """
		self.convertedColour = convert_color(self.colour, LabColor)
		return self.convertedColour

	def colorToTuple(self):
		""" get the colour as a tuple. eg. sRGBColor -> (r, g, b) """
		return self.colour.get_value_tuple()


	def convertedColourToTuple(self):
		""" get the previously converted colour as a tuple. eg.
		sRGBColor -> (r, g, b)
		"""
		return self.convertedColour.get_value_tuple()

	def convertedColourToHexTuple(self, uppercase=False):
		"""get the previously converted colour as a tuple of hexstrings. eg.
		sRGBColor -> ("ff", "ff", "ff")

		Args:
			uppercase (bool, optional): return hex in uppercase. Defaults to False.

		Returns:
			tuple: tuple of hexstrings
		"""
		return tuple(["{:02X}".format(colourPart) if uppercase else "{:02x}".format(
		colourPart) for colourPart in self.getRGB255()])

	def getRGB255(self):
		""" get the colour as an rgb 255 tuple """
		self.toRGB()
		return tuple([int(colourPart*255) for colourPart in self.convertedColourToTuple()])
