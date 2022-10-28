#!/bin/bash

ufo=../../../source/Narnoor-Regular.ufo
glyphnames=$HOME/script/smithplus/etc/glyph_names/glyph_names.csv
shimenkan=$HOME/script/plrd/fonts/shimenkan-local/instances/Shimenkan-Regular.ufo
sourcesans=$HOME/script/latn/fonts/source/sans/Roman/Instances/Regular/font.ufo
andika=$HOME/script/latn/fonts/andika/source/Andika-Regular.ufo

do_import()
{
    latin=$1
    import=$2
    tag=$(basename $latin .ufo)-$import
    glyphs=${tag}.csv
    scale=""
    if [ $latin = $andika ]
    then
        scale="--scale .439453" # 0.9 * 1000 / 2048
    fi
    psfgetglyphnames -i import_${import}.txt -a $glyphnames $latin $glyphs
    psfcopyglyphs --rename rename --unicode usv $scale -s $latin -i $glyphs -l ${tag}_import.log $ufo
    # git add $ufo
    # git commit -m $tag
}

psfrenameglyphs -i rename.txt $ufo
psfdeleteglyphs -i delete.txt $ufo
# git add $ufo
# git commit -m "latin"
do_import $shimenkan main
do_import $sourcesans numeric
do_import $andika main
psfsetunicodes -i encode.txt $ufo
$HOME/script/tools/indic_punct.py $ufo
psfbuildcomp -c -i ../../../source/composites.txt $ufo
