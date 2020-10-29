# GimpGplPalette

> Auto-generated documentation for [colourswatch.GimpGplPalette](../../colourswatch/GimpGplPalette.py) module.

Pure python implementation of the gimp gpl palette format

- [Colourswatch](../README.md#colourswatch-index) / [Modules](../README.md#colourswatch-modules) / [colourswatch](index.md#colourswatch) / GimpGplPalette
    - [GimpGplPalette](#gimpgplpalette)
        - [GimpGplPalette().\_\_eq\_\_](#gimpgplpalette__eq__)
        - [GimpGplPalette().\_\_repr\_\_](#gimpgplpalette__repr__)
        - [GimpGplPalette().decode](#gimpgplpalettedecode)
        - [GimpGplPalette().encode](#gimpgplpaletteencode)
        - [GimpGplPalette().load](#gimpgplpaletteload)
        - [GimpGplPalette().save](#gimpgplpalettesave)

## GimpGplPalette

[[find in source code]](../../colourswatch/GimpGplPalette.py#L9)

```python
class GimpGplPalette():
    def __init__(fileName: Union[(BytesIO, str, None)] = None):
```

Pure python implementation of the gimp gpl palette format

### GimpGplPalette().\_\_eq\_\_

[[find in source code]](../../colourswatch/GimpGplPalette.py#L98)

```python
def __eq__(other: GimpGplPalette):
```

perform a comparison

### GimpGplPalette().\_\_repr\_\_

[[find in source code]](../../colourswatch/GimpGplPalette.py#L83)

```python
def __repr__(indent: str = ''):
```

Get a textual representation of this object

### GimpGplPalette().decode

[[find in source code]](../../colourswatch/GimpGplPalette.py#L35)

```python
def decode(data: str) -> None:
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode

### GimpGplPalette().encode

[[find in source code]](../../colourswatch/GimpGplPalette.py#L58)

```python
def encode():
```

encode to a raw data stream

### GimpGplPalette().load

[[find in source code]](../../colourswatch/GimpGplPalette.py#L19)

```python
def load(fileName: Union[(BytesIO, str)]):
```

load a gimp file

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGplPalette().save

[[find in source code]](../../colourswatch/GimpGplPalette.py#L74)

```python
def save(fileName: Union[(str, BytesIO)]):
```

save this gimp image to a file
