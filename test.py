import dbl
import discord
import youtube_dl
from discord.ext import commands

import asyncio
import requests
import logging

import multiprocessing
import time

#discord.Message().

players = {}

DISCORD_BOT_TOKEN = 'NjA1NDgxOTQ5Nzc5NDYwMDk4.XT9Vzg.JZgvKNjxF9UcZziEih4_2aO3iDo'
BOT_NAME = 'TestBot#9545'
CREATOR_NAME = 'Sasha Drozdov#8680'

#client = discord.Client()
client = commands.Bot(command_prefix='?')
vclient = 0
source = 0

def play_music():
    global vclient, source
    while (True):
        vclient.play(source)
        source.read()
    #voice_client.play(source)

@client.event

async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message:discord.Message):
    global vclient
    if vclient.is_playing:
        vclient.stop()
    return  

@client.event
async def on_voice_state_update(member, before:discord.VoiceState, after:discord.VoiceState):
    global vclient, source
    if (str(member) == BOT_NAME):
        return
    if (after.channel == None):
        if (vclient.is_connected):
            await vclient.disconnect()            
    if (after.channel != None):
        if (vclient == 0):
            vclient =  await after.channel.connect()
        else:
            if vclient.is_connected:
                await vclient.disconnect()
            vclient =  await after.channel.connect()
        #source = discord.FFmpegPCMAudio("https://www.youtube.com/watch?v=hjGZLnja1o8")
        source = discord.FFmpegPCMAudio("/home/sasha/TestBot/music/output.avi")
        vclient.play(source)
        await asyncio.sleep(5)
        vclient.stop()
        #await vclient.disconnect()
    return

if discord.opus.is_loaded():
    print("OK")
client.run(DISCORD_BOT_TOKEN)
