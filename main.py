
from random import choice
import youtube_dl
import anime
from keep_alive import keep_alive
import discord, io, random
import time, requests, sys, os, config
import nekos
from discord.ext import commands, tasks



client = commands.Bot(command_prefix='?', intents = discord.Intents.all())
cogs = [anime]
for i in range(len(cogs)):
  cogs[i].setup(client)



status = ['Neon Genesis Evangelion', 'The End of Evangelion', 'Evangelion: 1.0 You Are (Not) Alone', 'Evangelion: 2.0 You Can (Not) Advance', 'Evangelion: 3.0 You Can (Not) Redo', 'Evangelion: 3.0+1.0 Thrice Upon a Time', 'Shinji jerking off to me']

@client.event 
async def on_ready():
  change_status.start()
  print('we have logged in as{0.user}.format(client)'.format(client))
  
@tasks.loop(seconds=400)
async def change_status():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=choice(status)), status=discord.Status.do_not_disturb)



@client.command()
async def play(ctx, url:str):
  song_there = os.path.isfile("song.mp3")
  try:
    if song_there:
      os.remove("song.mp3")
  except PermissionError:
    await ctx.send("Wait for the current playing music to end or use the stop command")
    return

  vc = ctx.author.voice.channel
  await vc.connect()
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  
  ydl_opts = {
    'format' : "bestaudio",
    'postprocessors' : [{
    'key' : 'FFmpegExtractAudio',
    'preferredcodec' : 'mp3',
    'preferredquality' : '192',
    }],
  }
 
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
      os.rename(file,"song.mp3")
  voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def disconnect(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if not voice == None:
    await voice.disconnect()
  else:
    await ctx.send('the bot is not connected to a voice channel')

@client.command()
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  if voice.is_playing():
    voice.pause()
  else:
    await ctx.send("NO audio is playing")

@client.command()
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  if voice.is_paused():
    voice.resume()
  else:
    await ctx.send("The audio is not paused")

@client.command()
async def stop(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  voice.stop()
#!/usr/bin/env python3



  

    

keep_alive()
client.run("ODkxNjY4MjI5NjAzMzYwODE5.YVBswA.3Gxl4eKukOx0ttqBBnVmqtEga6g")
