import json
import requests

def getIp():

    """
    gets the ip address

    Returns:
        (str) - The ip address \n
    """
    
    url = "https://api.ipify.org?format=json"

    #gets the ip
    response = requests.get(url)

    data = json.loads(response.text)

    return data["ip"]