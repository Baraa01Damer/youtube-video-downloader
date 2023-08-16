from pytube import YouTube
import os

def download_youtube_video(video_url, save_path="."):
    try:
        yt = YouTube(video_url)
    except Exception as e:
        print("Error:", e)
        return

    video_title = yt.title
    print(f"Downloading: {video_title}")

    # Get the highest resolution stream
    video_stream = yt.streams.get_highest_resolution()

    # Download the video
    video_stream.download(output_path=save_path)

    print("Download complete!")

if __name__ == "__main__":
    # Prompt the user to enter the YouTube URL
    youtube_url = input("Enter the YouTube URL: ")
    
    # Prompt the user to enter the directory path to save the video (optional)
    save_directory = input("Enter the path to save the video (leave blank for current directory): ")

    if not save_directory:
        save_directory = "."

    # Download the video
    download_youtube_video(youtube_url, save_directory)