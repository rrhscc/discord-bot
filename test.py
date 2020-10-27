import discord
from discord.ext import commands

class Tests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Ping {0.name}~'.format(member))
        else:
            await ctx.send('Ping {0.name}... This feels familiar.'.format(member))
        self._last_member = member

def setup(bot):
    bot.add_cog(Tests(bot))
