# This script can be run in youtube_env
# virtual environment by the command
# python3.8 youtube_check.py

from googleapiclient.discovery import build

api_key = 'AIzaSyCrHU3VEj9gMNdSU8aiq7D6yxi45hm0lnU'


youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(part='statistics', forUsername='schafer5')

response = request.execute()
print(response)
