#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
for glyph in font:
    if glyph.unicode != 0x25CC:
        continue
    bounds = glyph.bounds
    if bounds is None:
        continue
    (xmin, ymin, xmax, ymax) = bounds
    xcenter = (xmin + xmax) / 2
    glyph.appendAnchor('M', (xmax, ymax))
    glyph.appendAnchor('UR', (xmax, ymin))

# Save UFO
font.changed()
font.save()
font.close()
