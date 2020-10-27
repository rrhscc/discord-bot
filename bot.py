#import the stuff
import discord
from discord.ext import commands
import json

# with open("config.json") as f:
#   config = json.load(f)


# get extra top secret data from discord
#intents = discord.Intents.default()
#intents.members = True

#make bot with * prefix
#client = commands.Bot(command_prefix = "*", intents = intents)
bot = commands.Bot(command_prefix = "*")

#print bot here when the bot connects to discord
@bot.event
async def on_ready():
   print("bot here")

#send hi to discord when someone does *hi
@bot.command()
async def hi(ctx):
    await ctx.send("hi")
      
#echo command, this one has arguments
@bot.command()
async def echo(ctx, stuff: str):
   await ctx.send(stuff)
   
if __name__ == "__main__":
   bot.load_extension(ping)
   bot.load_extension(test)

# start sending the things to the discord
with open("token.txt") as f:
   bot.run(f.read())

#bot.run(config['TOKEN'])
