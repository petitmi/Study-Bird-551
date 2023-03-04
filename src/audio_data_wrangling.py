# from spotify_api import SpotifyData
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify
import yaml
import pandas as pd

def login():
    with open('config.yml', "r") as f:
        client = yaml.safe_load(f)
    client_id = client['client_id']
    client_secret= client['client_secret']
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id = client_id,
        client_secret = client_secret
    ))
    return sp
def sc(sp, type='track',q='the%201975'):
    req_search = sp.search(q=q,type=type)
    track_id = req_search['tracks']['items'][0]['id']
    print(q,track_id)
    return track_id

# login to access spotify API
sp=login()

# billboard hot songs list
hits = pd.read_csv('../data/raw/billboard_hot_100_2012to2022.csv')

# Add track_id column
q_df = hits[['Title','Artist']].apply(lambda x: f"{x['Title']} {x['Artist']}", axis=1)
_track_id1 = q_df[:500].apply(lambda x: sc(sp,q=x))
_track_id2 = q_df[500:1000].apply(lambda x: sc(sp,q=x))
_track_id3 = q_df[1000:].apply(lambda x: sc(sp,q=x))
hits['track_id'] = pd.concat([_track_id1, _track_id2,_track_id3], ignore_index=True)

# add popularity column
import time
def get_popularity(x):
    result = sp.track(x)
    # track['genres'] = result['album']['genres']
    # track['label'] = result['album']['label']
    time.sleep(0.5)
    return result['popularity']

hits['popularity'] = hits['track_id'].apply(lambda x: get_popularity(x))

# add all audio features column
audio_dct_keys = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
audio_dct={}
for audio_dct_key in audio_dct_keys:
    audio_dct[audio_dct_key] = []

def get_audioFeatures(track_ids):
    for idc, vl in enumerate(track_ids):
        result = sp.audio_features(track_ids[idc])
        for k,v in result[0].items():
            audio_dct[k].append(v)
    return audio_dct
get_audioFeatures(hits[:400]['track_id'].values)
get_audioFeatures(hits[400:900]['track_id'].values)
get_audioFeatures(hits[900:]['track_id'].values)

hits = pd.concat([hits,pd.DataFrame.from_dict(audio_dct)],axis=1)

hits.to_csv('../data/processed/audio_data_processed.csv')