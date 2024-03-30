"""Test module"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

import pytest
import tomli
from yaml import safe_load

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from colourswatch.io import openColourSwatch, saveColourSwatch


def _src_eq_dest(source_file: str, dest_file: str) -> bool:
	source = Path(source_file)
	dest = Path(dest_file)
	colourSwatch = openColourSwatch(source)
	saveColourSwatch(dest, colourSwatch)
	return source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


def _convert_eq_dest(source_file: str, cmp_file: str) -> bool:
	source = Path(source_file)
	cmp = Path(cmp_file)
	colourSwatch = openColourSwatch(source)

	with tempfile.NamedTemporaryFile(suffix=cmp.suffix, delete=False) as tmp:
		pth = Path(tmp.name)
		saveColourSwatch(pth, colourSwatch)
		dest = pth.read_text(encoding="utf-8")

	return dest == cmp.read_text(encoding="utf-8")


def test_not_exists() -> None:
	with pytest.raises(FileExistsError):
		openColourSwatch("not_exists")


def test_unsupported() -> None:
	with pytest.raises(ValueError, match="File extension is not recognised for file"):
		openColourSwatch(f"{THISDIR}/data/xyz.xyz")


# GPL
def test_roundtrip_gpl() -> None:
	assert _src_eq_dest(f"{THISDIR}/data/plasma.gpl", f"{THISDIR}/data/plasma(gpl).gpl")


# YAML
def test_roundtrip_yaml() -> None:
	yaml = openColourSwatch(f"{THISDIR}/data/base24.yaml")
	saveColourSwatch(f"{THISDIR}/data/base24(yaml).gpl", yaml)
	saveColourSwatch(f"{THISDIR}/data/base24(yaml).yaml", yaml)
	source = safe_load(Path(f"{THISDIR}/data/base24.yaml").read_text(encoding="utf-8"))
	dest = safe_load(Path(f"{THISDIR}/data/base24(yaml).yaml").read_text(encoding="utf-8"))
	assert source == dest


# COLORS
def test_roundtrip_colors() -> None:
	assert _src_eq_dest(f"{THISDIR}/data/40.colors", f"{THISDIR}/data/40(colors).colors")


def test_colors_gpl() -> None:
	assert _convert_eq_dest(f"{THISDIR}/data/40.colors", f"{THISDIR}/data/40(colors).gpl")


# SPL
def test_roundtrip_spl() -> None:
	assert _src_eq_dest(f"{THISDIR}/data/mini.spl", f"{THISDIR}/data/mini(spl).spl")


def test_spl_gpl() -> None:
	assert _convert_eq_dest(f"{THISDIR}/data/mini.spl", f"{THISDIR}/data/mini(spl).gpl")


# SKP
# def test_roundtrip_skp() -> None:
# 	assert _src_eq_dest(f"{THISDIR}/data/example.skp", f"{THISDIR}/data/example(skp).skp")


def test_skp_gpl() -> None:
	assert _convert_eq_dest(f"{THISDIR}/data/example.skp", f"{THISDIR}/data/example(skp).gpl")


# SOC
def test_roundtrip_soc() -> None:
	assert _src_eq_dest(f"{THISDIR}/data/series.soc", f"{THISDIR}/data/series(soc).soc")


def test_soc_gpl() -> None:
	assert _convert_eq_dest(f"{THISDIR}/data/series.soc", f"{THISDIR}/data/series(soc).gpl")


def test_soc_skp() -> None:
	assert _convert_eq_dest(f"{THISDIR}/data/series.soc", f"{THISDIR}/data/series(soc).skp")


# TXT
def test_roundtrip_txt() -> None:
	assert _src_eq_dest(f"{THISDIR}/data/defaultpdn.txt", f"{THISDIR}/data/defaultpdn(txt).txt")


# ACBL
def test_acbl() -> None:
	acbl = openColourSwatch(f"{THISDIR}/data/colours.acbl")
	saveColourSwatch(f"{THISDIR}/data/colours(acbl).gpl", acbl)
	saveColourSwatch(f"{THISDIR}/data/colours(acbl).skp", acbl)
	saveColourSwatch(f"{THISDIR}/data/colours(acbl).txt", acbl)


# XML
# def test_roundtrip_xml() -> None:
# 	assert _src_eq_dest(f"{THISDIR}/data/scribus.xml", f"{THISDIR}/data/scribus(xml).xml")


# CDPAl
def test_roundtrip_cdpal() -> None:
	assert _src_eq_dest(f"{THISDIR}/data/coreldraw.pal", f"{THISDIR}/data/coreldraw(pal).pal")


# PSPPAL
def test_roundtrip_psppal() -> None:
	assert _src_eq_dest(f"{THISDIR}/data/paintshoppro.pal", f"{THISDIR}/data/paintshoppro(pal).pal")


# HPL
def test_roundtrip_hpl() -> None:
	assert _src_eq_dest(f"{THISDIR}/data/example.hpl", f"{THISDIR}/data/example(hpl).hpl")


# TOML
def test_roundtrip_toml() -> None:
	toml = openColourSwatch(f"{THISDIR}/data/base24.toml")
	saveColourSwatch(f"{THISDIR}/data/base24(toml).gpl", toml)
	saveColourSwatch(f"{THISDIR}/data/base24(toml).toml", toml)
	source = tomli.loads(Path(f"{THISDIR}/data/base24.toml").read_text(encoding="utf-8"))
	dest = tomli.loads(Path(f"{THISDIR}/data/base24(toml).toml").read_text(encoding="utf-8"))
	assert source == dest


# JSON
def test_roundtrip_json() -> None:
	_json = openColourSwatch(f"{THISDIR}/data/base24.json")
	saveColourSwatch(f"{THISDIR}/data/base24(json).gpl", _json)
	saveColourSwatch(f"{THISDIR}/data/base24(json).json", _json)
	source = json.loads(Path(f"{THISDIR}/data/base24.json").read_text(encoding="utf-8"))
	dest = json.loads(Path(f"{THISDIR}/data/base24(json).json").read_text(encoding="utf-8"))
	assert source == dest


# PNG
def test_roundtrip_png() -> None:
	png = openColourSwatch(f"{THISDIR}/data/colours.png")
	saveColourSwatch(f"{THISDIR}/data/colours(png).gpl", png)
	saveColourSwatch(f"{THISDIR}/data/colours(png).png", png)
	compare = openColourSwatch(f"{THISDIR}/data/colours(png).png")
	assert len(png.colours) == len(compare.colours)


# JPG
def test_roundtrip_jpg() -> None:
	jpg = openColourSwatch(f"{THISDIR}/data/colours.jpg")
	saveColourSwatch(f"{THISDIR}/data/colours(jpg).gpl", jpg)
	saveColourSwatch(f"{THISDIR}/data/colours(jpg).jpg", jpg)
	compare = openColourSwatch(f"{THISDIR}/data/colours(jpg).jpg")
	assert len(jpg.colours) == len(compare.colours)


# WEBP
def test_roundtrip_webp() -> None:
	webp = openColourSwatch(f"{THISDIR}/data/colours.webp")
	saveColourSwatch(f"{THISDIR}/data/colours(webp).gpl", webp)
	saveColourSwatch(f"{THISDIR}/data/colours(webp).webp", webp)
	compare = openColourSwatch(f"{THISDIR}/data/colours(webp).webp")
	assert len(webp.colours) == len(compare.colours)


# ASE
def test_ase() -> None:
	# ase can hold multiple swatches so openColourSwatch will return a list of these
	ase = openColourSwatch(f"{THISDIR}/data/solarized.ase")[0]
	saveColourSwatch(f"{THISDIR}/data/solarized(ase).gpl", ase)


# SVG
def test_roundtrip_svg() -> None:
	svg = openColourSwatch(f"{THISDIR}/data/ai.svg")
	saveColourSwatch(f"{THISDIR}/data/ai(svg).gpl", svg)
	saveColourSwatch(f"{THISDIR}/data/ai(svg).svg", svg)
