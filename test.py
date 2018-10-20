import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot

fbi_watchlist = []
disaster_victims = []

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    author = message.author
    if message.content == "trump":
        await client.send_message(message.channel, "@{} got SWAT’d".format(author))
        fbi_watchlist.append(author)
    if message.content == "!ping":
        await client.send_message(message.channel, "{}, Pong! xddd".format(message.author))
        await client.send_message(message.channel, "@{}, your Role is {} ".format(message.author, message.author.top_role))
        await client.send_message(message.channel, "@{}, your status is {} ".format(message.author, message.author.status))
    if message.content == "!aids":
        await client.send_message(message.channel, "{} has aids".format(author))
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"


client.run("NTAzMjA3MDgwNDk3NTEyNDYw.DqzLNg.y9Y5cEob5LlA-k5U5wIOmUt5UhM") #Replace token with your bots token