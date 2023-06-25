# Io

[Colourswatch Index](../README.md#colourswatch-index) /
[Colourswatch](./index.md#colourswatch) /
Io

> Auto-generated documentation for [colourswatch.io](../../../colourswatch/io.py) module.

- [Io](#io)
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

[Show source in io.py:40](../../../colourswatch/io.py#L40)

Output the file extension not recognised error

#### Signature

```python
def extNotRecognised(fileName: str):
    ...
```



## getColourFromLine

[Show source in io.py:150](../../../colourswatch/io.py#L150)

getColourFromLine

#### Signature

```python
def getColourFromLine(
    line: str,
    lineno: int,
    colourSpaceSize: int = 3,
    colourSpace: ColorBase = sRGBColor,
    divider: int = 255,
):
    ...
```



## getSwatchFromFileName

[Show source in io.py:166](../../../colourswatch/io.py#L166)

getSwatchFromFileName

#### Signature

```python
def getSwatchFromFileName(file: str, colours: list[Colour]):
    ...
```

#### See also

- [Colour](./colourswatch.md#colour)



## getWriteOutColour

[Show source in io.py:171](../../../colourswatch/io.py#L171)

getWriteOutColour

#### Signature

```python
def getWriteOutColour(
    colour: Iterable[Any], convertType: type = int, multiplier: int = 255
) -> list[Any]:
    ...
```



## openColourSwatch

[Show source in io.py:67](../../../colourswatch/io.py#L67)

Open a colour swatch file into a layer image object

#### Arguments

- `file` *str* - path/ filename

#### Raises

- `FileExistsError` - [description]
- `ValueError` - [description]

#### Returns

- `ColourSwatch` - a colour swatch object

#### Signature

```python
def openColourSwatch(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_ACBL

[Show source in io.py:494](../../../colourswatch/io.py#L494)

Open a .ACBL into a colour swatch

#### Signature

```python
def openSwatch_ACBL(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_ASE

[Show source in io.py:649](../../../colourswatch/io.py#L649)

Open an .ase into a list of colour swatches

#### Signature

```python
def openSwatch_ASE(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_CDPAL

[Show source in io.py:587](../../../colourswatch/io.py#L587)

Open a CorelDraw .PAL into a colour swatch

#### Signature

```python
def openSwatch_CDPAL(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_COLOR

[Show source in io.py:306](../../../colourswatch/io.py#L306)

Open a .COLOR into a colour swatch

#### Signature

```python
def openSwatch_COLOR(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_GPL

[Show source in io.py:179](../../../colourswatch/io.py#L179)

Open a .GPL into a colour swatch

#### Signature

```python
def openSwatch_GPL(file: str):
    ...
```



## openSwatch_HPL

[Show source in io.py:625](../../../colourswatch/io.py#L625)

Open a .HPL into a colour swatch

#### Signature

```python
def openSwatch_HPL(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_IMAGE

[Show source in io.py:697](../../../colourswatch/io.py#L697)

open .jpg, .webp

#### Signature

```python
def openSwatch_IMAGE(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_JSON

[Show source in io.py:242](../../../colourswatch/io.py#L242)

Open a .JSON into a colour swatch

#### Signature

```python
def openSwatch_JSON(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_PNG

[Show source in io.py:679](../../../colourswatch/io.py#L679)

Open a .png into a colour swatch

#### Signature

```python
def openSwatch_PNG(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_PSPPAL

[Show source in io.py:563](../../../colourswatch/io.py#L563)

Open a PaintShopPro .PAL into a colour swatch

#### Signature

```python
def openSwatch_PSPPAL(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_SKP

[Show source in io.py:360](../../../colourswatch/io.py#L360)

Open a .SKP into a colour swatch

#### Signature

```python
def openSwatch_SKP(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_SOC

[Show source in io.py:397](../../../colourswatch/io.py#L397)

Open a .SOC into a colour swatch

#### Signature

```python
def openSwatch_SOC(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_SPL

[Show source in io.py:330](../../../colourswatch/io.py#L330)

Open a .SPL into a colour swatch

#### Signature

```python
def openSwatch_SPL(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_SVG

[Show source in io.py:736](../../../colourswatch/io.py#L736)

Open a .svg into a colour swatch

#### Signature

```python
def openSwatch_SVG(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_TOML

[Show source in io.py:274](../../../colourswatch/io.py#L274)

Open a .TOML into a colour swatch

#### Signature

```python
def openSwatch_TOML(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_TXT

[Show source in io.py:453](../../../colourswatch/io.py#L453)

Open a .TXT into a colour swatch

#### Signature

```python
def openSwatch_TXT(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_XML

[Show source in io.py:518](../../../colourswatch/io.py#L518)

Open a .XML into a colour swatch

#### Signature

```python
def openSwatch_XML(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_YAML

[Show source in io.py:210](../../../colourswatch/io.py#L210)

Open a .YAML into a colour swatch

#### Signature

```python
def openSwatch_YAML(file: str) -> ColourSwatch:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## prettify

[Show source in io.py:29](../../../colourswatch/io.py#L29)

Return a pretty-printed XML string for the Element.

#### Signature

```python
def prettify(
    elem: Element,
    indent: str = "\t",
    doctype: str = '<?xml version="1.0" encoding="utf-8"?>',
):
    ...
```



## saveColourSwatch

[Show source in io.py:110](../../../colourswatch/io.py#L110)

Save a colour swatch to a file

#### Arguments

- `fileName` *str* - path/ filename
- `colourSwatch` *ColourSwatch* - the colour swatch to save

#### Raises

- `ValueError` - [description]

#### Returns

- `None` - [description]

#### Signature

```python
def saveColourSwatch(fileName: str, colourSwatch: ColourSwatch) -> None:
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_ACBL

[Show source in io.py:512](../../../colourswatch/io.py#L512)

Save a colour swatch as .ACBL

#### Signature

```python
def saveSwatch_ACBL(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_ASE

[Show source in io.py:673](../../../colourswatch/io.py#L673)

Save a colour swatch as .ase

#### Signature

```python
def saveSwatch_ASE(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_CDPAL

[Show source in io.py:600](../../../colourswatch/io.py#L600)

Save a colour swatch as CorelDraw .PAL

#### Signature

```python
def saveSwatch_CDPAL(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_COLOR

[Show source in io.py:314](../../../colourswatch/io.py#L314)

Save a colour swatch as .COLOR

#### Signature

```python
def saveSwatch_COLOR(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_GPL

[Show source in io.py:196](../../../colourswatch/io.py#L196)

Save a colour swatch as .GPL

#### Signature

```python
def saveSwatch_GPL(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_HPL

[Show source in io.py:633](../../../colourswatch/io.py#L633)

Save a colour swatch as .HPL

#### Signature

```python
def saveSwatch_HPL(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_IMAGE

[Show source in io.py:716](../../../colourswatch/io.py#L716)

Save a colour swatch as .png, .jpg, .webp

#### Signature

```python
def saveSwatch_IMAGE(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_JSON

[Show source in io.py:265](../../../colourswatch/io.py#L265)

Save a colour swatch as .JSON

#### Signature

```python
def saveSwatch_JSON(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_PSPPAL

[Show source in io.py:571](../../../colourswatch/io.py#L571)

Save a colour swatch as PaintShopPro .PAL

#### Signature

```python
def saveSwatch_PSPPAL(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_SKP

[Show source in io.py:382](../../../colourswatch/io.py#L382)

Save a colour swatch as .SKP

#### Signature

```python
def saveSwatch_SKP(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_SOC

[Show source in io.py:409](../../../colourswatch/io.py#L409)

Save a colour swatch as .SOC

#### Signature

```python
def saveSwatch_SOC(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_SPL

[Show source in io.py:338](../../../colourswatch/io.py#L338)

Save a colour swatch as .SPL

#### Signature

```python
def saveSwatch_SPL(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_SVG

[Show source in io.py:770](../../../colourswatch/io.py#L770)

Save a colour swatch as .svg

#### Signature

```python
def saveSwatch_SVG(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_TOML

[Show source in io.py:297](../../../colourswatch/io.py#L297)

Save a colour swatch as .TOML

#### Signature

```python
def saveSwatch_TOML(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_TXT

[Show source in io.py:471](../../../colourswatch/io.py#L471)

Save a colour swatch as .TXT

#### Signature

```python
def saveSwatch_TXT(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_XML

[Show source in io.py:539](../../../colourswatch/io.py#L539)

Save a colour swatch as .XML

#### Signature

```python
def saveSwatch_XML(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_YAML

[Show source in io.py:233](../../../colourswatch/io.py#L233)

Save a colour swatch as .YAML

#### Signature

```python
def saveSwatch_YAML(fileName: str, colourSwatch: ColourSwatch):
    ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)


