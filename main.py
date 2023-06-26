from savify import Savify
from savify.types import Type, Format, Quality
import random
import streamlit as st 

# Defining some global variables 
CLIENT_ID = ""
CLIENT_SECRET = ""

# Function for ramdom balloon animations
def random_celeb():
    return random.choice([st.balloons()])
    
# setting up Spotify client 
s = Savify(api_credentials=(CLIENT_ID,CLIENT_SECRET),  quality=Quality.BEST, download_format=Format.MP3)

# Function to download Spotify track
def track(url):
    try:
        st.info("Downloading...")
        x = s.download(url, query_type=Type.TRACK)
        st.success("Download completed!")
        st.audio(x, format='mp3')
    except Exception as e:
        st.error(e)
        
# Function to download Spotify playlist 
def playlist(url):
    try:
        st.info("Downloading...")
        x = s.download(url, query_type=Type.PLAYLIST)
        st.success("Download completed!")
        st.audio(x, format='mp3')
    except Exception as e:
        st.error(e)
        
# Function to download Spotify album
def album(url):
    try:
        st.info("Downloading...")
        x = s.download(url, query_type=Type.ALBUM)
        st.success("Download completed!")
        st.audio(x, format='mp3')
    except Exception as e:
        st.error(e)
    
    
# Integration of all above-defined functions
st.title("Spotify Downloader")
url = st.text_input(label="Paste your Spotify URL")
if st.button("Download"):
    if url:
        try:
            with st.spinner("Loading..."):
                if 'playlist' in url:
                    playlist(url)
                elif 'album' in url:
                    album(url)
                else:
                    track(url)
            random_celeb()
        except Exception as e:
            st.error(e)
    
