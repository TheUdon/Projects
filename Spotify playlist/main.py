import sys
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

billboard_url = "https://www.billboard.com/charts/hot-100/"
date = input("What year would you like to travel back to? Type the date in this format YYYY-MM-DD: ")
SPOTIPY_CLIENT_ID = "fdc755dad2da46b5af133f527681e84b"
SPOTIPY_CLIENT_SECRET = "ed27eb708ac34188a621789a7489b142"
SPOTIPY_REDIRECT_URI = "http://example.com"


scope = "playlist-modify-private playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]

response = requests.get(f"{billboard_url}{date}")
billboard = response.text
soup = BeautifulSoup(billboard, "html.parser")
song_names_span = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_names = [song.getText() for song in song_names_span]

year = date.split('-')[0]
spotify_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        spotify_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in the Spotify library. Skipped.")

playlist_name = f"{date} Billboard 100"
user_playlists = sp.user_playlists(user_id)

playlist_already_made = False
if len(user_playlists) != 0:
    for playlist in user_playlists["items"]:
        if playlist["name"] == playlist_name:
            playlist_already_made = True

if playlist_already_made:
    sys.exit("There is already a playlist with this name.")
elif not playlist_already_made:
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=f"Top songs from {date}")
    sp.playlist_add_items(playlist_id=playlist["id"], items=spotify_uris)
# print(song_names)