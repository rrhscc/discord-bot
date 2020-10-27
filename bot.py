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
      
#echo command, this one has arguments
@client.command()
async def echo(ctx, stuff: str):
   await ctx.send(stuff)
   
if __name__ == "__main__":
   bot.load_extension(cogs.ping)
   bot.load_extension(cogs.test)

# start sending the things to the discord
with open("token.txt") as f:
   await client.run(f.read())
