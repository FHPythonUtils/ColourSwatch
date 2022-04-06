# Io

> Auto-generated documentation for [colourswatch.io](../../../colourswatch/io.py) module.

do file io

- [Colourswatch](../README.md#colourswatch-index) / [Modules](../MODULES.md#colourswatch-modules) / [Colourswatch](index.md#colourswatch) / Io
    - [extNotRecognised](#extnotrecognised)
    - [getColourFromLine](#getcolourfromline)
    - [getSwatchFromFileName](#getswatchfromfilename)
    - [getWriteOutColour](#getwriteoutcolour)
    - [openColourSwatch](#opencolourswatch)
    - [openSwatch_ACBL](#openswatch_acbl)
    - [openSwatch_ASE](#openswatch_ase)
    - [openSwatch_CDPAL](#openswatch_cdpal)
    - [openSwatch_COLOR](#openswatch_color)
    - [openSwatch_GPL](#openswatch_gpl)
    - [openSwatch_HPL](#openswatch_hpl)
    - [openSwatch_IMAGE](#openswatch_image)
    - [openSwatch_JSON](#openswatch_json)
    - [openSwatch_PNG](#openswatch_png)
    - [openSwatch_PSPPAL](#openswatch_psppal)
    - [openSwatch_SKP](#openswatch_skp)
    - [openSwatch_SOC](#openswatch_soc)
    - [openSwatch_SPL](#openswatch_spl)
    - [openSwatch_SVG](#openswatch_svg)
    - [openSwatch_TOML](#openswatch_toml)
    - [openSwatch_TXT](#openswatch_txt)
    - [openSwatch_XML](#openswatch_xml)
    - [openSwatch_YAML](#openswatch_yaml)
    - [prettify](#prettify)
    - [saveColourSwatch](#savecolourswatch)
    - [saveSwatch_ACBL](#saveswatch_acbl)
    - [saveSwatch_ASE](#saveswatch_ase)
    - [saveSwatch_CDPAL](#saveswatch_cdpal)
    - [saveSwatch_COLOR](#saveswatch_color)
    - [saveSwatch_GPL](#saveswatch_gpl)
    - [saveSwatch_HPL](#saveswatch_hpl)
    - [saveSwatch_IMAGE](#saveswatch_image)
    - [saveSwatch_JSON](#saveswatch_json)
    - [saveSwatch_PSPPAL](#saveswatch_psppal)
    - [saveSwatch_SKP](#saveswatch_skp)
    - [saveSwatch_SOC](#saveswatch_soc)
    - [saveSwatch_SPL](#saveswatch_spl)
    - [saveSwatch_SVG](#saveswatch_svg)
    - [saveSwatch_TOML](#saveswatch_toml)
    - [saveSwatch_TXT](#saveswatch_txt)
    - [saveSwatch_XML](#saveswatch_xml)
    - [saveSwatch_YAML](#saveswatch_yaml)

## extNotRecognised

[[find in source code]](../../../colourswatch/io.py#L40)

```python
def extNotRecognised(fileName: str):
```

Output the file extension not recognised error

## getColourFromLine

[[find in source code]](../../../colourswatch/io.py#L150)

```python
def getColourFromLine(
    line: str,
    lineno: int,
    colourSpaceSize: int = 3,
    colourSpace: ColorBase = sRGBColor,
    divider: int = 255,
):
```

getColourFromLine

## getSwatchFromFileName

[[find in source code]](../../../colourswatch/io.py#L166)

```python
def getSwatchFromFileName(file: str, colours: list[Colour]):
```

getSwatchFromFileName

#### See also

- [Colour](colourswatch.md#colour)

## getWriteOutColour

[[find in source code]](../../../colourswatch/io.py#L171)

```python
def getWriteOutColour(
    colour: Iterable[Any],
    convertType: type = int,
    multiplier: int = 255,
) -> list[Any]:
```

getWriteOutColour

## openColourSwatch

[[find in source code]](../../../colourswatch/io.py#L67)

```python
def openColourSwatch(file: str) -> ColourSwatch:
```

Open a colour swatch file into a layer image object

#### Arguments

- `file` *str* - path/ filename

#### Raises

- `FileExistsError` - [description]
- `ValueError` - [description]

#### Returns

- `ColourSwatch` - a colour swatch object

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_ACBL

[[find in source code]](../../../colourswatch/io.py#L494)

```python
def openSwatch_ACBL(file: str) -> ColourSwatch:
```

Open a .ACBL into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_ASE

[[find in source code]](../../../colourswatch/io.py#L649)

```python
def openSwatch_ASE(file: str) -> ColourSwatch:
```

Open an .ase into a list of colour swatches

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_CDPAL

[[find in source code]](../../../colourswatch/io.py#L587)

```python
def openSwatch_CDPAL(file: str) -> ColourSwatch:
```

Open a CorelDraw .PAL into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_COLOR

[[find in source code]](../../../colourswatch/io.py#L306)

```python
def openSwatch_COLOR(file: str) -> ColourSwatch:
```

Open a .COLOR into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_GPL

[[find in source code]](../../../colourswatch/io.py#L179)

```python
def openSwatch_GPL(file: str):
```

Open a .GPL into a colour swatch

## openSwatch_HPL

[[find in source code]](../../../colourswatch/io.py#L625)

```python
def openSwatch_HPL(file: str) -> ColourSwatch:
```

Open a .HPL into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_IMAGE

[[find in source code]](../../../colourswatch/io.py#L697)

```python
def openSwatch_IMAGE(file: str) -> ColourSwatch:
```

open .jpg, .webp

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_JSON

[[find in source code]](../../../colourswatch/io.py#L242)

```python
def openSwatch_JSON(file: str) -> ColourSwatch:
```

Open a .JSON into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_PNG

[[find in source code]](../../../colourswatch/io.py#L679)

```python
def openSwatch_PNG(file: str) -> ColourSwatch:
```

Open a .png into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_PSPPAL

[[find in source code]](../../../colourswatch/io.py#L563)

```python
def openSwatch_PSPPAL(file: str) -> ColourSwatch:
```

Open a PaintShopPro .PAL into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_SKP

[[find in source code]](../../../colourswatch/io.py#L360)

```python
def openSwatch_SKP(file: str) -> ColourSwatch:
```

Open a .SKP into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_SOC

[[find in source code]](../../../colourswatch/io.py#L397)

```python
def openSwatch_SOC(file: str) -> ColourSwatch:
```

Open a .SOC into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_SPL

[[find in source code]](../../../colourswatch/io.py#L330)

```python
def openSwatch_SPL(file: str) -> ColourSwatch:
```

Open a .SPL into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_SVG

[[find in source code]](../../../colourswatch/io.py#L736)

```python
def openSwatch_SVG(file: str) -> ColourSwatch:
```

Open a .svg into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_TOML

[[find in source code]](../../../colourswatch/io.py#L274)

```python
def openSwatch_TOML(file: str) -> ColourSwatch:
```

Open a .TOML into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_TXT

[[find in source code]](../../../colourswatch/io.py#L453)

```python
def openSwatch_TXT(file: str) -> ColourSwatch:
```

Open a .TXT into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_XML

[[find in source code]](../../../colourswatch/io.py#L518)

```python
def openSwatch_XML(file: str) -> ColourSwatch:
```

Open a .XML into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## openSwatch_YAML

[[find in source code]](../../../colourswatch/io.py#L210)

```python
def openSwatch_YAML(file: str) -> ColourSwatch:
```

Open a .YAML into a colour swatch

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## prettify

[[find in source code]](../../../colourswatch/io.py#L29)

```python
def prettify(
    elem: Element,
    indent: str = '\t',
    doctype: str = '<?xml version="1.0" encoding="utf-8"?>',
):
```

Return a pretty-printed XML string for the Element.

## saveColourSwatch

[[find in source code]](../../../colourswatch/io.py#L110)

```python
def saveColourSwatch(fileName: str, colourSwatch: ColourSwatch) -> None:
```

Save a colour swatch to a file

#### Arguments

- `fileName` *str* - path/ filename
- `colourSwatch` *ColourSwatch* - the colour swatch to save

#### Raises

- `ValueError` - [description]

#### Returns

- `None` - [description]

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_ACBL

[[find in source code]](../../../colourswatch/io.py#L512)

```python
def saveSwatch_ACBL(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .ACBL

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_ASE

[[find in source code]](../../../colourswatch/io.py#L673)

```python
def saveSwatch_ASE(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .ase

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_CDPAL

[[find in source code]](../../../colourswatch/io.py#L600)

```python
def saveSwatch_CDPAL(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as CorelDraw .PAL

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_COLOR

[[find in source code]](../../../colourswatch/io.py#L314)

```python
def saveSwatch_COLOR(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .COLOR

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_GPL

[[find in source code]](../../../colourswatch/io.py#L196)

```python
def saveSwatch_GPL(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .GPL

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_HPL

[[find in source code]](../../../colourswatch/io.py#L633)

```python
def saveSwatch_HPL(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .HPL

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_IMAGE

[[find in source code]](../../../colourswatch/io.py#L716)

```python
def saveSwatch_IMAGE(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .png, .jpg, .webp

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_JSON

[[find in source code]](../../../colourswatch/io.py#L265)

```python
def saveSwatch_JSON(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .JSON

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_PSPPAL

[[find in source code]](../../../colourswatch/io.py#L571)

```python
def saveSwatch_PSPPAL(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as PaintShopPro .PAL

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_SKP

[[find in source code]](../../../colourswatch/io.py#L382)

```python
def saveSwatch_SKP(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .SKP

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_SOC

[[find in source code]](../../../colourswatch/io.py#L409)

```python
def saveSwatch_SOC(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .SOC

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_SPL

[[find in source code]](../../../colourswatch/io.py#L338)

```python
def saveSwatch_SPL(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .SPL

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_SVG

[[find in source code]](../../../colourswatch/io.py#L770)

```python
def saveSwatch_SVG(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .svg

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_TOML

[[find in source code]](../../../colourswatch/io.py#L297)

```python
def saveSwatch_TOML(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .TOML

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_TXT

[[find in source code]](../../../colourswatch/io.py#L471)

```python
def saveSwatch_TXT(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .TXT

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_XML

[[find in source code]](../../../colourswatch/io.py#L539)

```python
def saveSwatch_XML(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .XML

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)

## saveSwatch_YAML

[[find in source code]](../../../colourswatch/io.py#L233)

```python
def saveSwatch_YAML(fileName: str, colourSwatch: ColourSwatch):
```

Save a colour swatch as .YAML

#### See also

- [ColourSwatch](colourswatch.md#colourswatch)
