# everything achivable with playlist class ;)
'''
>>> liste = playlist.static(type='artist', artist_pick='song_hotttnesss-desc', 
				artist="Foo Fighters", song_min_hotttnesss=0.7, results=5)
>>> for result in artist.Artist("Foo Fighters").similar:
...     liste=liste+playlist.static(type='artist', artist_pick='song_hotttnesss-desc', 
				artist=result, song_min_hotttnesss=0.7, results=5)
... 
>>> liste
[<song - All My Life>, <song - Learn To Fly>, <song - These Days>, 
	<song - Best Of You>, <song - Times Like These>, <song - About A Girl>, 
	<song - Come As You Are>, <song - All Apologies>, <song - Rape Me>, 
	<song - In Bloom>, <song - Like A Stone>, <song - Alive>, <song - Black>, 
	<song - Jeremy>, <song - Even Flow>, <song - Today>, <song - 1979>, 
	<song - Tonight, Tonight>, <song - Bullet With Butterfly Wings>, 
	<song - Rooster>, <song - Would?>, <song - Man In The Box>, 
	<song - Black Hole Sun>, <song - Been Away Too Long>]


"type=artist-radio" even makes this small logical snippet waste - ridiculous :)
>>> liste = playlist.static(type='artist-radio', artist_pick='song_hotttnesss-desc', 
				artist="Foo Fighters", song_min_hotttnesss=0.6, results=10)
>>> liste
[<song - All My Life>, <song - Show Me How To Live>, 
	<song - Come As You Are>, <song - You're Gonna Go Far, Kid>, 
	<song - Even Flow>, <song - Never Let You Go>, <song - Shine>, 
	<song - You Know My Name>, <song - Far Behind>, <song - Hunger Strike>]
'''

import sys
from pyechonest import config, song, artist

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
