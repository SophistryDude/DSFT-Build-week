import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests


cid = '994a02e31176479b90f256314374ed16'
secret = '057916dd2e9d48c096b174fae78f1c4e'
AUTH_URL = 'https://accounts.spotify.com/api/token'


# POST

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': cid,
    'client_secret': secret,
})


# convert the response to JSON

auth_response_data = auth_response.json()
# save the access token
access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id = '6y0igZArWVi6Iz0rj35c1Y'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

r = r.json()
print(r)