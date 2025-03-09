import yt_dlp


'''
This code serves the purpose of downloading youtube videos in the desired resolution.
'''

# Step 1 - Provide video URL. Copy and paste the URL from YouTube
VIDEO_URL = ""

# Step 2 - Provide output path where downloaded video shall be stored
OUTPUT_PATH = ""

def download_youtube_video(video_url, output_path='.'):
    
    # Step 3 - Provide options for downloading
    ydl_opts = {
        'format': '136',  # Download the best quality available
        'playlist_items': str(7),
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output template
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Downloading: {video_url}")
            ydl.download([video_url])
            print("Download completed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":

    download_youtube_video(VIDEO_URL, OUTPUT_PATH)