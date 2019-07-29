import dbl
import discord
from discord.ext import commands

import asyncio
import requests
import logging

DISCORD_BOT_TOKEN = 'NjA1NDgxOTQ5Nzc5NDYwMDk4.XT9S9g.eFuf9dlQgYqRY-yzeA1KTFUDZbw'
BOT_NAME = 'TestBot#9545'

client = discord.Client()

@client.event

async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    if message.author != BOT_NAME and message.content.startswith('Привет, TestBot'):
        print('[command]: test ')
        await message.channel.send('И тебе привет, %s.' % message.author)
        

client.run(DISCORD_BOT_TOKEN)
