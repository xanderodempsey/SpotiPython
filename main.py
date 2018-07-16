####################################################################################
# main.py                                                                          #
# Author:        Alexander O'Dempsey (xander-odempsey@hotmail.com)                 #
# Modified by:   Alexander O'Dempsey (xander-odempsey@hotmail.com)                 #
# Date Created:  13/07/2018                                                        #
# Last Modified: 16/07/2018                                                        #
# Brief:         Menu for SpotiPython Program                                      #
####################################################################################

from top_tracks_playlists import top_tracks_playlists

username = input('Please input username: ')
client_id = input('Thank you, ' + username + ', please input your client id (from https://developer.spotify.com): ')
client_secret = input('Now your client secret, please: ')

option = ''
while option != 'q':
    print('What would you like to do? \n PLAYLIST CREATION \n 1. Top Tracks \n 2. Input Your Own Songs (WIP) \n q. Quit')
    option = input('')
    if option == '1':
        top_tracks_playlists(username, client_id, client_secret)
    elif option == '2':
        print('\nThis feature is currently being developed.\n')
    elif option == 'q':
        print('\nSee you later.\n')
    else:
        print('\nInvalid choice, please try again.\n')