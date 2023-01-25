#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO

# Top of headline
height = 645

# Fix anusvara
anusvara = font['anusvara']
(xmin, ymin, xmax, ymax) = anusvara.bounds
xcenter = (xmin + xmax) / 2
anusvara.appendAnchor('_A', (xcenter, height))

rsb = anusvara.width - xcenter

# Font wide changes
for glyph in font:
    # Remove un-needed anchors
    for anchor in glyph.anchors:
        if anchor.name in ('_U', 'U', '_L', 'L', '_UR', 'UR'):
            glyph.removeAnchor(anchor)

    # Position anusvara
    offset = 0
    if glyph.name.endswith('eematra') or glyph.name.endswith('aimatra') or glyph.name.endswith('_imatra') or glyph.name in ('imatra', 'ivowel', 'eevowel', 'aivowel'):
        offset = 100
    if glyph.name.endswith('matra') or glyph.unicode and glyph.unicode >= 0x11D60 and glyph.unicode <= 0x11D89:
        glyph.appendAnchor('A', (glyph.width - rsb + offset, height))


# Save UFO
font.changed()
font.save()
font.close()
