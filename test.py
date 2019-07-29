import dbl
import discord
from discord.ext import commands

import asyncio
import requests
import logging

DISCORD_BOT_TOKEN = 'NjA1NDgxOTQ5Nzc5NDYwMDk4.XT9Nfg.J338d3btRnJ9SOUrq540eXczYhc'


client = discord.Client()

@client.event

async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith('test'):
        print('[command]: test ')
        await message.channel.send('test')
        

client.run(DISCORD_BOT_TOKEN)
