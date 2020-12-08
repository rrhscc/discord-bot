#import the stuff
import discord
from discord.ext import commands
import json

thing = ["beans"]

#with open("config.json") as f:
#   config = json.load(f)


# don't get extra top secret data from discord
#intents = discord.Intents.default()

# make bot with * prefix
#client = commands.Bot(command_prefix = "*", intents = intents)
bot = commands.Bot(command_prefix = "*")

# print bot here when the bot connects to discord
@bot.event
async def on_ready():
   print("bot here")

# process all messages
@bot.event
async def on_message(message):
   if message.author == bot.user:
      return
   
   await bot.process_commands(message)

# send hi to discord when someone does *hi
@bot.command()
async def hi(ctx):
    await ctx.send("hi")
      
# echo command, this one has arguments
@bot.command()
async def echo(ctx, stuff: str):
   await ctx.send(stuff)

# load all other commands
if __name__ == "__main__":
   bot.load_extension("ping")
   bot.load_extension("example")
   bot.load_extension("blackJack")
   bot.load_extension("chnick")

# start the bot
with open("token.txt") as f:
   bot.run(f.read())

#bot.run(config['TOKEN'])
