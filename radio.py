import sys
from pyechonest import config, song, artist
config.ECHO_NEST_API_KEY=""

art = str( raw_input("Interpret: ") )
tit = str( raw_input("Titel: ") )

s = song.search( artist=art, title=tit )
try:
	a = artist.Artist( s[0].artist_name )
except:
	print "Artist not found"
	sys.exit(0)

try:
	hotness = s[0].song_hotttnesss
except:
	# Song not found or specified - default 0.4
	hotness = 0.4

#hotlist=[]
songlist=[]
artistlist=[]
mixed=[]

def returnSongs(a):
	hotsongs = []
	for i in a.similar:
		if i.songs[0].song_hotttnesss >= hotness:
			#hotsongs.append( {'%s': '%s'} ) % ( str( i.songs[0].artist_name ), str( i.songs[0].title ) )
			songlist.append( str( i.songs[0].title ) )
			artistlist.append( str(i.songs[0].artist_name) )
			mixed.append( "%s - %s" % ( str( i.songs[0].artist_name ), str( i.songs[0].title ) ) )

def firstIter(a):
	returnSongs(a)

def secondIter(artistlist):
	for i in artistlist:
		ar = artist.search(name=a)
		ar = ar[0]
		returnSongs(ar)
firstIter(a)
secondIter(artistlist)

for i in mixed:
	print i
