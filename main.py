from Playlist import Playlist
from Movie import Movie
from Series import Series

avengers = Movie('the avengers ultimato', 2019, 300)
avengers.liked()
avengers.liked()
avengers.liked()

supernatural = Series('supernatural', 2005, 15)
supernatural.liked()
supernatural.liked()

got = Series('game of thrones', 2011, 7)
got.liked()
got.liked()
got.liked()
got.liked()

programs = [avengers, supernatural, got]

playlist = Playlist('movies and series', programs)

for item in playlist:
    print(item)
