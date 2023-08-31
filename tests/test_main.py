"""Test module """

from __future__ import annotations

import sys
from json import loads
from pathlib import Path

from tomlkit import loads as tloads
from yaml import safe_load

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
import colourswatch.io


# GPL
def test_gpl():
	gpl = colourswatch.io.openColourSwatch(f"{THISDIR}/data/plasma.gpl")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/plasma(gpl).gpl", gpl)
	source = Path(f"{THISDIR}/data/plasma.gpl")
	dest = Path(f"{THISDIR}/data/plasma(gpl).gpl")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# YAML
def test_yaml():
	yaml = colourswatch.io.openColourSwatch(f"{THISDIR}/data/base24.yaml")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/base24(yaml).gpl", yaml)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/base24(yaml).yaml", yaml)
	source = safe_load(Path(f"{THISDIR}/data/base24.yaml").read_text(encoding="utf-8"))
	dest = safe_load(Path(f"{THISDIR}/data/base24(yaml).yaml").read_text(encoding="utf-8"))
	assert source == dest


# COLORS
def test_colors():
	colors = colourswatch.io.openColourSwatch(f"{THISDIR}/data/40.colors")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/40(colors).gpl", colors)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/40(colors).colors", colors)
	source = Path(f"{THISDIR}/data/40.colors")
	dest = Path(f"{THISDIR}/data/40(colors).colors")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# SPL
def test_spl():
	spl = colourswatch.io.openColourSwatch(f"{THISDIR}/data/mini.spl")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/mini(spl).gpl", spl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/mini(spl).spl", spl)
	source = Path(f"{THISDIR}/data/mini.spl")
	dest = Path(f"{THISDIR}/data/mini(spl).spl")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# SKP
def test_skp():
	skp = colourswatch.io.openColourSwatch(f"{THISDIR}/data/example.skp")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/example(skp).gpl", skp)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/example(skp).skp", skp)
	assert Path(f"{THISDIR}/data/example.skp").read_text(encoding="utf-8") == Path(
		f"{THISDIR}/data/example(skp).skp"
	).read_text(encoding="utf-8")


# SOC
def test_soc():
	soc = colourswatch.io.openColourSwatch(f"{THISDIR}/data/series.soc")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/series(soc).gpl", soc)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/series(soc).skp", soc)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/series(soc).soc", soc)
	assert Path(f"{THISDIR}/data/series.soc").read_text(encoding="utf-8") == Path(
		f"{THISDIR}/data/series(soc).soc"
	).read_text(encoding="utf-8")


# TXT
def test_txt():
	txt = colourswatch.io.openColourSwatch(f"{THISDIR}/data/defaultpdn.txt")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/defaultpdn(txt).gpl", txt)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/defaultpdn(txt).skp", txt)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/defaultpdn(txt).txt", txt)
	source = Path(f"{THISDIR}/data/defaultpdn.txt")
	dest = Path(f"{THISDIR}/data/defaultpdn(txt).txt")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# ACBL
def test_acbl():
	acbl = colourswatch.io.openColourSwatch(f"{THISDIR}/data/colours.acbl")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/colours(acbl).gpl", acbl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/colours(acbl).skp", acbl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/colours(acbl).txt", acbl)


# XML
def test_xml():
	xml = colourswatch.io.openColourSwatch(f"{THISDIR}/data/scribus.xml")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/scribus(xml).gpl", xml)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/scribus(xml).skp", xml)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/scribus(xml).xml", xml)
	assert Path(f"{THISDIR}/data/scribus.xml").read_text(encoding="utf-8") == Path(
		f"{THISDIR}/data/scribus(xml).xml"
	).read_text(encoding="utf-8")


# CDPAl
def test_cdpal():
	pal = colourswatch.io.openColourSwatch(f"{THISDIR}/data/coreldraw.pal")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/coreldraw(pal).gpl", pal)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/coreldraw(pal).skp", pal)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/coreldraw(pal).pal", pal)
	source = Path(f"{THISDIR}/data/coreldraw.pal")
	dest = Path(f"{THISDIR}/data/coreldraw(pal).pal")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# PSPPAL
def test_psppal():
	pal = colourswatch.io.openColourSwatch(f"{THISDIR}/data/paintshoppro.pal")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/paintshoppro(pal).gpl", pal)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/paintshoppro(pal).skp", pal)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/paintshoppro(pal).pal", pal)
	source = Path(f"{THISDIR}/data/paintshoppro.pal")
	dest = Path(f"{THISDIR}/data/paintshoppro(pal).pal")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# HPL
def test_hpl():
	hpl = colourswatch.io.openColourSwatch(f"{THISDIR}/data/example.hpl")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/example(hpl).gpl", hpl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/example(hpl).skp", hpl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/example(hpl).hpl", hpl)
	source = Path(f"{THISDIR}/data/example.hpl")
	dest = Path(f"{THISDIR}/data/example(hpl).hpl")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# TOML
def test_toml():
	toml = colourswatch.io.openColourSwatch(f"{THISDIR}/data/base24.toml")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/base24(toml).gpl", toml)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/base24(toml).toml", toml)
	source = tloads(Path(f"{THISDIR}/data/base24.toml").read_text(encoding="utf-8"))
	dest = tloads(Path(f"{THISDIR}/data/base24(toml).toml").read_text(encoding="utf-8"))
	assert source == dest


# JSON
def test_json():
	json = colourswatch.io.openColourSwatch(f"{THISDIR}/data/base24.json")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/base24(json).gpl", json)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/base24(json).json", json)
	source = loads(Path(f"{THISDIR}/data/base24.json").read_text(encoding="utf-8"))
	dest = loads(Path(f"{THISDIR}/data/base24(json).json").read_text(encoding="utf-8"))
	assert source == dest


# PNG
def test_png():
	png = colourswatch.io.openColourSwatch(f"{THISDIR}/data/colours.png")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/colours(png).gpl", png)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/colours(png).png", png)
	compare = colourswatch.io.openColourSwatch(f"{THISDIR}/data/colours(png).png")
	assert len(png.colours) == len(compare.colours)


# JPG
def test_jpg():
	jpg = colourswatch.io.openColourSwatch(f"{THISDIR}/data/colours.jpg")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/colours(jpg).gpl", jpg)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/colours(jpg).jpg", jpg)
	compare = colourswatch.io.openColourSwatch(f"{THISDIR}/data/colours(jpg).jpg")
	assert len(jpg.colours) == len(compare.colours)


# WEBP
def test_webp():
	webp = colourswatch.io.openColourSwatch(f"{THISDIR}/data/colours.webp")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/colours(webp).gpl", webp)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/colours(webp).webp", webp)
	compare = colourswatch.io.openColourSwatch(f"{THISDIR}/data/colours(webp).webp")
	assert len(webp.colours) == len(compare.colours)


# ASE
def test_ase():
	# ase can hold multiple swatches so openColourSwatch will return a list of these
	ase = colourswatch.io.openColourSwatch(f"{THISDIR}/data/solarized.ase")[0]
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/solarized(ase).gpl", ase)


# SVG
def test_svg():
	svg = colourswatch.io.openColourSwatch(f"{THISDIR}/data/ai.svg")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/ai(svg).gpl", svg)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/data/ai(svg).svg", svg)


if __name__ == "__main__":
	test_gpl()
	test_yaml()
	test_colors()
	test_spl()
	test_skp()
	test_soc()
	test_txt()
	test_acbl()
	test_xml()
	test_cdpal()
	test_psppal()
	test_hpl()
	test_toml()
	test_json()
	test_png()
	test_jpg()
	test_webp()
	test_ase()
	test_svg()
