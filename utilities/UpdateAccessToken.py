import requests
import base64
import os

from dotenv import load_dotenv
from .UpdateEnv  import updateEnvVar
from .GetAccessToken import getSpotifyAccessToken


def UpdateAccessToken(authCode, refreshToken):
    """
    updates the users access token and saves it to enviroment

    Args:
        auth_code: (str) - the users auth code \n
        refresh_token: (str) - the users refresh token \n

    Returns:
        dict: {    
            AT: (str) - the users access token \n
            RT: (str) - the users refresh token \n
        }
    """

    #reloads .env file
    load_dotenv()

    #get users access token
    Tokens = getSpotifyAccessToken(authCode, refreshToken)

    #add access token to enviroment
    updateEnvVar("AT", Tokens["AT"])

    # if refresh token present
    if Tokens["RT"] is not None:

        #add access token to enviroment
        updateEnvVar("RT", Tokens["RT"])
        

    return Tokens