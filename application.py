from flask import Flask, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Flask app
app = Flask(__name__)

# Set up Spotify authentication

client_id = '55343857070f4bf8ac2a86ef80fd7996'
client_secret = 'b1487b1903274ce4b95e0019aa70c593'
redirect_uri = 'http://localhost:5000/callback'
scope = 'user-library-read'
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

# Set up index route
@app.route('/')
def index():
    # Redirect to Spotify authorization URL
    auth_url = sp_oauth.get_authorize_url()
    return f'<a href="{auth_url}">Authorize with Spotify</a>'

# Set up callback route
@app.route('/callback')
def callback():
    # Get authorization code from query parameters
    code = request.args.get('code')

    # Exchange authorization code for access token
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']

    # Use access token to get user's liked songs
    sp = spotipy.Spotify(auth=access_token)
    results = sp.current_user_saved_tracks()
    liked_songs = results['items']

    # Get the track URIs for the liked songs
    track_uris = [song['track']['uri'] for song in liked_songs]

    # Get the full track information for the liked songs
    tracks = sp.tracks(track_uris)['tracks']

    # Print the names of the liked songs
    output = '<h1>Liked Songs</h1>'
    for track in tracks:
        output += f'<p>{track["name"]}</p>'
    return output

# Run the app
if __name__ == '__main__':
    app.run()
