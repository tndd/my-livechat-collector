import json
import os

from dotenv import load_dotenv

from google.cloud import storage

load_dotenv('.env')

fname = 'output_youtube_data_api_search_list.json'
with open(fname, 'r') as f:
    data = json.loads(f.read())

channel_data = {}
channel_data['channel_id'] = data['items'][0]['snippet']['channelId']
channel_data['channel_title'] = data['items'][0]['snippet']['channelTitle']

videos_data = {}
for d in data.get('items', []):
    videos_data[d['id']['videoId']] = {
        'title': d['snippet']['title'],
        'published_at': d['snippet']['publishedAt']
    }

channel_data.update(videos_data=videos_data)

client = storage.Client.from_service_account_json(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
bucket_name = os.environ.get('BUCKET_NAME')

bucket = client.get_bucket(bucket_name)
blob = bucket.blob(f"channel-video-list/{channel_data['channel_id']}.json")

blob.upload_from_string(
    data=json.dumps(channel_data, indent=4, ensure_ascii=False),
    content_type='application/json'
)
