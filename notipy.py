
# Discord bot token and channel ID

import os
import time
import asyncio
import discord
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from dotenv import load_dotenv
load_dotenv()
# Discord bot token and channel ID
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))


# Set up the intents
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

# Set up the Discord client with intents
client = discord.Client(intents=intents)

class Watcher:
    DIRECTORY_TO_WATCH = os.getenv('DIRECTORY_TO_WATCH')

    def __init__(self, loop):
        self.observer = Observer()
        self.loop = loop

    def run(self):
        event_handler = Handler(self.loop)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except Exception as e:
            self.observer.stop()
            print(f"Observer Stopped: {e}")

        self.observer.join()

class Handler(FileSystemEventHandler):
    def __init__(self, loop):
        self.loop = loop

    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            print(f"New file created: {file_name}")
            asyncio.run_coroutine_threadsafe(send_message(file_name), self.loop)

async def send_message(file_name):
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    print(f"Channel ID: {CHANNEL_ID}")
    print(f"Channel: {channel}")
    if channel:
        await channel.send(f"{file_name} is up!\n------------------------------------------")
    else:
        print("Channel not found. Check bot permissions and availability on server.")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

async def main():
    loop = asyncio.get_running_loop()
    watcher = Watcher(loop)
    loop.run_in_executor(None, watcher.run)
    await client.start(DISCORD_TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
