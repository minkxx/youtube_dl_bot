import os
import pyrogram
from pyrogram import Client, filters
from pytube import YouTube

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize the Pyrogram client
api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN
app = Client('my_bot', api_id, api_hash, bot_token=bot_token)

# Define a function to handle incoming messages
@app.on_message(filters.command('start'))
def start_handler(client, message):
    # Send a welcome message to the user
    client.send_message(message.chat.id, 'Hey! Send me a YouTube video link and I will download it for you.\nMade with ❤️ by @minkxx69')

# Define a function to handle incoming video links
@app.on_message(filters.regex(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$'))
def download_handler(client, message):
    # Get the video link from the message
    link = message.text

    # Download the video using PyTube
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download()

    # Send the video file to the user
    client.send_message(message.chat.id, 'Here is your video that you requested to download...')
    client.send_video(message.chat.id, video.default_filename)
    client.send_message(message.chat.id, 'Thanks for using our service.')

    # Delete the downloaded file from the server
    os.remove(video.default_filename)

# Start the Pyrogram client
app.run()
