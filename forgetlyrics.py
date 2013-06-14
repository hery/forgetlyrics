import requests
import json 

apikey = "cd8462d8a900df627e954da096090907"
root_url = "http://api.musixmatch.com/ws/1.1/"
test_song_id = "15953433"

def get_lyrics_for_track_id(track_id):
  method = "track.lyrics.get"
  url = root_url + method
  payload = {'apikey': apikey, 'track_id': track_id}
  r = requests.get(url, params=payload)
  lyrics = r.json()['message']['body']['lyrics']['lyrics_body']
  return lyrics

def get_track_id_for_keywords_and_artists(keywords, artist):
  method = "track.search"
  url = root_url + method
  payload = {'apikey': apikey, 'q':keywords, 'q_artist': artist}
  r = requests.get(url, params=payload)
  first_track_id = r.json()['message']['body']['track_list'][0]['track']['track_id']
  return first_track_id

# Tests

# test get_lyrics_for_track_id
# lyrics = get_lyrics_for_track_id(test_song_id)
# print lyrics

# test get_track_id_for_keywords
# track_id = get_track_id_for_keywords_and_artists("radioactive", "imagine dragons")
# lyrics = get_lyrics_for_track_id(track_id)
# print lyrics

def main():
  artist = raw_input("Artist name contains:\n")
  title = raw_input("Track title contains:\n")
  track_id = get_track_id_for_keywords_and_artists(title, artist)
  lyrics = get_lyrics_for_track_id(track_id)
  print lyrics

if __name__ == "__main__":
  main()
