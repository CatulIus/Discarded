#plz dont break
import os
import requests
import discord
print(discord.__version__)
from discord.ext import commands
import pycord
import random

#firebase firestore
#link https://firebase.google.com/docs/firestore/quickstart#python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})

db = firestore.client()

description = """
ahhhh.
"""

intents = discord.Intents.default()

bot = commands.Bot(command_prefix=">", description=description, intents=intents)


async def create_thread(self,name,minutes,message):
    token = 'Bot ' + self._state.http.token
    url = f"https://discord.com/api/v9/channels/{self.id}/messages/{message.id}/threads"
    headers = {
        "authorization" : token,
        "content-type" : "application/json"
    }
    data = {
        "name" : name,
        "type" : 11,
        "auto_archive_duration" : minutes
    }
 
    return requests.post(url,headers=headers,json=data).json()

discord.TextChannel.create_thread = create_thread

@bot.event
async def on_ready():
  print("☭")

@bot.event
async def on_message(ctx):
  if ctx.content == ">test":
    await ctx.send("i hate this")

  
@bot.event
async def on_message(ctx):
  if ctx.content == ">enterZaDungeon":
      f = await ctx.channel.create_thread(name="Dungeon", minutes=60, message=ctx)



@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

  


#makes the bot run  
bot.run(os.getenv('TOKEN'))