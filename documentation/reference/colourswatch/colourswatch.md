# ColourSwatch

[Colourswatch Index](../README.md#colourswatch-index) /
[Colourswatch](./index.md#colourswatch) /
ColourSwatch

> Auto-generated documentation for [colourswatch.colourswatch](../../../colourswatch/colourswatch.py) module.

- [ColourSwatch](#colourswatch)
  - [Colour](#colour)
    - [Colour().__eq__](#colour()__eq__)
    - [Colour().__repr__](#colour()__repr__)
    - [Colour().colorToTuple](#colour()colortotuple)
    - [Colour().convertedColourToHexTuple](#colour()convertedcolourtohextuple)
    - [Colour().convertedColourToTuple](#colour()convertedcolourtotuple)
    - [Colour().getRGB255](#colour()getrgb255)
    - [Colour().getRGB255Hex](#colour()getrgb255hex)
    - [Colour().toCMYK](#colour()tocmyk)
    - [Colour().toHSL](#colour()tohsl)
    - [Colour().toHSV](#colour()tohsv)
    - [Colour().toLAB](#colour()tolab)
    - [Colour().toRGB](#colour()torgb)
  - [ColourSwatch](#colourswatch-1)
    - [ColourSwatch().__eq__](#colourswatch()__eq__)
    - [ColourSwatch().__repr__](#colourswatch()__repr__)
    - [ColourSwatch().toPILPalette](#colourswatch()topilpalette)

## Colour

[Show source in colourswatch.py:68](../../../colourswatch/colourswatch.py#L68)

this represents a single colour within the colour swatch

#### Signature

```python
class Colour:
    def __init__(
        self,
        name: str,
        colour: ColorBase | None = None,
        nameNull: bool = False,
        alpha: float = 1.0,
    ): ...
```

### Colour().__eq__

[Show source in colourswatch.py:102](../../../colourswatch/colourswatch.py#L102)

equals

#### Signature

```python
def __eq__(self, other: Colour) -> bool: ...
```

### Colour().__repr__

[Show source in colourswatch.py:84](../../../colourswatch/colourswatch.py#L84)

get a string representation of the object

#### Signature

```python
def __repr__(self): ...
```

### Colour().colorToTuple

[Show source in colourswatch.py:131](../../../colourswatch/colourswatch.py#L131)

get the colour as a tuple. eg. sRGBColor -> (r, g, b)

#### Signature

```python
def colorToTuple(self) -> tuple[float, ...]: ...
```

### Colour().convertedColourToHexTuple

[Show source in colourswatch.py:145](../../../colourswatch/colourswatch.py#L145)

get the previously converted colour as a tuple of hexstrings. eg.
sRGBColor -> ("ff", "ff", "ff")

#### Arguments

- `uppercase` *bool, optional* - return hex in uppercase. Defaults to False.

#### Returns

- `tuple` - tuple of hexstrings

#### Signature

```python
def convertedColourToHexTuple(self, uppercase: bool = False) -> tuple[str, ...]: ...
```

### Colour().convertedColourToTuple

[Show source in colourswatch.py:137](../../../colourswatch/colourswatch.py#L137)

get the previously converted colour as a tuple. eg.
sRGBColor -> (r, g, b)

#### Signature

```python
def convertedColourToTuple(self) -> tuple[float, ...]: ...
```

### Colour().getRGB255

[Show source in colourswatch.py:160](../../../colourswatch/colourswatch.py#L160)

get the colour as an rgb 255 tuple

#### Signature

```python
def getRGB255(self) -> tuple[int, ...]: ...
```

### Colour().getRGB255Hex

[Show source in colourswatch.py:165](../../../colourswatch/colourswatch.py#L165)

get the colour as an rgb 255 tuple in hex

#### Signature

```python
def getRGB255Hex(self, uppercase: bool = False) -> tuple[str, ...]: ...
```

### Colour().toCMYK

[Show source in colourswatch.py:111](../../../colourswatch/colourswatch.py#L111)

convert to cmyk and dump a copy in self.convertedColour

#### Signature

```python
def toCMYK(self) -> CMYKColor: ...
```

### Colour().toHSL

[Show source in colourswatch.py:121](../../../colourswatch/colourswatch.py#L121)

convert to hsl and dump a copy in self.convertedColour

#### Signature

```python
def toHSL(self) -> HSLColor: ...
```

### Colour().toHSV

[Show source in colourswatch.py:116](../../../colourswatch/colourswatch.py#L116)

convert to hsv and dump a copy in self.convertedColour

#### Signature

```python
def toHSV(self) -> HSVColor: ...
```

### Colour().toLAB

[Show source in colourswatch.py:126](../../../colourswatch/colourswatch.py#L126)

convert to lab and dump a copy in self.convertedColour

#### Signature

```python
def toLAB(self) -> LabColor: ...
```

### Colour().toRGB

[Show source in colourswatch.py:106](../../../colourswatch/colourswatch.py#L106)

convert to rgb and dump a copy in self.convertedColour

#### Signature

```python
def toRGB(self) -> sRGBColor: ...
```



## ColourSwatch

[Show source in colourswatch.py:20](../../../colourswatch/colourswatch.py#L20)

this represents a colour swatch

#### Signature

```python
class ColourSwatch:
    def __init__(
        self,
        name: str,
        colours: list[Colour] | None = None,
        swatchId: str | None = None,
        description: str | None = None,
        swatchCopyright: str | None = None,
        author: str | None = None,
    ): ...
```

### ColourSwatch().__eq__

[Show source in colourswatch.py:61](../../../colourswatch/colourswatch.py#L61)

probably not ideal for getting equality - avoid using ==

#### Signature

```python
def __eq__(self, other: ColourSwatch): ...
```

### ColourSwatch().__repr__

[Show source in colourswatch.py:57](../../../colourswatch/colourswatch.py#L57)

get a string representation of the object

#### Signature

```python
def __repr__(self) -> str: ...
```

### ColourSwatch().toPILPalette

[Show source in colourswatch.py:39](../../../colourswatch/colourswatch.py#L39)

Convert the ColourSwatch object to a pil palette

Usage:

```python
image = PIL.Image.new('P', (1, 1))
image.putpalette(colourSwatch.toPILPalette())
```

#### Signature

```python
def toPILPalette(self) -> list[int]: ...
```