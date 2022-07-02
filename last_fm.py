# Importing the required Librarires
import requests
import json
import pandas as pd
from config import USER_AGENT, API_KEY


# Api key
API_KEY = API_KEY
USER_AGENT = USER_AGENT

# Function to return Dictionary of Songs take Emotion as Input
def SongByTag(tag):
    payload = {
        'api_key': API_KEY,
        'method': 'tag.getTopTracks',
        'format': 'json',
        'limit': 30
    }
    payload['tag'] = tag 

    url = 'https://ws.audioscrobbler.com/2.0/'
    response = requests.get(url, params = payload)
    response = response.json()
    return response['tracks']['track']


# Function to extract only required Information to Dictionary
def database(response):
    dict = {
        'Song': [],
        'Artist': [],
        'Song_mbid':[],
        'Artist_mbid':[]
    }
    for song in response:
        dict['Song'].append(song['name'])
        dict['Artist'].append(song['artist']['name'])
        dict['Song_mbid'].append(song['mbid'])
        dict['Artist_mbid'].append(song['artist']['mbid'])
    
    return dict

# This Function return Pandas DataFrame of Songs
def getAllSong(lst):
    df = pd.DataFrame({
        'Song': [],
        'Artist': [],
        'Song_mbid':[],
        'Artist_mbid':[]
    })
    for item in lst:
        response = SongByTag(item)
        dict = database(response)
        df2 = pd.DataFrame(dict)
        df = df.append(df2,ignore_index = True)
    return df

# Function to return List of Top Artists
def getTopArtist(df):
    lst = df['Artist'].value_counts()
    lst = lst.index[:6]
    artist = []
    for x in lst:
        artist.append(x)
    return artist
