import discord
from discord.ext import commands

from bot import thing

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *, recip=None, member: discord.Member = None):
        if recip is not None:
            await ctx.send(f'Hello {recip}!')
            return

        member = member or ctx.author
        await ctx.send(f'Hello {member.name}!')
    
    @commands.command()
    async def testthing(self, ctx):
        await ctx.send(thing[0])
    
def setup(bot):
    bot.add_cog(Example(bot))
