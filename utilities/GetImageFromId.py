
import dotenv
import requests
import json


def GetImageFromId(albumId, accessToken):

    """
    gets the album image from its id

    Args:
        album_id: (str) - the album id \n
        access_token: (str) - the users access token \n

    Returns:
        (str) - the image url \n
    """
    
    #gets .env file 
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    #general headers for api
    headers = {
        "Authorization": f"Bearer {accessToken}",
        'Content-Type': 'application/json'
    }

    #send request to spotify api
    albumResponse = requests.get(f'https://api.spotify.com/v1/albums/{albumId}', headers=headers)

    #load the response data to json
    albumData = json.loads(albumResponse.text)

    #gets image url from data
    imageUrl = albumData['images'][0]['url']

    return imageUrl