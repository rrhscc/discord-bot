import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "*", intents = intents)

@client.event
async def on_ready():
   print("bot here")

@client.command()
async def hi(ctx):
    await ctx.send("hi")

await client.run(TOKEN)
