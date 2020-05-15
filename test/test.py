"""Test module """

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
from json import loads
from comparexml import compareFiles
from yaml import safe_load
from tomlkit import loads as tloads
import colourswatch.io

#pylint: disable=missing-function-docstring

# GPL
def test_gpl():
	gpl = colourswatch.io.openColourSwatch(THISDIR + "/plasma.gpl")
	colourswatch.io.saveColourSwatch(THISDIR + "/plasma(gpl).gpl", gpl)
	source = open(THISDIR + "/plasma.gpl")
	dest = open(THISDIR + "/plasma(gpl).gpl")
	assert source.read() == dest.read()
	source.close()
	dest.close()

# YAML
def test_yaml():
	yaml = colourswatch.io.openColourSwatch(THISDIR + "/base24.yaml")
	colourswatch.io.saveColourSwatch(THISDIR + "/base24(yaml).gpl", yaml)
	colourswatch.io.saveColourSwatch(THISDIR + "/base24(yaml).yaml", yaml)
	with open(THISDIR + "/base24.yaml") as yaml:
		source = safe_load(yaml.read())
	with open(THISDIR + "/base24(yaml).yaml") as yaml:
		dest = safe_load(yaml.read())
	assert source == dest

# COLORS
def test_colors():
	colors = colourswatch.io.openColourSwatch(THISDIR + "/40.colors")
	colourswatch.io.saveColourSwatch(THISDIR + "/40(colors).gpl", colors)
	colourswatch.io.saveColourSwatch(THISDIR + "/40(colors).colors", colors)
	source = open(THISDIR + "/40.colors")
	dest = open(THISDIR + "/40(colors).colors")
	assert source.read() == dest.read()
	source.close()
	dest.close()

# SPL
def test_spl():
	spl = colourswatch.io.openColourSwatch(THISDIR + "/mini.spl")
	colourswatch.io.saveColourSwatch(THISDIR + "/mini(spl).gpl", spl)
	colourswatch.io.saveColourSwatch(THISDIR + "/mini(spl).spl", spl)
	source = open(THISDIR + "/mini.spl")
	dest = open(THISDIR + "/mini(spl).spl")
	assert source.read() == dest.read()
	source.close()
	dest.close()

# SKP
def test_skp():
	skp = colourswatch.io.openColourSwatch(THISDIR + "/example.skp")
	colourswatch.io.saveColourSwatch(THISDIR + "/example(skp).gpl", skp)
	colourswatch.io.saveColourSwatch(THISDIR + "/example(skp).skp", skp)
	assert compareFiles(THISDIR + "/example.skp", THISDIR + "/example(skp).skp")

# SOC
def test_soc():
	soc = colourswatch.io.openColourSwatch(THISDIR + "/series.soc")
	colourswatch.io.saveColourSwatch(THISDIR + "/series(soc).gpl", soc)
	colourswatch.io.saveColourSwatch(THISDIR + "/series(soc).skp", soc)
	colourswatch.io.saveColourSwatch(THISDIR + "/series(soc).soc", soc)
	assert compareFiles(THISDIR + "/series.soc", THISDIR + "/series(soc).soc")

# TXT
def test_txt():
	txt = colourswatch.io.openColourSwatch(THISDIR + "/defaultpdn.txt")
	colourswatch.io.saveColourSwatch(THISDIR + "/defaultpdn(txt).gpl", txt)
	colourswatch.io.saveColourSwatch(THISDIR + "/defaultpdn(txt).skp", txt)
	colourswatch.io.saveColourSwatch(THISDIR + "/defaultpdn(txt).txt", txt)
	source = open(THISDIR + "/defaultpdn.txt")
	dest = open(THISDIR + "/defaultpdn(txt).txt")
	assert source.read() == dest.read()
	source.close()
	dest.close()

# ACBL
def test_acbl():
	acbl = colourswatch.io.openColourSwatch(THISDIR + "/colours.acbl")
	colourswatch.io.saveColourSwatch(THISDIR + "/colours(acbl).gpl", acbl)
	colourswatch.io.saveColourSwatch(THISDIR + "/colours(acbl).skp", acbl)
	colourswatch.io.saveColourSwatch(THISDIR + "/colours(acbl).txt", acbl)

# XML
def test_xml():
	xml = colourswatch.io.openColourSwatch(THISDIR + "/scribus.xml")
	colourswatch.io.saveColourSwatch(THISDIR + "/scribus(xml).gpl", xml)
	colourswatch.io.saveColourSwatch(THISDIR + "/scribus(xml).skp", xml)
	colourswatch.io.saveColourSwatch(THISDIR + "/scribus(xml).xml", xml)
	assert compareFiles(THISDIR + "/scribus_desired.xml", THISDIR + "/scribus(xml).xml")

# CDPAl
def test_cdpal():
	pal = colourswatch.io.openColourSwatch(THISDIR + "/coreldraw.pal")
	colourswatch.io.saveColourSwatch(THISDIR + "/coreldraw(pal).gpl", pal)
	colourswatch.io.saveColourSwatch(THISDIR + "/coreldraw(pal).skp", pal)
	colourswatch.io.saveColourSwatch(THISDIR + "/coreldraw(pal).pal", pal)
	source = open(THISDIR + "/coreldraw.pal")
	dest = open(THISDIR + "/coreldraw(pal).pal")
	assert source.read() == dest.read()
	source.close()
	dest.close()

# PSPPAL
def test_psppal():
	pal = colourswatch.io.openColourSwatch(THISDIR + "/paintshoppro.pal")
	colourswatch.io.saveColourSwatch(THISDIR + "/paintshoppro(pal).gpl", pal)
	colourswatch.io.saveColourSwatch(THISDIR + "/paintshoppro(pal).skp", pal)
	colourswatch.io.saveColourSwatch(THISDIR + "/paintshoppro(pal).pal", pal)
	source = open(THISDIR + "/paintshoppro.pal")
	dest = open(THISDIR + "/paintshoppro(pal).pal")
	assert source.read() == dest.read()
	source.close()
	dest.close()

# HPL
def test_hpl():
	hpl = colourswatch.io.openColourSwatch(THISDIR + "/example.hpl")
	colourswatch.io.saveColourSwatch(THISDIR + "/example(hpl).gpl", hpl)
	colourswatch.io.saveColourSwatch(THISDIR + "/example(hpl).skp", hpl)
	colourswatch.io.saveColourSwatch(THISDIR + "/example(hpl).hpl", hpl)
	source = open(THISDIR + "/example.hpl")
	dest = open(THISDIR + "/example(hpl).hpl")
	assert source.read() == dest.read()
	source.close()
	dest.close()

# TOML
def test_toml():
	toml = colourswatch.io.openColourSwatch(THISDIR + "/base24.toml")
	colourswatch.io.saveColourSwatch(THISDIR + "/base24(toml).gpl", toml)
	colourswatch.io.saveColourSwatch(THISDIR + "/base24(toml).toml", toml)
	with open(THISDIR + "/base24.toml") as toml:
		source = tloads(toml.read())
	with open(THISDIR + "/base24(toml).toml") as toml:
		dest = tloads(toml.read())
	assert source == dest

# JSON
def test_json():
	json = colourswatch.io.openColourSwatch(THISDIR + "/base24.json")
	colourswatch.io.saveColourSwatch(THISDIR + "/base24(json).gpl", json)
	colourswatch.io.saveColourSwatch(THISDIR + "/base24(json).json", json)
	with open(THISDIR + "/base24.json") as json:
		source = loads(json.read())
	with open(THISDIR + "/base24(json).json") as json:
		dest = loads(json.read())
	assert source == dest

# PNG
def test_png():
	png = colourswatch.io.openColourSwatch(THISDIR + "/colours.png")
	colourswatch.io.saveColourSwatch(THISDIR + "/colours(png).gpl", png)
	colourswatch.io.saveColourSwatch(THISDIR + "/colours(png).png", png)
	compare = colourswatch.io.openColourSwatch(THISDIR + "/colours(png).png")
	assert len(png.colours) == len(compare.colours)

# JPG
def test_jpg():
	jpg = colourswatch.io.openColourSwatch(THISDIR + "/colours.jpg")
	colourswatch.io.saveColourSwatch(THISDIR + "/colours(jpg).gpl", jpg)
	colourswatch.io.saveColourSwatch(THISDIR + "/colours(jpg).jpg", jpg)
	compare = colourswatch.io.openColourSwatch(THISDIR + "/colours(jpg).jpg")
	assert len(jpg.colours) == len(compare.colours)

# WEBP
def test_webp():
	webp = colourswatch.io.openColourSwatch(THISDIR + "/colours.webp")
	colourswatch.io.saveColourSwatch(THISDIR + "/colours(webp).gpl", webp)
	colourswatch.io.saveColourSwatch(THISDIR + "/colours(webp).webp", webp)
	compare = colourswatch.io.openColourSwatch(THISDIR + "/colours(webp).webp")
	assert len(webp.colours) == len(compare.colours)

# ASE
def test_ase():
	# ase can hold multiple swatches so openColourSwatch will return a list of these
	ase = colourswatch.io.openColourSwatch(THISDIR + "/solarized.ase")[0]
	colourswatch.io.saveColourSwatch(THISDIR + "/solarized(ase).gpl", ase)

# SVG
def test_svg():
	svg = colourswatch.io.openColourSwatch(THISDIR + "/ai.svg")
	colourswatch.io.saveColourSwatch(THISDIR + "/ai(svg).gpl", svg)
	colourswatch.io.saveColourSwatch(THISDIR + "/ai(svg).svg", svg)

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
