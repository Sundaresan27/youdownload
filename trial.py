import os
import streamlit as st
from pytube import YouTube

st.title("YouTube Video Downloader")

# Ask the user for a video link
link = st.text_input("Enter the link of the YouTube video you want to download:")

if link:
    # Create a YouTube object
    yt = YouTube(link)

    # Get the available video streams
    streams = yt.streams.filter(progressive=True)

    # Get the highest resolution video stream
    video = streams.get_highest_resolution()

    if video:
        # Set the output file path and name
        output_file = os.path.join(os.path.dirname(__file__), f"{yt.title}.mp4")

        try:
            # Download the video
            st.write("Downloading video...")
            video.download(output_path=output_file)
            st.write("Video downloaded successfully!")
        except OSError as e:
            st.error(f"Error: {e}")
    else:
        st.error("No video stream available for download.")
else:
    st.error("Please enter a valid YouTube video link.")
