# blackjack
import discord
from discord.ext import commands

class blackJack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send(f'Welcome To Blackjack!')

def setup(bot):
    bot.add_cog(blackJack(bot))
