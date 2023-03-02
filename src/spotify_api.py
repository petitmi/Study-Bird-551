from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify
import yaml
import pandas as pd

class SpotifyData(Spotify):
    def __init__(self):
        Spotify.__init__(self)
        with open('config.yml', "r") as f:
            client = yaml.safe_load(f)
        self.client_id = client['client_id']
        self.client_secret= client['client_secret']
        self.sp = Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id = self.client_id,
            client_secret = self.client_secret
        ))
    def search(self, type='track,artist,album',q='the%201975'):
            req_search = self.sp.search(q=q,type=type)
            artists, albums, tracks =[], [], []
            for item in req_search['artists']['items']:
                artist={}
                artist['artist'] = item['name']
                artist['id'] = item['id']
                artist['followers'] = item['followers']['total']
                artist['genres'] = item['genres']
                artist['explore'] = f"""<a href="/artist/{artist['artist']}"> gooo </a>"""

                # artist['type'] = item['type']
                artists.append(artist)
            for item in req_search['albums']['items']:
                album = {}
                album['album'] = item['name']
                album['id'] = item['id']
                album['release_date'] = item['release_date']
                album['total_tracks'] = item['total_tracks']
                album['artist'] = item['artists'][0]['name']
                album['artist_id'] = item['artists'][0]['id']
                album['explore'] = f"""<a href="/album/{album['album']}"> gooo </a>"""
                # album['type'] = item['type']
                albums.append(album)
            for item in req_search['tracks']['items']:
                track = {}
                track['track'] = item['name']
                track['release_date'] = item['album']['release_date']
                track['popularity'] = item['popularity']
                track['id'] = item['id']
                track['artist'] = item['artists'][0]['name']
                track['artist_id'] = item['artists'][0]['id']
                track['album'] = item['album']['name']
                track['album_id'] = item['album']['id']
                track['type'] = item['type']
                track['explore'] = f"""<a href="/track/{track['artist']}_{track['track']}"> gooo </a>"""
            
                tracks.append(track)
            artists = pd.DataFrame(artists)
            albums = pd.DataFrame(albums)
            tracks = pd.DataFrame(tracks)
            return artists, albums, tracks



