#import the stuff
import discord
from discord.ext import commands

# get extra top secret data from discord
intents = discord.Intents.default()
intents.members = True

#make bot with * prefix
client = commands.Bot(command_prefix = "*", intents = intents)

#print bot here when the bot connects to discord
@client.event
async def on_ready():
   print("bot here")

#send hi to discord when someone does *hi
@client.command()
async def hi(ctx):
    await ctx.send("hi")

# start sending the things to the discord
await client.run(TOKEN)
