# Discord bot to run spotify api calls
import os
import discord
import time

from dotenv import load_dotenv

# get token as environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# define client 
client = discord.Client()

# Run when connection to discord is established 
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# Respond to messages
@client.event
async def on_message(message):
    # make sure user is not a bot
    if message.author == client.user:
        return
    
    # Test command 
    if 'p!test' in message.content.lower():
        await message.channel.send('Test')

    # TODO
    # - spotify api call controls through bot





# Instantiate
client.run(TOKEN)
