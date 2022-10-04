#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
cgj = 0x034F
vs = range(0xFE00, 0xFE0F+1)
mn = [cgj] + list(vs)

for glyph in font:
    if glyph.unicode in mn:
        glyph.appendAnchor('_none', (0, 0))

# Save UFO
font.changed()
font.save()
font.close()
