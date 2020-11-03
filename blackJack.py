# blackjack
import discord
import asyncio
from discord.ext import commands

class blackJack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blackJack(self, ctx):
        m = await ctx.send(f'Welcome To Blackjack! React with ✅ to begin.')
        await m.add_reaction("✅")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit('timed out.')
        else:
            await channel.send('👍')

def setup(bot):
    bot.add_cog(blackJack(bot))
