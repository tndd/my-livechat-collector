import os

from dotenv import load_dotenv

import googleapiclient.discovery
import googleapiclient.errors

load_dotenv('.env')

def main():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = os.environ.get("YOUTUBE_DATA_API_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name,
        api_version,
        developerKey=api_key
    )

    request = youtube.search().list(
        part="snippet",
        channelId="UCvaTdHTWBGv3MKj3KVqJVCw",
        eventType="completed",
        maxResults=50,
        order="date",
        type="video"
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()
