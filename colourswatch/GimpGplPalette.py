#!/usr/bin/env python3
"""
Pure python implementation of the gimp gpl palette format
"""
from __future__ import annotations
from io import BytesIO
from typing import Union

class GimpGplPalette:
	""" Pure python implementation of the gimp gpl palette format """
	def __init__(self, fileName: Union[BytesIO, str, None]=None):
		self.name = ""
		self.columns = 16
		self.colors = []
		self.colorNames = []
		if fileName is not None:
			self.load(fileName)

	def load(self, fileName: Union[BytesIO, str]):
		"""
		load a gimp file

		:param fileName: can be a file name or a file-like object
		"""
		if isinstance(fileName, str):
			self.fileName = fileName
			file = open(fileName, "r")
		else:
			self.fileName = fileName.name
			file = fileName
		data = file.read()
		file.close()
		self.decode(data)

	def decode(self, data: str) -> None:
		"""
		decode a byte buffer

		:param data: data buffer to decode
		"""
		lines = [s.strip() for s in data.split("\n")]
		if lines[0] != "GIMP Palette":
			raise Exception("File format error.  Magic value mismatch.")
		self.name = lines[1].split(":", 1)[-1].lstrip()
		self.columns = int(lines[2].split(":", 1)[-1].lstrip())
		for line in lines[3:]:
			if len(line) < 1 or line[0] == "#": # Commented Line
				continue
			line = line.split(None, 4)
			if len(line) < 3:
				continue
			self.colors.append((int(line[0]), int(line[1]), int(line[2])))
			if len(line) > 3:
				self.colorNames.append(line[3])
			else:
				self.colorNames.append(None)

	def encode(self):
		""" encode to a raw data stream """
		data = []
		data.append("GIMP Palette")
		data.append("Name: " + str(self.name))
		data.append("Columns: " + str(self.columns))
		data.append("#")
		for i, color in enumerate(self.colors):
			colorName = self.colorNames[i]
			line = str(color[0]).rjust(3) + " " + str(color[1]).rjust(3) + " " + str(
			color[2]).rjust(3)
			if colorName is not None:
				line = line + "\t" + colorName
			data.append(line)
		return ("\n".join(data) + "\n").encode("utf-8")

	def save(self, fileName: Union[str, BytesIO]):
		""" save this gimp image to a file """
		if isinstance(fileName, str):
			file = open(fileName, "wb")
		else:
			file = fileName
		file.write(self.encode())
		file.close()

	def __repr__(self, indent: str=""):
		""" Get a textual representation of this object """
		ret = []
		if self.fileName is not None:
			ret.append("fileName: " + self.fileName)
		ret.append("Name: " + str(self.name))
		ret.append("Columns: " + str(self.columns))
		ret.append("Colors:")
		for i, color in enumerate(self.colors):
			colorName = self.colorNames[i]
			line = "(%d,%d,%d)" % color[0], color[1], color[2]
			if colorName is not None:
				line = line + " " + colorName
		return "\n".join(ret)

	def __eq__(self, other: GimpGplPalette):
		""" perform a comparison """
		if other.name != self.name:
			return False
		if other.columns != self.columns:
			return False
		if len(self.colors) != len(other.colors):
			return False
		for i, c in enumerate(self.colors):
			if c != other.colors[i]:
				return False
			if self.colorNames[i] != other.colorNames[i]:
				return False
		return True
