from models import db, Playlist, Song, PlaylistSong
from app import app

db.drop_all()
db.create_all()

Playlist.query.delete()
Song.query.delete()
PlaylistSong.query.delete()

playlist1 = Playlist(name='Rock Music',
                     description = 'a playlist of rock music')

playlist2 = Playlist(name='EDM Music',
                     description = 'a playlist of EDM music')

song1 = Song(title='We Will Rock You',
             artist='Queen')

song2 = Song(title='Whole Lotta Love',
             artist='Led Zeppelin')

song3 = Song(title='Lean On',
             artist='DJ Snake')

song4 = Song(title='Titanium',
             artist='David Guetta')

playlist_song1 = PlaylistSong(playlist_id=1,
                              song_id = 1)

playlist_song2 = PlaylistSong(playlist_id=1,
                              song_id = 2)

playlist_song3 = PlaylistSong(playlist_id=2,
                              song_id = 3)

playlist_song4 = PlaylistSong(playlist_id=2,
                              song_id = 4)

db.session.add(playlist1)
db.session.add(playlist2)
db.session.add(song1)
db.session.add(song2)
db.session.add(song3)
db.session.add(song4)
db.session.add(playlist_song1)
db.session.add(playlist_song2)
db.session.add(playlist_song3)
db.session.add(playlist_song4)

db.session.commit()
