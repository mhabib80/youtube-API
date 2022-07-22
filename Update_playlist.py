import os

import google_auth_oauthlib.flow
from pprint import pprint
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials

api_service_name = "youtube"
api_version = "v3"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
scopes = ["https://www.googleapis.com/auth/youtube"]
credentials = Credentials.from_authorized_user_file('youtube_token.json', scopes)
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)



def create_playlist(playlist_name):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": playlist_name,
            "description": "This is a sample playlist description.",
            "tags": [
              "sample playlist",
              "API call"
            ],
            "defaultLanguage": "en"
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()
    pprint(response)


def search(search_keywords):
    search_request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=search_keywords)
    search_response = search_request.execute()
    pprint(search_response)
    video_id = search_response['items'][0]['id']['videoId']
    return video_id



def update_playlist(search_keywords):
    video_id = search(search_keywords)
    update_request = youtube.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": "PLX2GvEZZQZFv-HdWgkwKiauwzh-ST9r4j",
            "resourceId": {
              "kind": "youtube#video",
              "videoId": video_id
            }
          }
        }
    )
    response = update_request.execute()
    pprint(response)


search('red lights chloe x halle')



