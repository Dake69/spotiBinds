import os
import time

import keyboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="c963ac8ff4a44fa084d2cf35086210ae",
    client_secret="d4efc569545a49acb461a2c087f36eb6",
    redirect_uri="http://localhost:8080/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

def play_song(song_uri):
    devices = sp.devices()
    print("Список устройств:", devices)

    if not devices['devices']:
        print("Нет доступных устройств для воспроизведения.")
        return

    device_id = devices['devices'][0]['id']
    print(f"Воспроизведение на устройстве: {device_id}")

    sp.start_playback(device_id=device_id, uris=[song_uri])


def pause_song():
    sp.pause_playback()

def url_to_uri(url):
    if "track/" in url:
        track_id = url.split("track/")[1].split("?")[0]
        return f"spotify:track:{track_id}"
    return None

url = input()
uri = url_to_uri(url)
play_song(uri)

while True:
    keyboard.add_hotkey('Ctrl + 2', pause_song)
#{'devices': [{'id': '1c27addb8497b4badcaa5784c24489881fea77b7', 'is_active': True, 'is_private_session': False, 'is_restricted': False, 'name': 'DESKTOP-25AN9DB', 'supports_volume': True, 'type': 'Computer', 'volume_percent': 24}, {'id': 'f3747869da932258fb700fe2906c55efc4d157df', 'is_active': False, 'is_private_session': False, 'is_restricted': False, 'name': 'MIBOX4', 'supports_volume': True, 'type': 'TV', 'volume_percent': 53}]}
