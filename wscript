#!/usr/bin/python3
# this is a smith configuration file

# override the default folders
DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'Narnoor'
FAMILY = APPNAME
DESC_SHORT = "Font for the Gunjala Gondi script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

omitaps = '--omitaps "_U,U"'
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
                    make_params = omitaps + ' -L last',
                    params = '',
                    ),
                graphite = gdl(generated + '${DS:FILENAME_BASE}.gdl',
                             master='source/master.gdl',
                             make_params=omitaps + ' -l last -p 1',
                             params='-e gdlerr-${DS:FILENAME_BASE}.txt',
                             depends=[]),
                classes = 'source/' + 'classes.xml',
                ap = 'generated/' + '${DS:FILENAME_BASE}.xml',
                version = VERSION,
                woff = woff('woff/${DS:FILENAME_BASE}',
                    metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml'),
                script = ['gong'],
                pdf = fret(params='-oi')
    )
