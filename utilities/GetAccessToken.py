import requests
import base64
import os

def getSpotifyAccessToken(authCode, refreshToken):

    """
    gets the users access and refresh token

    Args:
        authCode: (str) - the users authcode \n
        refreshToken: (str) - the refresh token \n

    Returns:
        dict: {
            AT: (str) - access_token \n
            RT: (str) - resfresh_token \n
        }

    """

    # Set up the endpoint URLs
    auth_endpoint = "https://accounts.spotify.com/api/token"

    # Base64 encode the client ID and secret
    client_creds = f"{os.getenv('CLIENT_ID')}:{os.getenv('CLIENT_SECRET')}"
    client_creds_b64 = base64.b64encode(client_creds.encode())

    # Set up the request headers and data
    headers = {
        "Authorization": f"Basic {client_creds_b64.decode()}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "redirect_uri": f"http://{os.getenv('IP')}:8000/callback"
    }
    
    if authCode is not None:
        data["grant_type"] = "authorization_code"
        data["code"] = authCode


    else:
        data["grant_type"] = "refresh_token"
        data["refresh_token"] = refreshToken


        
    # Send the request to get an access token
    response = requests.post(auth_endpoint, headers=headers, data=data)
    

    # Get the access token from the response
    access_token = response.json()["access_token"]

    # Check if refresh token in response
    refresh_token = None

    if "refresh_token" in response.json():

        # Get the refresh token from the response
        refresh_token = response.json()["refresh_token"]

    return {"AT": access_token, "RT": refresh_token}