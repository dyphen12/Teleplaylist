import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyPKCE

# Set up Spotify authentication
client_id = '55343857070f4bf8ac2a86ef80fd7996'
client_secret = 'b1487b1903274ce4b95e0019aa70c593'
redirect_uri = 'http://localhost:5000/callback'
scope = 'user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyPKCE(redirect_uri=redirect_uri,client_id=client_id, scope=scope))

results = sp.current_user_saved_tracks()
liked_songs = results['items']

# Get the track URIs for the liked songs
track_uris = [song['track']['uri'] for song in liked_songs]

# Get the full track information for the liked songs
tracks = sp.tracks(track_uris)['tracks']

# Print the names of the liked songs
for track in tracks:
    print(track['name'])