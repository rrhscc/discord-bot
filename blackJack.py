# blackjack
import discord
from discord.ext import commands

class blackJack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blackJack(self, ctx):
        m = await ctx.send(f'Welcome To Blackjack! React with ✅ to begin.')
        await m.add_reaction("✅")

def setup(bot):
    bot.add_cog(blackJack(bot))
