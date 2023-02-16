from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import yaml

class SpotifyData:
    def __init__(self):
        with open('config.yml', "r") as f:
            client = yaml.safe_load(f)
        self.client_id = client['client_id']
        self.client_secret= client['client_secret']
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id = self.client_id,
            client_secret = self.client_secret
        ))
    def search_playlist(self,q='rock'):
        results = self.sp.search(q=q, type='playlist')
        return results

