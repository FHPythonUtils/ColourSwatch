<a name=".colourswatch"></a>
## colourswatch

Use this module to read, and write to a number of colour palette file formats

<a name=".colourswatch.colourswatch"></a>
## colourswatch.colourswatch

hold colourswatch data and provide a series of helper methods such as the
ability to convert to to a pillow palette.

<a name=".colourswatch.colourswatch.ColourSwatch"></a>
### ColourSwatch

```python
class ColourSwatch():
 |  ColourSwatch(name, colours=None, swatchId=None, description=None, swatchCopyright=None, author=None)
```

this represents a colour swatch

<a name=".colourswatch.colourswatch.ColourSwatch.toPILPalette"></a>
#### toPILPalette

```python
 | toPILPalette()
```

Convert the ColourSwatch object to a pil palette

<a name=".colourswatch.colourswatch.Colour"></a>
### Colour

```python
class Colour():
 |  Colour(name, colour=None, nameNull=False, alpha=1.0)
```

this represents a single colour within the colour swatch

<a name=".colourswatch.colourswatch.Colour.toRGB"></a>
#### toRGB

```python
 | toRGB()
```

convert to rgb and dump a copy in self.convertedColour

<a name=".colourswatch.colourswatch.Colour.toCMYK"></a>
#### toCMYK

```python
 | toCMYK()
```

convert to cmyk and dump a copy in self.convertedColour

<a name=".colourswatch.colourswatch.Colour.toHSV"></a>
#### toHSV

```python
 | toHSV()
```

convert to hsv and dump a copy in self.convertedColour

<a name=".colourswatch.colourswatch.Colour.toHSL"></a>
#### toHSL

```python
 | toHSL()
```

convert to hsl and dump a copy in self.convertedColour

<a name=".colourswatch.colourswatch.Colour.toLAB"></a>
#### toLAB

```python
 | toLAB()
```

convert to lab and dump a copy in self.convertedColour

<a name=".colourswatch.colourswatch.Colour.colorToTuple"></a>
#### colorToTuple

```python
 | colorToTuple()
```

get the colour as a tuple. eg. sRGBColor -> (r, g, b)

<a name=".colourswatch.colourswatch.Colour.convertedColourToTuple"></a>
#### convertedColourToTuple

```python
 | convertedColourToTuple()
```

get the previously converted colour as a tuple. eg.
sRGBColor -> (r, g, b)

<a name=".colourswatch.io"></a>
## colourswatch.io

do file io

<a name=".colourswatch.io.extNotRecognised"></a>
#### extNotRecognised

```python
extNotRecognised(fileName)
```

Output the file extension not recognised error

<a name=".colourswatch.io.openColourSwatch"></a>
#### openColourSwatch

```python
openColourSwatch(file)
```

Open a colour swatch file into a layer image object

**Arguments**:

- `file` _string_ - path/ filename

**Returns**:

- `ColourSwatch` - a colour swatch object

<a name=".colourswatch.io.saveColourSwatch"></a>
#### saveColourSwatch

```python
saveColourSwatch(fileName, colourSwatch)
```

Save a colour swatch to a file

**Arguments**:

- `fileName` _string_ - path/ filename
- `colourSwatch` _ColourSwatch_ - the colour swatch to save

<a name=".colourswatch.io.getColourFromLine"></a>
#### getColourFromLine

```python
getColourFromLine(line, lineno, colourSpaceSize=3, colourSpace=sRGBColor, divider=255)
```

getColourFromLine

<a name=".colourswatch.io.getSwatchFromFileName"></a>
#### getSwatchFromFileName

```python
getSwatchFromFileName(file, colours)
```

getSwatchFromFileName

<a name=".colourswatch.io.getWriteOutColour"></a>
#### getWriteOutColour

```python
getWriteOutColour(colour, convertType=int, multiplier=255)
```

getWriteOutColour

<a name=".colourswatch.io.openSwatch_GPL"></a>
#### openSwatch\_GPL

```python
openSwatch_GPL(file)
```

Open a .GPL into a colour swatch

<a name=".colourswatch.io.saveSwatch_GPL"></a>
#### saveSwatch\_GPL

```python
saveSwatch_GPL(fileName, colourSwatch)
```

Save a colour swatch as .GPL

<a name=".colourswatch.io.openSwatch_YAML"></a>
#### openSwatch\_YAML

```python
openSwatch_YAML(file)
```

Open a .YAML into a colour swatch

<a name=".colourswatch.io.saveSwatch_YAML"></a>
#### saveSwatch\_YAML

```python
saveSwatch_YAML(fileName, colourSwatch)
```

Save a colour swatch as .YAML

<a name=".colourswatch.io.openSwatch_COLOR"></a>
#### openSwatch\_COLOR

```python
openSwatch_COLOR(file)
```

Open a .COLOR into a colour swatch

<a name=".colourswatch.io.saveSwatch_COLOR"></a>
#### saveSwatch\_COLOR

```python
saveSwatch_COLOR(fileName, colourSwatch)
```

Save a colour swatch as .COLOR

<a name=".colourswatch.io.openSwatch_SPL"></a>
#### openSwatch\_SPL

```python
openSwatch_SPL(file)
```

Open a .SPL into a colour swatch

<a name=".colourswatch.io.saveSwatch_SPL"></a>
#### saveSwatch\_SPL

```python
saveSwatch_SPL(fileName, colourSwatch)
```

Save a colour swatch as .SPL

<a name=".colourswatch.io.openSwatch_SKP"></a>
#### openSwatch\_SKP

```python
openSwatch_SKP(file)
```

Open a .SKP into a colour swatch

<a name=".colourswatch.io.saveSwatch_SKP"></a>
#### saveSwatch\_SKP

```python
saveSwatch_SKP(fileName, colourSwatch)
```

Save a colour swatch as .SKP

<a name=".colourswatch.io.openSwatch_SOC"></a>
#### openSwatch\_SOC

```python
openSwatch_SOC(file)
```

Open a .SOC into a colour swatch

<a name=".colourswatch.io.saveSwatch_SOC"></a>
#### saveSwatch\_SOC

```python
saveSwatch_SOC(fileName, colourSwatch)
```

Save a colour swatch as .SOC

<a name=".colourswatch.io.openSwatch_TXT"></a>
#### openSwatch\_TXT

```python
openSwatch_TXT(file)
```

Open a .TXT into a colour swatch

<a name=".colourswatch.io.saveSwatch_TXT"></a>
#### saveSwatch\_TXT

```python
saveSwatch_TXT(fileName, colourSwatch)
```

Save a colour swatch as .TXT

<a name=".colourswatch.io.openSwatch_ACBL"></a>
#### openSwatch\_ACBL

```python
openSwatch_ACBL(file)
```

Open a .ACBL into a colour swatch

<a name=".colourswatch.io.saveSwatch_ACBL"></a>
#### saveSwatch\_ACBL

```python
saveSwatch_ACBL(fileName, colourSwatch)
```

Save a colour swatch as .ACBL

<a name=".colourswatch.io.openSwatch_XML"></a>
#### openSwatch\_XML

```python
openSwatch_XML(file)
```

Open a .XML into a colour swatch

<a name=".colourswatch.io.saveSwatch_XML"></a>
#### saveSwatch\_XML

```python
saveSwatch_XML(fileName, colourSwatch)
```

Save a colour swatch as .XML

<a name=".colourswatch.io.openSwatch_PSPPAL"></a>
#### openSwatch\_PSPPAL

```python
openSwatch_PSPPAL(file)
```

Open a PaintShopPro .PAL into a colour swatch

<a name=".colourswatch.io.saveSwatch_PSPPAL"></a>
#### saveSwatch\_PSPPAL

```python
saveSwatch_PSPPAL(fileName, colourSwatch)
```

Save a colour swatch as PaintShopPro .PAL

<a name=".colourswatch.io.openSwatch_CDPAL"></a>
#### openSwatch\_CDPAL

```python
openSwatch_CDPAL(file)
```

Open a CorelDraw .PAL into a colour swatch

<a name=".colourswatch.io.saveSwatch_CDPAL"></a>
#### saveSwatch\_CDPAL

```python
saveSwatch_CDPAL(fileName, colourSwatch)
```

Save a colour swatch as CorelDraw .PAL

<a name=".colourswatch.io.openSwatch_HPL"></a>
#### openSwatch\_HPL

```python
openSwatch_HPL(file)
```

Open a .HPL into a colour swatch

<a name=".colourswatch.io.saveSwatch_HPL"></a>
#### saveSwatch\_HPL

```python
saveSwatch_HPL(fileName, colourSwatch)
```

Save a colour swatch as .HPL

<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

