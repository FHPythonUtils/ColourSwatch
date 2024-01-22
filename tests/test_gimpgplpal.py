"""Test module """

from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from colourswatch.gimpgplpal import GimpGplPalette


def test_eq() -> None:
	gpl = GimpGplPalette(f"{THISDIR}/data/plasma.gpl")
	gpl2 = GimpGplPalette(f"{THISDIR}/data/plasma.gpl")
	gpl3 = GimpGplPalette(f"{THISDIR}/data/plasma.gpl")
	gpl3.name = "None"
	gpl4 = GimpGplPalette(f"{THISDIR}/data/plasma.gpl")
	gpl4.columns = 0
	gpl5 = GimpGplPalette(f"{THISDIR}/data/plasma.gpl")
	gpl5.colors = []
	assert gpl == gpl2
	assert gpl != gpl3
	assert gpl != gpl4
	assert gpl != gpl5



def test_gpl() -> None:
	gpl = GimpGplPalette(f"{THISDIR}/data/plasma.gpl")
	assert gpl.name == "Plasma"
	assert gpl.columns == 16
	assert (112, 112, 112) in gpl.colors
	assert "grey44" in gpl.colorNames


def test_str() -> None:
	gpl = GimpGplPalette(f"{THISDIR}/data/plasma.gpl")
	gpl_str_expected = Path(f"{THISDIR}/data/plasma_gpl_str_expected.txt").read_text("utf-8").strip()
	assert str(gpl) == gpl_str_expected
	gpl.fileName = None
	assert str(gpl) == "\n".join(gpl_str_expected.splitlines()[1:])
