# colourswatch

> Auto-generated documentation for [colourswatch.colourswatch](../../colourswatch/colourswatch.py) module.

 hold colourswatch data and provide a series of helper methods such as the
ability to convert to to a pillow palette.

- [Colourswatch](../README.md#colourswatch-index) / [Modules](../README.md#colourswatch-modules) / [colourswatch](index.md#colourswatch) / colourswatch
    - [Colour](#colour)
        - [Colour().\_\_eq\_\_](#colour__eq__)
        - [Colour().\_\_repr\_\_](#colour__repr__)
        - [Colour().colorToTuple](#colourcolortotuple)
        - [Colour().convertedColourToHexTuple](#colourconvertedcolourtohextuple)
        - [Colour().convertedColourToTuple](#colourconvertedcolourtotuple)
        - [Colour().getRGB255](#colourgetrgb255)
        - [Colour().getRGB255Hex](#colourgetrgb255hex)
        - [Colour().toCMYK](#colourtocmyk)
        - [Colour().toHSL](#colourtohsl)
        - [Colour().toHSV](#colourtohsv)
        - [Colour().toLAB](#colourtolab)
        - [Colour().toRGB](#colourtorgb)
    - [ColourSwatch](#colourswatch)
        - [ColourSwatch().\_\_eq\_\_](#colourswatch__eq__)
        - [ColourSwatch().\_\_repr\_\_](#colourswatch__repr__)
        - [ColourSwatch().toPILPalette](#colourswatchtopilpalette)

## Colour

[[find in source code]](../../colourswatch/colourswatch.py#L68)

```python
class Colour():
    def __init__(
        name: str,
        colour: ColorBase | None = None,
        nameNull: bool = False,
        alpha: float = 1.0,
    ):
```

this represents a single colour within the colour swatch

### Colour().\_\_eq\_\_

[[find in source code]](../../colourswatch/colourswatch.py#L102)

```python
def __eq__(other: Colour) -> bool:
```

equals

### Colour().\_\_repr\_\_

[[find in source code]](../../colourswatch/colourswatch.py#L84)

```python
def __repr__():
```

get a string representation of the object

### Colour().colorToTuple

[[find in source code]](../../colourswatch/colourswatch.py#L131)

```python
def colorToTuple() -> tuple[(float, ...)]:
```

get the colour as a tuple. eg. sRGBColor -> (r, g, b)

### Colour().convertedColourToHexTuple

[[find in source code]](../../colourswatch/colourswatch.py#L145)

```python
def convertedColourToHexTuple(uppercase: bool = False) -> tuple[(str, ...)]:
```

get the previously converted colour as a tuple of hexstrings. eg.
sRGBColor -> ("ff", "ff", "ff")

#### Arguments

- `uppercase` *bool, optional* - return hex in uppercase. Defaults to False.

#### Returns

- `tuple` - tuple of hexstrings

### Colour().convertedColourToTuple

[[find in source code]](../../colourswatch/colourswatch.py#L137)

```python
def convertedColourToTuple() -> tuple[(float, ...)]:
```

get the previously converted colour as a tuple. eg.
sRGBColor -> (r, g, b)

### Colour().getRGB255

[[find in source code]](../../colourswatch/colourswatch.py#L160)

```python
def getRGB255() -> tuple[(int, ...)]:
```

get the colour as an rgb 255 tuple

### Colour().getRGB255Hex

[[find in source code]](../../colourswatch/colourswatch.py#L165)

```python
def getRGB255Hex(uppercase: bool = False) -> tuple[(str, ...)]:
```

get the colour as an rgb 255 tuple in hex

### Colour().toCMYK

[[find in source code]](../../colourswatch/colourswatch.py#L111)

```python
def toCMYK() -> CMYKColor:
```

convert to cmyk and dump a copy in self.convertedColour

### Colour().toHSL

[[find in source code]](../../colourswatch/colourswatch.py#L121)

```python
def toHSL() -> HSLColor:
```

convert to hsl and dump a copy in self.convertedColour

### Colour().toHSV

[[find in source code]](../../colourswatch/colourswatch.py#L116)

```python
def toHSV() -> HSVColor:
```

convert to hsv and dump a copy in self.convertedColour

### Colour().toLAB

[[find in source code]](../../colourswatch/colourswatch.py#L126)

```python
def toLAB() -> LabColor:
```

convert to lab and dump a copy in self.convertedColour

### Colour().toRGB

[[find in source code]](../../colourswatch/colourswatch.py#L106)

```python
def toRGB() -> sRGBColor:
```

convert to rgb and dump a copy in self.convertedColour

## ColourSwatch

[[find in source code]](../../colourswatch/colourswatch.py#L20)

```python
class ColourSwatch():
    def __init__(
        name: str,
        colours: list[Colour] | None = None,
        swatchId: str | None = None,
        description: str | None = None,
        swatchCopyright: str | None = None,
        author: str | None = None,
    ):
```

this represents a colour swatch

### ColourSwatch().\_\_eq\_\_

[[find in source code]](../../colourswatch/colourswatch.py#L61)

```python
def __eq__(other: ColourSwatch):
```

probably not ideal for getting equality - avoid using ==

### ColourSwatch().\_\_repr\_\_

[[find in source code]](../../colourswatch/colourswatch.py#L57)

```python
def __repr__() -> str:
```

get a string representation of the object

### ColourSwatch().toPILPalette

[[find in source code]](../../colourswatch/colourswatch.py#L39)

```python
def toPILPalette() -> list[int]:
```

Convert the ColourSwatch object to a pil palette

Usage:

```python
image = PIL.Image.new('P', (1, 1))
image.putpalette(colourSwatch.toPILPalette())
```
