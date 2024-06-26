import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

token = ''

headers = {
    'Authorization': f'Bearer {token}'
}

endpoint = 'v1/me/top/tracks?time_range=long_term&limit=5'

SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='SPOTIPY_CLIENT_ID', client_secret='SPOTIPY_CLIENT_SECRET'))

url = f'https://api.spotify.com/{endpoint}'
r = requests.get(headers=headers, url=url)

def getTracks():
    i = 0
    rank = 1

    for item in r.json()["items"]:
        musica = r.json()["items"][i]["name"]
        artista = r.json()["items"][i]["artists"][0]["name"]
        result = print(rank, ". ", artista, " - ", musica)
        i += 1
        rank += 1

    return result

getTracks()

