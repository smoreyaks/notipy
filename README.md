# NotiPy

### Initial Release v1.0.0 - 17/06/2024
---

NotiPy is a python script used to post to a Discord Channel of your choosing when a local system folder has been updated with a new file.
NotiPy needs to be synced with your Discord Server Bot
Useful for creating a notification flow to receive Discord channel pings.


### Dependencies
pip install watchdog discord.py python-dotenv


### Environment Variable Setup
After installing dependencies, you will need to setup an environment variable file to store your private keys.

1. Create a .env file in the projects root directory.
2. Copy the following code into the .env and replace the corresponding text with your values:

DISCORD_TOKEN=replaceThisWithYourDiscordToken  
CHANNEL_ID=replaceThisWithYourDesiredChannelId  
DIRECTORY_TO_WATCH=replaceThisWithTheDirectoryToMonitor


### Discord Bot Setup

#### Bot Permissions
TBA

#### Server Permissions
TBA


### Run Script
1. Open Run with "Windows Key + R"  
2. Run cmd, to open a terminal  
3. Navigate to NotiPy project root folder in terminal.  
4. Once inside project root, run the script with "python notipy.py"  
