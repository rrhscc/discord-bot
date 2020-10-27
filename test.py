import discord
from discord.ext import commands

class Tests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx, *, member: discord.Member = None):
        await ctx.send("hello!")

def setup(bot):
    bot.add_cog(Tests(bot))
