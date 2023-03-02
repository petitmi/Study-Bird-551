from spotify_api import SpotifyData
sp = SpotifyData()
results = sp.search(q='David Bowie', type='track')
results