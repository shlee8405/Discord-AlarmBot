# bot.py
import os
import datetime
import time



import discord

from datetime import datetime

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default() 
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discoasdafrd!')

    text_channel_list = []
    for guild in client.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)
    print(text_channel_list)
    # await text_channel_list[16].send("테스트")

    print(text_channel_list)
 
    i = 0
    while i<=10:
        i = i
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        
        print(now.strftime("%H:%M:%S"))
        if now.strftime("%H:%M:%S")=="10:58:00":
            await text_channel_list[11].send("Current Time ="+ current_time)
            break
            

client.run(TOKEN)