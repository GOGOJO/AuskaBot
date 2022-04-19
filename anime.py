import discord
from discord.ext import commands
import animec

class Anime(commands.Cog):
  """Anime commands for weebs"""
  def __init__(self,client):
    self.client = client


  @commands.command()
  async def anime(self,ctx,*,query):
    try:
      anime = animec.Anime(query)
    except:
      await ctx.send(embed = discord.Embed(description = "no anime was found"))
      return
    embed = discord.Embed(title = anime.title_english, description = anime.description, url = anime.url, color = discord.Color.random())
    embed.add_field(name = 'Episodes', value = str(anime.episodes))
    embed.add_field(name = 'Rating', value = str(anime.rating))
    embed.add_field(name = 'Broadcast date', value = str(anime.broadcast))
    embed.add_field(name = 'Popularity', value = str(anime.popularity))
    embed.add_field(name = 'Genre', value = str(anime.genres))
    embed.add_field(name = 'NSFW status', value = str(anime.is_nsfw()))
    embed.set_thumbnail(url = anime.poster)
    await ctx.send(embed = embed)

  @commands.command(aliases = ["char", "anime character"])
  async def image(self,ctx,*,query):
    try:
      char = animec.Charsearch(query)
    except:
      await ctx.send(embed = discord.Embed(description = "no character was found", color = discord.Color.red()))
      return
    embed = discord.Embed(title = char.title, url = char.url, color = discord.Color.random())
    embed.set_image(url = char.image_url)
    embed.set_footer(text = ", ".join(list(char.references.keys())[:2]))
    await ctx.send(embed = embed)

  
    
  

def setup(client):
  client.add_cog(Anime(client))