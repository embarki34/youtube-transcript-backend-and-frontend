

# YouTube Transcript & Stats Fetcher

This Streamlit application allows users to fetch and display transcripts and statistics for YouTube videos. By entering a YouTube video URL, users can view the video player, transcript, and various statistics, including view count and top comments.

## Features

- **Fetch Video Transcript**: Retrieve the full transcript of the YouTube video.
- **Display Video Statistics**: Get statistics such as total views, total comments, and publish date.
- **Show Top Comments**: Display the top 3 comments for the video.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Streamlit
- YouTube Transcript API
- Google API Client Library

You can install the necessary packages using pip:

```bash
pip install streamlit youtube-transcript-api google-api-python-client
```

## Running the Application

1. **Set up your Google API Key**: Obtain an API key from the Google Cloud Console for the YouTube Data API v3 and replace the placeholder in the code.

2. **Run the Streamlit app:**

   ```bash
   streamlit run your_streamlit_app.py
   ```

3. Open your browser and navigate to `http://localhost:8501` to view the application.

## Application Structure

The application consists of the following main functions:

- **extract_video_id(url)**: Extracts the video ID from the given YouTube URL using a regular expression.

- **get_transcript(video_id)**: Fetches the transcript for the video using the YouTube Transcript API.

- **get_video_stats(video_id, api_key)**: Retrieves video statistics and top comments using the Google API Client Library.

- **main()**: Main function to handle user interactions and display the application interface.

## How to Use

1. Enter a valid YouTube video URL in the sidebar.
2. The application will extract the video ID and fetch the transcript and video statistics.
3. View the video player, transcript, and video statistics on the main page.

## API Key Configuration

Make sure to replace the following line in the code with your actual API key:

```python
api_key = "YOUR_API_KEY"
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

Omar
