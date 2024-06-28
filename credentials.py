import os

class Credentials:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}'
        }
        self.endpoint = 'v1/me/top/tracks?time_range=long_term&limit=5'
        self.SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
        self.SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.scope = "user-library-read"

    def get_headers(self):
        return self.headers

    def get_endpoint(self):
        return self.endpoint

    def get_client_credentials(self):
        return {
            'client_id': self.SPOTIFY_CLIENT_ID,
            'client_secret': self.SPOTIFY_CLIENT_SECRET
        }