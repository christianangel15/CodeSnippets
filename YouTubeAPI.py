import os
import re
import datetime
from googleapiclient.discovery import build

API_KEY = os.environ.get('YOUTUBE_API')

YT = build('youtube', 'v3', developerKey=API_KEY)


def PlaylistDuration(PlayListId):
    totalSeconds = 0

    hoursPat = re.compile(r'(\d+)H')
    minutesPat = re.compile(r'(\d+)M')
    secondsPat = re.compile(r'(\d+)S')

    nextPage = None
    while True:
        Plrequest = YT.playlistItems().list(part='contentDetails',
                                            playlistId=PlayListId, maxResults=50, pageToken=nextPage)
        Plres = Plrequest.execute()
        vidID = []
        for item in Plres['items']:
            vidID.append(item['contentDetails']['videoId'])

        vidRequest = YT.videos().list(part='contentDetails', id=','.join(vidID))
        vidRes = vidRequest.execute()

        for item in vidRes['items']:
            duration = item['contentDetails']['duration']

            hours = hoursPat.search(duration)
            minutes = minutesPat.search(duration)
            seconds = secondsPat.search(duration)

            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0
            seconds = int(seconds.group(1)) if seconds else 0

            vidSeconds = datetime.timedelta(
                hours=hours, minutes=minutes, seconds=seconds).total_seconds()
            totalSeconds += vidSeconds

        nextPage = Plres.get('nextPageToken')
        if not nextPage:
            break
    Playlist_Duration = datetime.timedelta(seconds=totalSeconds)
    return Playlist_Duration
