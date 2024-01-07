# Gimpgplpalette

[Colourswatch Index](../README.md#colourswatch-index) /
[Colourswatch](./index.md#colourswatch) /
Gimpgplpalette

> Auto-generated documentation for [colourswatch.GimpGplPalette](../../../colourswatch/GimpGplPalette.py) module.

- [Gimpgplpalette](#gimpgplpalette)
  - [GimpGplPalette](#gimpgplpalette)
    - [GimpGplPalette().__eq__](#gimpgplpalette()__eq__)
    - [GimpGplPalette().__repr__](#gimpgplpalette()__repr__)
    - [GimpGplPalette().decode](#gimpgplpalette()decode)
    - [GimpGplPalette().encode](#gimpgplpalette()encode)
    - [GimpGplPalette().load](#gimpgplpalette()load)
    - [GimpGplPalette().save](#gimpgplpalette()save)

## GimpGplPalette

[Show source in GimpGplPalette.py:8](../../../colourswatch/GimpGplPalette.py#L8)

Pure python implementation of the gimp gpl palette format.

#### Signature

```python
class GimpGplPalette:
    def __init__(self, fileName: BytesIO | str | None = None): ...
```

### GimpGplPalette().__eq__

[Show source in GimpGplPalette.py:106](../../../colourswatch/GimpGplPalette.py#L106)

Perform a comparison.

#### Signature

```python
def __eq__(self, other: GimpGplPalette): ...
```

### GimpGplPalette().__repr__

[Show source in GimpGplPalette.py:91](../../../colourswatch/GimpGplPalette.py#L91)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self): ...
```

### GimpGplPalette().decode

[Show source in GimpGplPalette.py:39](../../../colourswatch/GimpGplPalette.py#L39)

Decode a byte buffer.

#### Arguments

- `data` *str* - data buffer to decode

#### Raises

- `Exception` - File format error.  Magic value mismatch.

#### Signature

```python
def decode(self, data: str) -> None: ...
```

### GimpGplPalette().encode

[Show source in GimpGplPalette.py:65](../../../colourswatch/GimpGplPalette.py#L65)

Encode to a raw data stream.

#### Signature

```python
def encode(self): ...
```

### GimpGplPalette().load

[Show source in GimpGplPalette.py:24](../../../colourswatch/GimpGplPalette.py#L24)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str): ...
```

### GimpGplPalette().save

[Show source in GimpGplPalette.py:82](../../../colourswatch/GimpGplPalette.py#L82)

Save this gimp image to a file.

#### Signature

```python
def save(self, fileName: str | BytesIO): ...
```