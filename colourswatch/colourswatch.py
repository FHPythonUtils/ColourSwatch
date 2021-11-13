""" hold colourswatch data and provide a series of helper methods such as the
ability to convert to to a pillow palette.
"""

# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
from __future__ import annotations

from colormath.color_conversions import convert_color
from colormath.color_objects import (
	CMYKColor,
	ColorBase,
	HSLColor,
	HSVColor,
	LabColor,
	sRGBColor,
)


class ColourSwatch:
	"""this represents a colour swatch"""

	def __init__(
		self,
		name: str,
		colours: list[Colour] | None = None,
		swatchId: str | None = None,
		description: str | None = None,
		swatchCopyright: str | None = None,
		author: str | None = None,
	):
		self.swatchId = swatchId
		self.name = name
		self.description = description
		self.copyright = swatchCopyright
		self.colours = colours if colours is not None else []
		self.author = author

	def toPILPalette(self) -> list[int]:
		"""Convert the ColourSwatch object to a pil palette

		Usage:
		```python
		image = PIL.Image.new('P', (1, 1))
		image.putpalette(colourSwatch.toPILPalette())
		```
		"""
		pilPalette = []
		for colour in self.colours:
			pilPalette.extend(list(colour.getRGB255()))
		if len(pilPalette) < (256 * 3):
			pilPalette.extend([0] * (256 * 3 - len(pilPalette)))
		else:
			pilPalette = pilPalette[: 256 * 3]
		return pilPalette

	def __repr__(self) -> str:
		"""get a string representation of the object"""
		return '<ColourSwatch "' + self.name + '" colours:' + str(len(self.colours)) + ">"

	def __eq__(self, other: ColourSwatch):
		"""probably not ideal for getting equality - avoid using =="""
		if len(self.colours) != len(other.colours):
			return False
		return True


class Colour:
	"""this represents a single colour within the colour swatch"""

	def __init__(
		self,
		name: str,
		colour: ColorBase | None = None,
		nameNull: bool = False,
		alpha: float = 1.0,
	):
		self.name = name
		self.nameNull = nameNull
		self.colour = colour
		self.alpha = alpha
		self.convertedColour: ColorBase | None = None

	def __repr__(self):
		"""get a string representation of the object"""
		bConverted = (
			self.convertedColour
		)  # do a backup of the convertedColour, we will need to restore
		self.toRGB()
		rString = (
			'<Colour "'
			+ self.name
			+ '" RGB:(hex=#'
			+ "".join(self.convertedColourToHexTuple())
			+ ", dec="
			+ ", ".join([str(col) for col in self.convertedColourToTuple()])
			+ ")>"
		)
		self.convertedColour = bConverted  # and restore
		return rString

	def __eq__(self, other: Colour) -> bool:
		"""equals"""
		return self.toRGB() == other.toRGB()

	def toRGB(self) -> sRGBColor:
		"""convert to rgb and dump a copy in self.convertedColour"""
		self.convertedColour = convert_color(self.colour, sRGBColor)
		return self.convertedColour

	def toCMYK(self) -> CMYKColor:
		"""convert to cmyk and dump a copy in self.convertedColour"""
		self.convertedColour = convert_color(self.colour, CMYKColor)
		return self.convertedColour

	def toHSV(self) -> HSVColor:
		"""convert to hsv and dump a copy in self.convertedColour"""
		self.convertedColour = convert_color(self.colour, HSVColor)
		return self.convertedColour

	def toHSL(self) -> HSLColor:
		"""convert to hsl and dump a copy in self.convertedColour"""
		self.convertedColour = convert_color(self.colour, HSLColor)
		return self.convertedColour

	def toLAB(self) -> LabColor:
		"""convert to lab and dump a copy in self.convertedColour"""
		self.convertedColour = convert_color(self.colour, LabColor)
		return self.convertedColour

	def colorToTuple(self) -> tuple[float, ...]:
		"""get the colour as a tuple. eg. sRGBColor -> (r, g, b)"""
		if not self.colour:
			raise ValueError
		return self.colour.get_value_tuple()

	def convertedColourToTuple(self) -> tuple[float, ...]:
		"""get the previously converted colour as a tuple. eg.
		sRGBColor -> (r, g, b)
		"""
		if not self.convertedColour:
			raise ValueError
		return self.convertedColour.get_value_tuple()

	def convertedColourToHexTuple(self, uppercase: bool = False) -> tuple[str, ...]:
		"""get the previously converted colour as a tuple of hexstrings. eg.
		sRGBColor -> ("ff", "ff", "ff")

		Args:
			uppercase (bool, optional): return hex in uppercase. Defaults to False.

		Returns:
			tuple: tuple of hexstrings
		"""
		return tuple(
			f"{colourPart:02X}" if uppercase else f"{colourPart:02x}"
			for colourPart in self.getRGB255()
		)

	def getRGB255(self) -> tuple[int, ...]:
		"""get the colour as an rgb 255 tuple"""
		self.toRGB()
		return tuple(int(colourPart * 255) for colourPart in self.convertedColourToTuple())

	def getRGB255Hex(self, uppercase: bool = False) -> tuple[str, ...]:
		"""get the colour as an rgb 255 tuple in hex"""
		self.toRGB()
		return self.convertedColourToHexTuple(uppercase)
