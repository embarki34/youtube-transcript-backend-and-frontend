from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ''
        for segment in transcript_list:
            transcript_text += segment['text'] + ' '
        return transcript_text.strip()
    except Exception as e:
        return f"Error fetching transcript: {e}"

def get_video_stats(video_id, api_key):
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        # Retrieve video statistics
        video_response = youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        ).execute()
        
        if 'items' in video_response:
            snippet = video_response['items'][0]['snippet']
            statistics = video_response['items'][0]['statistics']
            total_views = statistics.get('viewCount', 'N/A')
            total_comments = statistics.get('commentCount', 'N/A')
            publish_date = snippet.get('publishedAt', 'N/A')
        else:
            total_views = 'N/A'
            total_comments = 'N/A'
            publish_date = 'N/A'
        
        # Retrieve top comments
        comment_response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=3,
            order="relevance",
            textFormat="plainText"
        ).execute()
        
        top_comments = []
        if 'items' in comment_response:
            for item in comment_response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                top_comments.append(comment)
        
        return {
            'total_views': total_views,
            'total_comments': total_comments,
            'publish_date': publish_date,
            'top_comments': top_comments
        }
    except Exception as e:
        return f"Error fetching video stats: {e}"
