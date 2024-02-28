# Io

[Colourswatch Index](../README.md#colourswatch-index) / [Colourswatch](./index.md#colourswatch) / Io

> Auto-generated documentation for [colourswatch.io](../../../colourswatch/io.py) module.

- [Io](#io)
  - [extNotRecognised](#extnotrecognised)
  - [getColourFromLine](#getcolourfromline)
  - [getSwatchFromfile](#getswatchfromfile)
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

[Show source in io.py:38](../../../colourswatch/io.py#L38)

Output the file extension not recognised error.

#### Signature

```python
def extNotRecognised(file: str | Path) -> str: ...
```



## getColourFromLine

[Show source in io.py:144](../../../colourswatch/io.py#L144)

GetColourFromLine.

#### Signature

```python
def getColourFromLine(
    line: str,
    lineno: int,
    colourSpaceSize: int = 3,
    colourSpace: ColorBase = sRGBColor,
    divider: int = 255,
) -> Colour: ...
```

#### See also

- [Colour](./colourswatch.md#colour)



## getSwatchFromfile

[Show source in io.py:160](../../../colourswatch/io.py#L160)

GetSwatchFromfile.

#### Signature

```python
def getSwatchFromfile(file: str | Path, colours: list[Colour]) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)
- [Colour](./colourswatch.md#colour)



## getWriteOutColour

[Show source in io.py:165](../../../colourswatch/io.py#L165)

GetWriteOutColour.

#### Signature

```python
def getWriteOutColour(
    colour: Iterable[Any], convertType: type = int, multiplier: int = 255
) -> list[Any]: ...
```



## openColourSwatch

[Show source in io.py:47](../../../colourswatch/io.py#L47)

Open a colour swatch file into a layer image object.

#### Arguments

----
 - `file` *str* - path/ file

#### Raises

------
 - `FileExistsError` - [description]
 - `ValueError` - [description]

#### Returns

-------
 ColourSwatch | list[ColourSwatch]: a colour swatch object

#### Signature

```python
def openColourSwatch(file: str | Path) -> ColourSwatch | list[ColourSwatch]: ...
```



## openSwatch_ACBL

[Show source in io.py:495](../../../colourswatch/io.py#L495)

Open a .ACBL into a colour swatch.

#### Signature

```python
def openSwatch_ACBL(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_ASE

[Show source in io.py:653](../../../colourswatch/io.py#L653)

Open an .ase into a list of colour swatches.

#### Signature

```python
def openSwatch_ASE(file: str | Path) -> list[ColourSwatch]: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_CDPAL

[Show source in io.py:590](../../../colourswatch/io.py#L590)

Open a CorelDraw .PAL into a colour swatch.

#### Signature

```python
def openSwatch_CDPAL(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_COLOR

[Show source in io.py:302](../../../colourswatch/io.py#L302)

Open a .COLOR into a colour swatch.

#### Signature

```python
def openSwatch_COLOR(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_GPL

[Show source in io.py:173](../../../colourswatch/io.py#L173)

Open a .GPL into a colour swatch.

#### Signature

```python
def openSwatch_GPL(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_HPL

[Show source in io.py:628](../../../colourswatch/io.py#L628)

Open a .HPL into a colour swatch.

#### Signature

```python
def openSwatch_HPL(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_IMAGE

[Show source in io.py:702](../../../colourswatch/io.py#L702)

Open .jpg, .webp.

#### Signature

```python
def openSwatch_IMAGE(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_JSON

[Show source in io.py:238](../../../colourswatch/io.py#L238)

Open a .JSON into a colour swatch.

#### Signature

```python
def openSwatch_JSON(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_PNG

[Show source in io.py:684](../../../colourswatch/io.py#L684)

Open a .png into a colour swatch.

#### Signature

```python
def openSwatch_PNG(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_PSPPAL

[Show source in io.py:565](../../../colourswatch/io.py#L565)

Open a PaintShopPro .PAL into a colour swatch.

#### Signature

```python
def openSwatch_PSPPAL(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_SKP

[Show source in io.py:358](../../../colourswatch/io.py#L358)

Open a .SKP into a colour swatch.

#### Signature

```python
def openSwatch_SKP(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_SOC

[Show source in io.py:395](../../../colourswatch/io.py#L395)

Open a .SOC into a colour swatch.

#### Signature

```python
def openSwatch_SOC(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_SPL

[Show source in io.py:327](../../../colourswatch/io.py#L327)

Open a .SPL into a colour swatch.

#### Signature

```python
def openSwatch_SPL(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_SVG

[Show source in io.py:741](../../../colourswatch/io.py#L741)

Open a .svg into a colour swatch.

#### Signature

```python
def openSwatch_SVG(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_TOML

[Show source in io.py:270](../../../colourswatch/io.py#L270)

Open a .TOML into a colour swatch.

#### Signature

```python
def openSwatch_TOML(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_TXT

[Show source in io.py:453](../../../colourswatch/io.py#L453)

Open a .TXT into a colour swatch.

#### Signature

```python
def openSwatch_TXT(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_XML

[Show source in io.py:520](../../../colourswatch/io.py#L520)

Open a .XML into a colour swatch.

#### Signature

```python
def openSwatch_XML(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## openSwatch_YAML

[Show source in io.py:206](../../../colourswatch/io.py#L206)

Open a .YAML into a colour swatch.

#### Signature

```python
def openSwatch_YAML(file: str | Path) -> ColourSwatch: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## prettify

[Show source in io.py:27](../../../colourswatch/io.py#L27)

Return a pretty-printed XML string for the Element.

#### Signature

```python
def prettify(
    elem: Element,
    indent: str = "\t",
    doctype: str = '<?xml version="1.0" encoding="utf-8"?>',
) -> str: ...
```



## saveColourSwatch

[Show source in io.py:95](../../../colourswatch/io.py#L95)

Save a colour swatch to a file.

#### Arguments

----
 - `file` *str* - path/ file
 colourSwatch (ColourSwatch | list[ColourSwatch]): the colour swatch(es) to save

#### Raises

------
 - `ValueError` - [description]

#### Returns

-------
 - `None` - [description]

#### Signature

```python
def saveColourSwatch(
    file: str | Path, colourSwatch: ColourSwatch | list[ColourSwatch]
) -> None: ...
```



## saveSwatch_ACBL

[Show source in io.py:513](../../../colourswatch/io.py#L513)

Save a colour swatch as .ACBL.

#### Signature

```python
def saveSwatch_ACBL(file: str | Path, colourSwatch: ColourSwatch) -> NoReturn: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_ASE

[Show source in io.py:677](../../../colourswatch/io.py#L677)

Save a colour swatch as .ase.

#### Signature

```python
def saveSwatch_ASE(file: str | Path, colourSwatch: ColourSwatch) -> NoReturn: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_CDPAL

[Show source in io.py:603](../../../colourswatch/io.py#L603)

Save a colour swatch as CorelDraw .PAL.

#### Signature

```python
def saveSwatch_CDPAL(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_COLOR

[Show source in io.py:311](../../../colourswatch/io.py#L311)

Save a colour swatch as .COLOR.

#### Signature

```python
def saveSwatch_COLOR(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_GPL

[Show source in io.py:192](../../../colourswatch/io.py#L192)

Save a colour swatch as .GPL.

#### Signature

```python
def saveSwatch_GPL(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_HPL

[Show source in io.py:637](../../../colourswatch/io.py#L637)

Save a colour swatch as .HPL.

#### Signature

```python
def saveSwatch_HPL(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_IMAGE

[Show source in io.py:721](../../../colourswatch/io.py#L721)

Save a colour swatch as .png, .jpg, .webp.

#### Signature

```python
def saveSwatch_IMAGE(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_JSON

[Show source in io.py:261](../../../colourswatch/io.py#L261)

Save a colour swatch as .JSON.

#### Signature

```python
def saveSwatch_JSON(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_PSPPAL

[Show source in io.py:574](../../../colourswatch/io.py#L574)

Save a colour swatch as PaintShopPro .PAL.

#### Signature

```python
def saveSwatch_PSPPAL(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_SKP

[Show source in io.py:380](../../../colourswatch/io.py#L380)

Save a colour swatch as .SKP.

#### Signature

```python
def saveSwatch_SKP(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_SOC

[Show source in io.py:409](../../../colourswatch/io.py#L409)

Save a colour swatch as .SOC.

#### Signature

```python
def saveSwatch_SOC(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_SPL

[Show source in io.py:336](../../../colourswatch/io.py#L336)

Save a colour swatch as .SPL.

#### Signature

```python
def saveSwatch_SPL(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_SVG

[Show source in io.py:777](../../../colourswatch/io.py#L777)

Save a colour swatch as .svg.

#### Signature

```python
def saveSwatch_SVG(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_TOML

[Show source in io.py:293](../../../colourswatch/io.py#L293)

Save a colour swatch as .TOML.

#### Signature

```python
def saveSwatch_TOML(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_TXT

[Show source in io.py:472](../../../colourswatch/io.py#L472)

Save a colour swatch as .TXT.

#### Signature

```python
def saveSwatch_TXT(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_XML

[Show source in io.py:541](../../../colourswatch/io.py#L541)

Save a colour swatch as .XML.

#### Signature

```python
def saveSwatch_XML(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)



## saveSwatch_YAML

[Show source in io.py:229](../../../colourswatch/io.py#L229)

Save a colour swatch as .YAML.

#### Signature

```python
def saveSwatch_YAML(file: str | Path, colourSwatch: ColourSwatch) -> None: ...
```

#### See also

- [ColourSwatch](./colourswatch.md#colourswatch)