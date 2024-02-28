# Gimpgplpal

[Colourswatch Index](../README.md#colourswatch-index) / [Colourswatch](./index.md#colourswatch) / Gimpgplpal

> Auto-generated documentation for [colourswatch.gimpgplpal](../../../colourswatch/gimpgplpal.py) module.

- [Gimpgplpal](#gimpgplpal)
  - [GimpGplPalette](#gimpgplpalette)
    - [GimpGplPalette().__eq__](#gimpgplpalette()__eq__)
    - [GimpGplPalette().__repr__](#gimpgplpalette()__repr__)
    - [GimpGplPalette().__str__](#gimpgplpalette()__str__)
    - [GimpGplPalette().decode](#gimpgplpalette()decode)
    - [GimpGplPalette().encode](#gimpgplpalette()encode)
    - [GimpGplPalette().load](#gimpgplpalette()load)
    - [GimpGplPalette().save](#gimpgplpalette()save)

## GimpGplPalette

[Show source in gimpgplpal.py:9](../../../colourswatch/gimpgplpal.py#L9)

Pure python implementation of the gimp gpl palette format.

#### Signature

```python
class GimpGplPalette:
    def __init__(self, file: BytesIO | str | Path | None = None) -> None: ...
```

### GimpGplPalette().__eq__

[Show source in gimpgplpal.py:119](../../../colourswatch/gimpgplpal.py#L119)

Perform a comparison.

#### Signature

```python
def __eq__(self, other: GimpGplPalette) -> bool: ...
```

### GimpGplPalette().__repr__

[Show source in gimpgplpal.py:99](../../../colourswatch/gimpgplpal.py#L99)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpGplPalette().__str__

[Show source in gimpgplpal.py:115](../../../colourswatch/gimpgplpal.py#L115)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGplPalette().decode

[Show source in gimpgplpal.py:42](../../../colourswatch/gimpgplpal.py#L42)

Decode a byte buffer.

#### Arguments

----
 - `data` *str* - data buffer to decode

#### Raises

------
 - `Exception` - File format error.  Magic value mismatch.

#### Signature

```python
def decode(self, data: str) -> None: ...
```

### GimpGplPalette().encode

[Show source in gimpgplpal.py:72](../../../colourswatch/gimpgplpal.py#L72)

Encode to a raw data stream.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGplPalette().load

[Show source in gimpgplpal.py:28](../../../colourswatch/gimpgplpal.py#L28)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, file: BytesIO | str | Path) -> None: ...
```

### GimpGplPalette().save

[Show source in gimpgplpal.py:89](../../../colourswatch/gimpgplpal.py#L89)

Save this gimp image to a file.

#### Signature

```python
def save(self, file: BytesIO | str | Path) -> None: ...
```