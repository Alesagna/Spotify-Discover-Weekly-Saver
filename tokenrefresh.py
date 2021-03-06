from authentication import refreshToken, base_64ID
import requests
import json

#Initialize class that will hold the function to refresh the token

class Refresh:

    def __init__(self):
        self.refresh_token = refreshToken
        self.base_64 = base_64ID
        
        #Define function to refresh token

    def refresh(self):

        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                 data={"grant_type": "refresh_token", "refresh_token": refreshToken},
                                 headers={"Authorization": "Basic " + base_64ID})

        response_json = response.json()
        print(response_json)

        return response_json["access_token"]
