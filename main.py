from urllib import response
import requests
import json
from authentication import spotifyID, spotifyToken, dwID
from datetime import date
from tokenrefresh import Refresh

class saveSongs:
    def __init__(self):
        self.spotifyID = spotifyID
        self.spotifyToken = " "
        self.dwID = dwID
        self.songs = ""
        self.newDwID = ""

    def findSongs(self):
        print("Finding my Discover Weekly Songs...")
        query = f"https://api.spotify.com/v1/playlists/{dwID}/tracks"
        response = requests.get(query,
        headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.spotifyToken}"})
        response_json = response.json()
        for m in response_json["items"]:
            self.songs += (m["track"]["uri"] + ",")
        self.songs = self.songs[:-1]
        

    def makePlaylist(self):
        print("Creating my Playlist and Adding Songs...")
        todaysDate = date.today()
        dateFormatted = todaysDate.strftime("%m/%d/%Y")
        query = f"https://api.spotify.com/v1/users/{spotifyID}/playlists"
        requestBody = json.dumps({
            "name": f"Discover Weekly for {dateFormatted}",
            "description": f"Discover Weekly saved for the week of {dateFormatted} by my Discover Weekly Automation Program!",
            "public": False
        })
        response = requests.post(query, data=requestBody, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.spotifyToken}"})
        response_json = response.json()
        print(response_json)
        return response_json["id"]

    def addSongs(self):
        self.newDwID = self.makePlaylist()
        query = f"https://api.spotify.com/v1/playlists/{self.newDwID}/tracks?uris={self.songs}"
        response = requests.post(query, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.spotifyToken}"})
        response_json = response.json
        print(response_json)

    def doRefresh(self):
        print("Refreshing access token...")
        refresher = Refresh()
        self.spotifyToken = refresher.refresh()


x = saveSongs()
x.doRefresh()
x.findSongs()
x.addSongs()

