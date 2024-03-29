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

latn = (0x0060, 0x00A8, 0x00AF, 0x00B4, 0x00B8, 0x02C6, 0x02C7, 0x02D8, 0x02DB, 0x02D9, 0x02DA, 0x02DC, 0x02DD)

for glyph in font:
    if glyph.unicode in latn:
        for anchor in glyph.anchors:
            if anchor.name.startswith('_'):
                glyph.removeAnchor(anchor)
    # if glyph.unicode == 0x11D97: # virama
    # if glyph.unicode in vs:
    #     glyph.appendAnchor('_none', (0, 0))
    # if glyph.unicode == cgj:
    #     glyph.appendAnchor('_aboveLC', (0, 0))

# Save UFO
font.changed()
font.save()
font.close()
