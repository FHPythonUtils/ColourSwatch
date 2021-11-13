"""Test module """

import sys
from json import loads
from pathlib import Path

from tomlkit import loads as tloads
from yaml import safe_load

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
import colourswatch.io

# pylint: disable=missing-function-docstring, invalid-name, wrong-import-position

# GPL
def test_gpl():
	gpl = colourswatch.io.openColourSwatch(f"{THISDIR}/plasma.gpl")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/plasma(gpl).gpl", gpl)
	source = Path(f"{THISDIR}/plasma.gpl")
	dest = Path(f"{THISDIR}/plasma(gpl).gpl")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# YAML
def test_yaml():
	yaml = colourswatch.io.openColourSwatch(f"{THISDIR}/base24.yaml")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/base24(yaml).gpl", yaml)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/base24(yaml).yaml", yaml)
	with Path(f"{THISDIR}/base24.yaml") as yaml:
		source = safe_load(yaml.read_text(encoding="utf-8"))
	with Path(f"{THISDIR}/base24(yaml).yaml") as yaml:
		dest = safe_load(yaml.read_text(encoding="utf-8"))
	assert source == dest


# COLORS
def test_colors():
	colors = colourswatch.io.openColourSwatch(f"{THISDIR}/40.colors")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/40(colors).gpl", colors)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/40(colors).colors", colors)
	source = Path(f"{THISDIR}/40.colors")
	dest = Path(f"{THISDIR}/40(colors).colors")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# SPL
def test_spl():
	spl = colourswatch.io.openColourSwatch(f"{THISDIR}/mini.spl")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/mini(spl).gpl", spl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/mini(spl).spl", spl)
	source = Path(f"{THISDIR}/mini.spl")
	dest = Path(f"{THISDIR}/mini(spl).spl")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# SKP
def test_skp():
	skp = colourswatch.io.openColourSwatch(f"{THISDIR}/example.skp")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/example(skp).gpl", skp)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/example(skp).skp", skp)
	assert Path(f"{THISDIR}/example.skp").read_text(encoding="utf-8") == Path(
		f"{THISDIR}/example(skp).skp"
	).read_text(encoding="utf-8")


# SOC
def test_soc():
	soc = colourswatch.io.openColourSwatch(f"{THISDIR}/series.soc")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/series(soc).gpl", soc)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/series(soc).skp", soc)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/series(soc).soc", soc)
	assert Path(f"{THISDIR}/series.soc").read_text(encoding="utf-8") == Path(
		f"{THISDIR}/series(soc).soc"
	).read_text(encoding="utf-8")


# TXT
def test_txt():
	txt = colourswatch.io.openColourSwatch(f"{THISDIR}/defaultpdn.txt")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/defaultpdn(txt).gpl", txt)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/defaultpdn(txt).skp", txt)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/defaultpdn(txt).txt", txt)
	source = Path(f"{THISDIR}/defaultpdn.txt")
	dest = Path(f"{THISDIR}/defaultpdn(txt).txt")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# ACBL
def test_acbl():
	acbl = colourswatch.io.openColourSwatch(f"{THISDIR}/colours.acbl")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/colours(acbl).gpl", acbl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/colours(acbl).skp", acbl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/colours(acbl).txt", acbl)


# XML
def test_xml():
	xml = colourswatch.io.openColourSwatch(f"{THISDIR}/scribus.xml")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/scribus(xml).gpl", xml)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/scribus(xml).skp", xml)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/scribus(xml).xml", xml)
	assert Path(f"{THISDIR}/scribus.xml").read_text(encoding="utf-8") == Path(
		f"{THISDIR}/scribus(xml).xml"
	).read_text(encoding="utf-8")


# CDPAl
def test_cdpal():
	pal = colourswatch.io.openColourSwatch(f"{THISDIR}/coreldraw.pal")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/coreldraw(pal).gpl", pal)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/coreldraw(pal).skp", pal)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/coreldraw(pal).pal", pal)
	source = Path(f"{THISDIR}/coreldraw.pal")
	dest = Path(f"{THISDIR}/coreldraw(pal).pal")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# PSPPAL
def test_psppal():
	pal = colourswatch.io.openColourSwatch(f"{THISDIR}/paintshoppro.pal")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/paintshoppro(pal).gpl", pal)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/paintshoppro(pal).skp", pal)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/paintshoppro(pal).pal", pal)
	source = Path(f"{THISDIR}/paintshoppro.pal")
	dest = Path(f"{THISDIR}/paintshoppro(pal).pal")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# HPL
def test_hpl():
	hpl = colourswatch.io.openColourSwatch(f"{THISDIR}/example.hpl")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/example(hpl).gpl", hpl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/example(hpl).skp", hpl)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/example(hpl).hpl", hpl)
	source = Path(f"{THISDIR}/example.hpl")
	dest = Path(f"{THISDIR}/example(hpl).hpl")
	assert source.read_text(encoding="utf-8") == dest.read_text(encoding="utf-8")


# TOML
def test_toml():
	toml = colourswatch.io.openColourSwatch(f"{THISDIR}/base24.toml")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/base24(toml).gpl", toml)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/base24(toml).toml", toml)
	with Path(f"{THISDIR}/base24.toml") as toml:
		source = tloads(toml.read_text(encoding="utf-8"))
	with Path(f"{THISDIR}/base24(toml).toml") as toml:
		dest = tloads(toml.read_text(encoding="utf-8"))
	assert source == dest


# JSON
def test_json():
	json = colourswatch.io.openColourSwatch(f"{THISDIR}/base24.json")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/base24(json).gpl", json)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/base24(json).json", json)
	with Path(f"{THISDIR}/base24.json") as json:
		source = loads(json.read_text(encoding="utf-8"))
	with Path(f"{THISDIR}/base24(json).json") as json:
		dest = loads(json.read_text(encoding="utf-8"))
	assert source == dest


# PNG
def test_png():
	png = colourswatch.io.openColourSwatch(f"{THISDIR}/colours.png")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/colours(png).gpl", png)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/colours(png).png", png)
	compare = colourswatch.io.openColourSwatch(f"{THISDIR}/colours(png).png")
	assert len(png.colours) == len(compare.colours)


# JPG
def test_jpg():
	jpg = colourswatch.io.openColourSwatch(f"{THISDIR}/colours.jpg")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/colours(jpg).gpl", jpg)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/colours(jpg).jpg", jpg)
	compare = colourswatch.io.openColourSwatch(f"{THISDIR}/colours(jpg).jpg")
	assert len(jpg.colours) == len(compare.colours)


# WEBP
def test_webp():
	webp = colourswatch.io.openColourSwatch(f"{THISDIR}/colours.webp")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/colours(webp).gpl", webp)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/colours(webp).webp", webp)
	compare = colourswatch.io.openColourSwatch(f"{THISDIR}/colours(webp).webp")
	assert len(webp.colours) == len(compare.colours)


# ASE
def test_ase():
	# ase can hold multiple swatches so openColourSwatch will return a list of these
	ase = colourswatch.io.openColourSwatch(f"{THISDIR}/solarized.ase")[0]
	colourswatch.io.saveColourSwatch(f"{THISDIR}/solarized(ase).gpl", ase)


# SVG
def test_svg():
	svg = colourswatch.io.openColourSwatch(f"{THISDIR}/ai.svg")
	colourswatch.io.saveColourSwatch(f"{THISDIR}/ai(svg).gpl", svg)
	colourswatch.io.saveColourSwatch(f"{THISDIR}/ai(svg).svg", svg)


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
