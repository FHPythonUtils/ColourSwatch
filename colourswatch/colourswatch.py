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
		""" Convert the ColourSwatch object to a pil palette """
		pilPalette = []
		for colour in self.colours:
			pilPalette.extend(list(colour.toRGB().get_value_tuple()))


class Colour:
	""" this represents a single colour within the colour swatch """
	def __init__(self, name, colour=None, nameNull=False, alpha=1.0):
		self.name = name
		self.nameNull = nameNull
		self.colour = colour
		self.alpha = alpha
		self.convertedColour = []

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
