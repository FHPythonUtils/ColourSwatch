"""Test module """

import sys
import os
from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, os.path.dirname(THISDIR))
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
	'''
	source = open(THISDIR + "/base24.yaml")
	dest = open(THISDIR + "/base24(yaml).yaml")
	assert source.read() == dest.read()
	source.close()
	dest.close()
	'''

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
	'''
	source = open(THISDIR + "/example.skp")
	dest = open(THISDIR + "/example(skp).skp")
	assert source.read() == dest.read()
	source.close()
	dest.close()
	'''

# SOC
def test_soc():
	soc = colourswatch.io.openColourSwatch(THISDIR + "/series.soc")
	colourswatch.io.saveColourSwatch(THISDIR + "/series(soc).gpl", soc)
	colourswatch.io.saveColourSwatch(THISDIR + "/series(soc).skp", soc)
	colourswatch.io.saveColourSwatch(THISDIR + "/series(soc).soc", soc)
	'''
	source = open(THISDIR + "/series.soc")
	dest = open(THISDIR + "/series(soc).soc")
	assert source.read() == dest.read()
	source.close()
	dest.close()
	'''

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
	'''
	source = open(THISDIR + "/scribus.xml")
	dest = open(THISDIR + "/scribus(xml).xml")
	assert source.read() == dest.read()
	source.close()
	dest.close()
	'''


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
