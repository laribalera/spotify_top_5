import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import Credentials

app = Flask(__name__)


token = ''

spotify_api = Credentials(token)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='SPOTIPY_CLIENT_ID', client_secret='SPOTIPY_CLIENT_SECRET'))

@app.route('/')
def index():

    url = f'https://api.spotify.com/{spotify_api.get_endpoint()}'
    r = requests.get(headers=spotify_api.get_headers(), url=url)


    def getTracks():
        tracks = []
        for item in r.json()["items"]:
            musica = item["name"]
            artista = item["artists"][0]["name"]
            tracks.append({"artista": artista, "musica": musica})
        return tracks
    
    tracks = getTracks()
    return render_template('index.html', tracks=tracks)

if __name__ == '__main__':
    app.run(debug=True)