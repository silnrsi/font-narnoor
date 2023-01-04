#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
reverse = ['.notdef', 'abbreviationsign', 'figuredash', 'horizontalbar', 'inrupee']
with open('../tools/archive/latin/delete_latin_punct.txt') as latn_punct:
    for line in latn_punct:
        glyph_name = line.split('.')[0]
        reverse.append(glyph_name)

for glyph in font:
    # Reverse contour direction since the glyphs might have come
    # from a TTF font and the source should have PostScript curves
    if glyph.name in reverse:
        for contour in glyph.contours:
            contour.reverse()

# Save UFO
font.changed()
font.save()
font.close()
