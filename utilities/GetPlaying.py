import requests
import os
import json
from dotenv import load_dotenv
from .GetImageFromId import GetImageFromId
from .UpdateAccessToken import UpdateAccessToken

def getCurrentSong(accessToken):

    """
    gets the currently playing song

    Args:
        access_token: (str) - the users access token

    Returns:
        dict: {
            playing: (bool) - playing status \n
            songName: (str) - the song title \n
            artistName: (str) - the artists name \n
            albumId: (str) - the album id \n 
            albumUrl: (str) - the album image url \n
            error: (bool) - error status \n
        }
    """
    
    load_dotenv()

    currentPlay = {}

    url = "https://api.spotify.com/v1/me/player/currently-playing"

    headers = {
        "Authorization": f"Bearer {accessToken}",
        'Content-Type': 'application/json'
    }

    #gets currently playing song
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:

        data = json.loads(response.text)

        #if sog currently playing
        if data['is_playing']:

            currentPlay["playing"] = True

            #get song name
            currentPlay["songName"] = data['item']['name']

            #get song artist
            currentPlay["artistName"] = data['item']['artists'][0]['name']

            #get the album ID 
            currentPlay["albumId"] = data['item']['album']['id']

            #get album url
            currentPlay["albumUrl"] = GetImageFromId(currentPlay["albumId"], accessToken)



        
        #if not
        else:
            currentPlay["playing"] = False       
    
    #if access token revoked
    elif response.status_code == 401:

        Tokens = UpdateAccessToken(None, os.getenv('RT')) 

        return getCurrentSong(Tokens["AT"])

    else:
        currentPlay["error"] = True


    return currentPlay