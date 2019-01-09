APPNAME = 'GunjalaGondi'
VERSION = 0.6
TESTDIR='test-suite'

font(target = 'GunjalaGondi.ttf',
	source = 'font-source/GunjalaGondi.sfd',
	#source = process('font-source/GunjalaGondi.sfd', cmd('../tools/addchars ../font-source/CharisSIL-R.ttf ${DEP} ${TGT}')),
	graphite = gdl('GunjalaGondi.gdl', master='font-source/GunjalaGondi.gdl', make_params="-l last -p 1"),
	ap = 'font-source/GunjalaGondi.xml',
	opentype = internal(),
	woff = woff(),
	fret = fret(params = '-r -s A4'),
	script = 'dflt')

# kbd(source="../../keyboards/gunjala/koytura-gunjala.kmn",
#	fontdir="kbdfonts",
#	font="GunjalaGondi.ttf",
#	fontname="GunjalaGondi",
#	mskbd=mskbd())

