import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import Credentials


token = ''

spotify_api = Credentials(token)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='SPOTIPY_CLIENT_ID', client_secret='SPOTIPY_CLIENT_SECRET'))

url = f'https://api.spotify.com/{spotify_api.get_endpoint()}'
r = requests.get(headers=spotify_api.get_headers(), url=url)

def getTracks():
    i = 0

    for item in r.json()["items"]:
        musica = r.json()["items"][i]["name"]
        artista = r.json()["items"][i]["artists"][0]["name"]
        result = print(artista, " - ", musica)
        i += 1

    return result

getTracks()

