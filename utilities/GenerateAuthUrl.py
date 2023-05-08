
import os
import dotenv

def GenerateAuthUrl():

    """
    generates the authentication url for spotify

    Returns:
        (str) - the auth url \n
    """
    
    #gets .env file 
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    
    #generates auth uurl
    redirectUrl = f"http://{os.getenv('IP')}:8000/callback"
    scopes = ["user-library-read", "user-read-playback-state, user-read-recently-played"]
    authUrl = f"https://accounts.spotify.com/authorize?client_id={os.getenv('CLIENT_ID')}&response_type=code&redirect_uri={redirectUrl}&scope={'+'.join(scopes)}"

    return authUrl