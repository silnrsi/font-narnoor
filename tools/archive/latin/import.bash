#!/bin/bash

glyphnames=$HOME/script/smithplus/etc/glyph_names/glyph_names.csv
ar=$PWD/tools/archive/latin
import=$PWD-local/latin/Shimenkan
scale="--scale .9667"

pushd source/masters
for weight in Regular ExtraBold
do
    ufo=Narnoor-${weight}.ufo
    latin=${import}-${weight}.ufo
    glyphs=$ar/import-${weight}.csv

    # prepare
    psfdeleteglyphs -i $ar/delete.txt $ufo
    psfdeleteglyphs -i $ar/orig_latin_punct.txt $ufo
    psfdeleteglyphs -i $ar/dashes.txt $ufo
    psfdeleteglyphs -i $ar/changed_latin_punct.txt $ufo

    # import
    psfgetglyphnames -i $ar/import_main.txt -a $glyphnames $latin $glyphs
    psfcopyglyphs --rename rename --unicode usv $scale -s $latin -i $glyphs -l tmp.log $ufo

    # cleanup
    cat $ar/orig_latin_punct.txt $ar/dashes.txt $ar/changed_latin_punct.txt | xargs -L 1 echo git restore $ufo/glyphs/ | sed 's/\/\ /\//g' | awk '{print $0 ".glif"}' | bash
    psfsetunicodes -i $ar/encode.txt $ufo
    $HOME/script/tools/anchor-keep.py only $ar/anchors.json $ufo
    $ar/../gdef.py $ufo
    $ar/../dotted_circle.py $ufo
    psfsetmarkcolors -i $ar/delete.txt -c g_light_gray $ufo
    psfsetmarkcolors -i $ar/import_main.txt -u -c g_light_gray $ufo
done
popd
