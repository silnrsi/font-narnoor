#!/usr/bin/python2
# encoding: utf-8
# this is a smith configuration file - http://scripts.sil.org/smith

# set some default output folders (most are already set by default)
DOCDIR = ["documentation", "web"]
STANDARDS = 'tests/reference'

# set the font name and description
APPNAME = 'Narnoor'
FAMILY = APPNAME
DESC_SHORT = "Font for the Gunjala Gondi script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')

# Set up the FTML tests
ftmlTest('tools/ftml-padauk.xsl', fonts=['../test/reference/Narnoor-Regular.ttf'], addfontindex=1, fontmode='collect')

# set the build and test parameters
TESTSTRING = u'\U00011D6C'

OMITAPS = '--omitaps "_U,U"'
generated = 'generated/'

# set up the build parameters from the designspace file(s)
for dspace in ('Roman',):
    designspace('source/' + FAMILY + dspace + '.designspace',
                target = process('${DS:FILENAME_BASE}.ttf',
                    cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo'])
                ),
                opentype = fea(generated + '${DS:FILENAME_BASE}.fea',
                    mapfile = generated + '${DS:FILENAME_BASE}.map',
                    master = 'source/master.feax',
                    make_params = OMITAPS + ' -L last',
                    params = '',
                    ),
                graphite = gdl(generated + '${DS:FILENAME_BASE}.gdl',
                             master='source/master.gdl',
                             make_params=OMITAPS + ' -l last -p 1',
                             params='-e gdlerr-${DS:FILENAME_BASE}.txt',
                             depends=[]),
                script = ['gong'],
                ap = 'generated/' + '${DS:FILENAME_BASE}.xml',
                # classes = 'source/' + 'classes.xml',
                fret = fret(params='-r -oi'),
                woff = woff('web/${DS:FILENAME_BASE}.woff', params='-v ' + VERSION + ' -m ../source/${DS:FAMILYNAME}-WOFF-metadata.xml')
    )
