import dbl
import discord
import youtube_dl
from discord.ext import commands

import asyncio
import requests
import logging

import multiprocessing
import time
import sqlite3

from my_classes import YTDLSource
#discord.Message().

players = {}

DISCORD_BOT_TOKEN = 'NjA1NDgxOTQ5Nzc5NDYwMDk4.XUFYeQ.LKGc8kUXDnExPKj12MHBlh3zMqE'
BOT_NAME = 'TestBot#9545'
CREATOR_NAME = 'Sasha Drozdov#8680'

#client = discord.Client()
db = sqlite3.connect('./bot.db')
cursor = db.cursor()
"""cursor.execute('''
    CREATE TABLE users(name TEXT PRIMARY KEY, url TEXT)
''')
db.commit()"""
#db.commit()
client = commands.Bot(command_prefix='.')
vclient = 0
source = 0
cnt = 0

#ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    #print(client.user.id)
    print('------')

def get_url(name):
    cursor.execute('''SELECT url FROM users WHERE name=?''', (name,))
    x = cursor.fetchone()
    if x == None:
        return ''
    return x[0]

def get_time(name):
    cursor.execute('''SELECT time FROM users WHERE name=?''', (name,))
    x = cursor.fetchone()
    if x == None:
        return 0
    return x[0]    

@client.event
async def on_voice_state_update(member, before:discord.VoiceState, after:discord.VoiceState):
    global vclient, source, cnt
    if (str(member) == BOT_NAME):
        return
    if (after.channel == None):
        return           
    if (after.channel != None and after.channel != before.channel):
        if (vclient == 0):
            vclient =  await after.channel.connect()
        else:
            if vclient.is_connected():
                #if vclient.is_playing():
                    #vclient.stop()
                #print(type(vlcient.is_connected()))
                #await vclient.disconnect()
                #print(vclient.is_connected())
                #vclient.connect()
                await vclient.move_to(after.channel)
            else:
                vclient =  await after.channel.connect()
        c_url = get_url(str(member))
        if (c_url == ''):
            await vclient.disconnect()
            return
        source = await YTDLSource.from_url(c_url, loop=client.loop, stream=False)
        if (vclient.is_connected()):
            if (vclient.is_playing()):
                vclient.stop()
            vclient.play(source)
            await asyncio.sleep(get_time(str(member)))
            if (vclient.channel == after.channel):
                vclient.stop()
        if (vclient.channel == after.channel):
            await vclient.disconnect()
    return

context = discord.ext.commands.context.Context

@client.command()
async def close(ctx:context):
    if (str(ctx.author) != CREATOR_NAME):
        await ctx.send("Permission denied")
        return
    db.close()
    await client.close()

@client.command()
async def echo(ctx:context, args):
    await ctx.channel.send(args)

@client.command()
async def add(ctx:context, *name):
    name = ' '.join(name)
    cursor.execute('''INSERT INTO users(name, url, time)
              VALUES(?,?,?)''', (name, '', 0))    
    db.commit()
    
@client.command()
async def remove(ctx:context, *name):
    name = ' '.join(name)
    cursor.execute('''DELETE FROM users WHERE id = ? ''', (name))
    db.commit()
    
@client.command()
async def set_url(ctx:context, *name):
    url = name[-1]
    name = ' '.join(name[:-1])
    cursor.execute('''UPDATE users SET url = ? WHERE name = ? ''',
     (url, name))     
    db.commit()
    
@client.command()
async def set_time(ctx:context, *name):
    time = int(name[-1])
    time = min(time, 10)
    name = ' '.join(name[:-1])
    cursor.execute('''UPDATE users SET time = ? WHERE name = ? ''',
     (time, name))     
    db.commit()
    
@client.command()
async def view(ctx:context, *name):
    name = ' '.join(name)
    await ctx.send(get_url(name) + ' ' + str(get_time(name)))


if not discord.opus.is_loaded():
    print("OPUS NOT LOADED")
client.run(DISCORD_BOT_TOKEN)
db.close()
