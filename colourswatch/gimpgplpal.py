"""Pure python implementation of the gimp gpl palette format."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path


class GimpGplPalette:
	"""Pure python implementation of the gimp gpl palette format."""

	def __init__(self, file: BytesIO | str | Path | None = None) -> None:
		"""Pure python implementation of the gimp gpl palette format.

		Args:
		----
			file (BytesIO | str| Path | None): filename. Defaults to None.

		"""
		self.name = ""
		self.columns = 16
		self.colors = []
		self.colorNames = []
		self.fileName = None
		if file is not None:
			self.load(file)

	def load(self, file: BytesIO | str | Path) -> None:
		"""Load a gimp file.

		:param fileName: can be a file name or a file-like object
		"""
		if isinstance(file, BytesIO):
			with file as file:
				self.decode(file.read().decode("utf-8"))
				self.fileName = file.name
			return
		pth = Path(file)
		self.decode(pth.read_text("utf-8"))
		self.fileName = pth.name

	def decode(self, data: str) -> None:
		"""Decode a byte buffer.

		Args:
		----
			data (str): data buffer to decode

		Raises:
		------
			Exception: File format error.  Magic value mismatch.

		"""
		lines = [s.strip() for s in data.split("\n")]
		if lines[0] != "GIMP Palette":
			msg = "File format error.  Magic value mismatch."
			raise RuntimeError(msg)
		self.name = lines[1].split(":", 1)[-1].lstrip()
		self.columns = int(lines[2].split(":", 1)[-1].lstrip())
		for line in lines[3:]:
			if len(line) < 1 or line[0] == "#":  # Commented Line
				continue
			line = line.split(None, 4)
			if len(line) < 3:
				continue
			self.colors.append((int(line[0]), int(line[1]), int(line[2])))
			if len(line) > 3:
				self.colorNames.append(line[3])
			else:
				self.colorNames.append(None)

	def encode(self) -> bytes:
		"""Encode to a raw data stream."""
		data = []
		data.append("GIMP Palette")
		data.append(f"Name: {self.name}")
		data.append(f"Columns: {self.columns}")
		data.append("#")
		for i, color in enumerate(self.colors):
			colorName = self.colorNames[i]
			line = (
				str(color[0]).rjust(3) + " " + str(color[1]).rjust(3) + " " + str(color[2]).rjust(3)
			)
			if colorName is not None:
				line = line + "\t" + colorName
			data.append(line)
		return ("\n".join(data) + "\n").encode("utf-8")

	def save(self, file: BytesIO | str | Path) -> None:
		"""Save this gimp image to a file."""
		data = self.encode()
		if isinstance(file, BytesIO):
			with file as file:
				file.write(data)
			return
		pth = Path(file)
		pth.write_bytes(data)

	def __repr__(self) -> str:
		"""Get a textual representation of this object."""
		ret = []
		if self.fileName is not None:
			ret.append(f"File Name: {self.fileName}")
		ret.append(f"Name: {self.name}")
		ret.append(f"Columns: {self.columns}")
		ret.append("Colors:")
		for i, color in enumerate(self.colors):
			colorName = self.colorNames[i]
			line = f"{color[0]},{color[1]},{color[2]}"
			if colorName is not None:
				line = line + " " + colorName
			ret.append(line)
		return "\n".join(ret)

	def __str__(self) -> str:
		"""Get a textual representation of this object."""
		return self.__repr__()

	def __eq__(self, other: GimpGplPalette) -> bool:
		"""Perform a comparison."""
		if other.name != self.name:
			return False
		if other.columns != self.columns:
			return False
		if len(self.colors) != len(other.colors):
			return False
		for i, colour in enumerate(self.colors):
			if colour != other.colors[i]:
				return False
			if self.colorNames[i] != other.colorNames[i]:
				return False
		return True
