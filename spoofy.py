import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
import sys
import datetime

if len(sys.argv) > 3:
    username = sys.argv[1]
    client_id = sys.argv[2]
    client_secret = sys.argv[3]
    
else:
    print("Usage: %s username, client_id, client_secret" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(
                username=username, 
                scope='user-top-read playlist-modify-public ', 
                client_id=client_id, 
                client_secret=client_secret, 
                redirect_uri='http://localhost:8888/callback/')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    ranges = ['short_term', 'medium_term', 'long_term']
    song_list = []
    for range in ranges:
        playlist_name = 'My Automated ' + range + ' Playlist'
        playlist_desc = 'Script last ran: ' + str(datetime.datetime)
        new_playlist = sp.user_playlist_create(username, playlist_name)
        new_playlist_id = new_playlist['id']
        results = sp.current_user_top_tracks(time_range=range, limit=20)
        for i, item in enumerate(results['items']):
            song_list.append(item['id'])

        print('Adding songs to ' + '"' + playlist_name + '"')    
        sp.user_playlist_add_tracks(username, new_playlist_id, song_list)
        song_list.clear()
        print('Playlist ' + '"' + playlist_name + '"' + ' made')
    print('All playlists made')

else:
    print("can't get token")
    

    