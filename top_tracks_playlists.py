####################################################################################
# top_tracks_playlists.py                                                          #
# Author:        Alexander O'Dempsey (xander-odempsey@hotmail.com)                 #
# Modified by:   Alexander O'Dempsey (xander-odempsey@hotmail.com)                 #
# Date Created:  15/07/2018                                                        #
# Last Modified: 16/07/2018                                                        #
# Brief:         Creates the 3 top track playlists                                 #
####################################################################################

import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
import datetime

def top_tracks_playlists(username, id, secret):
    token = util.prompt_for_user_token(
                username = username, 
                scope = 'user-top-read playlist-modify-public ', 
                client_id = id, 
                client_secret = secret, 
                redirect_uri = 'http://localhost:8888/callback/')

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        ranges = ['short_term', 'medium_term', 'long_term']
        song_list = []

        for range in ranges:
            playlist_name = 'My Automated ' + range + ' Playlist'
            playlist_desc = 'Script last ran: ' + str(datetime.datetime.today()) + ' (Created with SpotiPython: https://github.com/xanderodempsey/SpotiPython)'
            new_playlist = sp.user_playlist_create(username, playlist_name, public=True, description=playlist_desc)
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
        print("Cannot get token \n Program terminating...")