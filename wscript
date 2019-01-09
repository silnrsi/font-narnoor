APPNAME = 'GunjalaGondi'
VERSION = 0.6
TESTDIR='tests'

font(target = 'GunjalaGondi.ttf',
	source = 'source/GunjalaGondi.sfd',
	graphite = gdl('GunjalaGondi.gdl', master='source/master.gdl', make_params="-l last -p 1"),
	ap = 'source/GunjalaGondi.xml',
	opentype = internal(),
	woff = woff(),
	fret = fret(params = '-r -s A4'),
	script = 'dflt')
