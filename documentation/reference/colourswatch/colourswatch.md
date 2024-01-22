# ColourSwatch

[Colourswatch Index](../README.md#colourswatch-index) / [Colourswatch](./index.md#colourswatch) / ColourSwatch

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

[Show source in colourswatch.py:78](../../../colourswatch/colourswatch.py#L78)

Represent a single colour within the colour swatch.

#### Signature

```python
class Colour:
    def __init__(
        self,
        name: str,
        colour: ColorBase | None = None,
        nameNull: bool = False,
        alpha: float = 1.0,
    ) -> None: ...
```

### Colour().__eq__

[Show source in colourswatch.py:118](../../../colourswatch/colourswatch.py#L118)

Equals.

#### Signature

```python
def __eq__(self, other: Colour) -> bool: ...
```

### Colour().__repr__

[Show source in colourswatch.py:104](../../../colourswatch/colourswatch.py#L104)

Get a string representation of the object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### Colour().colorToTuple

[Show source in colourswatch.py:147](../../../colourswatch/colourswatch.py#L147)

Get the colour as a tuple. eg. sRGBColor -> (r, g, b).

#### Signature

```python
def colorToTuple(self) -> tuple[float, ...]: ...
```

### Colour().convertedColourToHexTuple

[Show source in colourswatch.py:161](../../../colourswatch/colourswatch.py#L161)

Get the previously converted colour as a tuple of hexstrings. eg.
sRGBColor -> ("ff", "ff", "ff").

#### Arguments

----
 - `uppercase` *bool, optional* - return hex in uppercase. Defaults to False.

#### Returns

-------
 - `tuple` - tuple of hexstrings

#### Signature

```python
def convertedColourToHexTuple(self, uppercase: bool = False) -> tuple[str, ...]: ...
```

### Colour().convertedColourToTuple

[Show source in colourswatch.py:153](../../../colourswatch/colourswatch.py#L153)

Get the previously converted colour as a tuple. eg.
sRGBColor -> (r, g, b).

#### Signature

```python
def convertedColourToTuple(self) -> tuple[float, ...]: ...
```

### Colour().getRGB255

[Show source in colourswatch.py:178](../../../colourswatch/colourswatch.py#L178)

Get the colour as an rgb 255 tuple.

#### Signature

```python
def getRGB255(self) -> tuple[int, ...]: ...
```

### Colour().getRGB255Hex

[Show source in colourswatch.py:183](../../../colourswatch/colourswatch.py#L183)

Get the colour as an rgb 255 tuple in hex.

#### Signature

```python
def getRGB255Hex(self, uppercase: bool = False) -> tuple[str, ...]: ...
```

### Colour().toCMYK

[Show source in colourswatch.py:127](../../../colourswatch/colourswatch.py#L127)

Convert to cmyk and dump a copy in self.convertedColour.

#### Signature

```python
def toCMYK(self) -> CMYKColor: ...
```

### Colour().toHSL

[Show source in colourswatch.py:137](../../../colourswatch/colourswatch.py#L137)

Convert to hsl and dump a copy in self.convertedColour.

#### Signature

```python
def toHSL(self) -> HSLColor: ...
```

### Colour().toHSV

[Show source in colourswatch.py:132](../../../colourswatch/colourswatch.py#L132)

Convert to hsv and dump a copy in self.convertedColour.

#### Signature

```python
def toHSV(self) -> HSVColor: ...
```

### Colour().toLAB

[Show source in colourswatch.py:142](../../../colourswatch/colourswatch.py#L142)

Convert to lab and dump a copy in self.convertedColour.

#### Signature

```python
def toLAB(self) -> LabColor: ...
```

### Colour().toRGB

[Show source in colourswatch.py:122](../../../colourswatch/colourswatch.py#L122)

Convert to rgb and dump a copy in self.convertedColour.

#### Signature

```python
def toRGB(self) -> sRGBColor: ...
```



## ColourSwatch

[Show source in colourswatch.py:19](../../../colourswatch/colourswatch.py#L19)

Represents a colour swatch.

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
    ) -> None: ...
```

### ColourSwatch().__eq__

[Show source in colourswatch.py:71](../../../colourswatch/colourswatch.py#L71)

Probably not ideal for getting equality - avoid using ==.

#### Signature

```python
def __eq__(self, other: ColourSwatch) -> bool: ...
```

### ColourSwatch().__repr__

[Show source in colourswatch.py:67](../../../colourswatch/colourswatch.py#L67)

Get a string representation of the object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### ColourSwatch().toPILPalette

[Show source in colourswatch.py:49](../../../colourswatch/colourswatch.py#L49)

Convert the ColourSwatch object to a pil palette.

Usage:

```python
image = PIL.Image.new('P', (1, 1))
image.putpalette(colourSwatch.toPILPalette())
```

#### Signature

```python
def toPILPalette(self) -> list[int]: ...
```