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

[[find in source code]](../../colourswatch/colourswatch.py#L60)

```python
class Colour():
    def __init__(
        name: str,
        colour: Optional[ColorBase] = None,
        nameNull: bool = False,
        alpha: float = 1.0,
    ):
```

this represents a single colour within the colour swatch

### Colour().\_\_eq\_\_

[[find in source code]](../../colourswatch/colourswatch.py#L80)

```python
def __eq__(other: Colour) -> bool:
```

equals

### Colour().\_\_repr\_\_

[[find in source code]](../../colourswatch/colourswatch.py#L70)

```python
def __repr__():
```

get a string representation of the object

### Colour().colorToTuple

[[find in source code]](../../colourswatch/colourswatch.py#L109)

```python
def colorToTuple() -> tuple[(float, ...)]:
```

get the colour as a tuple. eg. sRGBColor -> (r, g, b)

### Colour().convertedColourToHexTuple

[[find in source code]](../../colourswatch/colourswatch.py#L120)

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

[[find in source code]](../../colourswatch/colourswatch.py#L114)

```python
def convertedColourToTuple() -> tuple[(float, ...)]:
```

 get the previously converted colour as a tuple. eg.
sRGBColor -> (r, g, b)

### Colour().getRGB255

[[find in source code]](../../colourswatch/colourswatch.py#L133)

```python
def getRGB255() -> tuple[(int, int, int)]:
```

get the colour as an rgb 255 tuple

### Colour().getRGB255Hex

[[find in source code]](../../colourswatch/colourswatch.py#L139)

```python
def getRGB255Hex(uppercase: bool = False) -> tuple[(str, str, str)]:
```

get the colour as an rgb 255 tuple in hex

### Colour().toCMYK

[[find in source code]](../../colourswatch/colourswatch.py#L89)

```python
def toCMYK() -> CMYKColor:
```

convert to cmyk and dump a copy in self.convertedColour

### Colour().toHSL

[[find in source code]](../../colourswatch/colourswatch.py#L99)

```python
def toHSL() -> HSLColor:
```

convert to hsl and dump a copy in self.convertedColour

### Colour().toHSV

[[find in source code]](../../colourswatch/colourswatch.py#L94)

```python
def toHSV() -> HSVColor:
```

convert to hsv and dump a copy in self.convertedColour

### Colour().toLAB

[[find in source code]](../../colourswatch/colourswatch.py#L104)

```python
def toLAB() -> LabColor:
```

convert to lab and dump a copy in self.convertedColour

### Colour().toRGB

[[find in source code]](../../colourswatch/colourswatch.py#L84)

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
        colours: Optional[list[Colour]] = None,
        swatchId: Optional[str] = None,
        description: Optional[str] = None,
        swatchCopyright: Optional[str] = None,
        author: Optional[str] = None,
    ):
```

this represents a colour swatch

### ColourSwatch().\_\_eq\_\_

[[find in source code]](../../colourswatch/colourswatch.py#L54)

```python
def __eq__(other: ColourSwatch):
```

probably not ideal for getting equality - avoid using ==

### ColourSwatch().\_\_repr\_\_

[[find in source code]](../../colourswatch/colourswatch.py#L50)

```python
def __repr__() -> str:
```

get a string representation of the object

### ColourSwatch().toPILPalette

[[find in source code]](../../colourswatch/colourswatch.py#L32)

```python
def toPILPalette() -> list[int]:
```

Convert the ColourSwatch object to a pil palette

Usage:

```python
image = PIL.Image.new('P', (1, 1))
image.putpalette(colourSwatch.toPILPalette())
```
