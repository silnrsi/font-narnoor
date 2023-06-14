#!/bin/bash

ufoR=../../../source/masters/Narnoor-Regular.ufo
ufo=../../../source/masters/Narnoor-ExtraBold.ufo
glyphnames=$HOME/script/smithplus/etc/glyph_names/glyph_names.csv
shimenkanR=$HOME/script/plrd/fonts/shimenkan-local/instances/Shimenkan-Regular.ufo
shimenkan=$HOME/script/plrd/fonts/shimenkan-local/instances/ShimenkanLight-Bold.ufo
sourcesans=$HOME/script/latn/fonts/source/sans/Roman/Instances/Semibold/font.ufo # Regular/font.ufo
andika=$HOME/script/latn/fonts/andika/source/masters/Andika-Bold.ufo # Andika-Regular.ufo

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

# psfrenameglyphs -i rename.txt $ufo
psfdeleteglyphs -i delete.txt $ufo
psfdeleteglyphs -i orig_latin_punct.txt $ufo
psfdeleteglyphs -i dashes.txt $ufo
psfdeleteglyphs -i changed_latin_punct.txt $ufo
# git add $ufo
# git commit -m "latin"
do_import $shimenkan main
do_import $sourcesans numeric
do_import $andika main
cat orig_latin_punct.txt dashes.txt changed_latin_punct.txt | xargs -L 1 echo git restore $ufo/glyphs/ | sed 's/\/\ /\//g' | awk '{print $0 ".glif"}' | bash
psfsetunicodes -i encode.txt $ufo
# $HOME/script/tools/indic_punct.py $ufo
$HOME/script/tools/anchor-keep.py only anchors.json $ufo
$HOME/script/tools/anchor-keep.py only anchors.json $ufoR
../gdef.py $ufo
../dotted_circle.py $ufo
cp $shimenkanR/glyphs/brevecmb.glif $ufoR/glyphs
# psfbuildcomp -c -i ../../../source/composites.txt $ufo
