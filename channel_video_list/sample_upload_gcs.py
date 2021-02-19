import json
import yaml

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

with open('sample_channel_video_list_out.yml', 'w') as f:
    yaml.dump(channel_data, f, allow_unicode=True, indent=4)
