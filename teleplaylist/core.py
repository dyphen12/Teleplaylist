import win32com.client

# create a reference to the iTunes application
itunes = win32com.client.Dispatch("iTunes.Application")

# create a new playlist
new_playlist = itunes.CreatePlaylist("My Playlist")

# add some tracks to the playlist
track1 = itunes.LibraryPlaylist.Tracks.ItemByName("Track Name 1")
new_playlist.Tracks.AddTrack(track1)

track2 = itunes.LibraryPlaylist.Tracks.ItemByName("Track Name 2")
new_playlist.Tracks.AddTrack(track2)

# save the new playlist
new_playlist = None # set the reference to None to release it
