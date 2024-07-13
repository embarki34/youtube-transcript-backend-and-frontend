import streamlit as st
from youtube_transcript_stat import get_transcript, get_video_stats
import re

def extract_video_id(url):
    # Regular expression to extract video ID from YouTube URL
    regex = r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        return None
    
def main():
    st.title("YouTube Transcript & Stats Fetcher")
    st.sidebar.title("YouTube Transcript & Stats Fetcher")

    # Create an empty placeholder for the explanatory text
    explanation_placeholder = st.empty()

    # Display explanatory text
    explanation_placeholder.write("""
This app fetches both the transcript and video statistics from YouTube videos. 
It utilizes the YouTubeTranscriptApi to retrieve the transcript and the 
Google API Client Library to fetch video statistics. Here's how it works:

1. Transcript Retrieval:
    - The YouTubeTranscriptApi.get_transcript() function is used to fetch the transcript of the video.
    - If successful, the transcript is extracted from the JSON response and displayed.

2. Video Statistics Retrieval:
    - The Google API Client Library is used to build a YouTube service object.
    - The youtube.videos().list() method is called to fetch video statistics such as view count, comment count, and publish date.
    - The youtube.commentThreads().list() method is used to retrieve the top 3 comments for the video.
    - If successful, the statistics are displayed in the sidebar.
    - If there is any error during the retrieval process, appropriate error messages are displayed.

Simply enter the YouTube video URL in the sidebar, and the app will handle the rest!
""")


    # Input for entering YouTube video URL in the sidebar
    video_url = st.sidebar.text_input("Enter YouTube Video URL:")
    
    if video_url:
        video_id = extract_video_id(video_url)
        if video_id:
            st.sidebar.subheader("Video Statistics")
            
            # Fetch video stats
            api_key = "AIzaSyCKkAcXWY3gpnDjtTe2_SkRcNDeF2_vkAk"
            video_stats = get_video_stats(video_id, api_key)
            if video_stats:
                st.sidebar.write(f"Total Views: {video_stats['total_views']}")
                st.sidebar.write(f"Total Comments: {video_stats['total_comments']}")
                st.sidebar.write(f"Publish Date: {video_stats['publish_date']}")
                st.sidebar.write("Top 3 Comments:")
                for i, comment in enumerate(video_stats['top_comments'], start=1):
                    st.sidebar.write(f"{i}. {comment}")
                # Once the results are shown, clear the explanatory text
                explanation_placeholder.empty()
            else:
                st.sidebar.warning("Video statistics not available.")
                
            # Video player in the main section
            st.subheader(f"YouTube Video Player for {video_id}")
            st.video(f"https://www.youtube.com/watch?v={video_id}")
            
            # Fetch transcript
            transcript = get_transcript(video_id)
            if transcript:
                st.subheader(f"Transcript for {video_id}")
                st.write(transcript)
            else:
                st.warning("Transcript not available.")
                
        else:
            st.warning("Invalid YouTube Video URL.")

if __name__ == "__main__":
    main()
