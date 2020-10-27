import discord
from discord.ext import commands

class Tests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx, *, member: discord.Member = None):
<<<<<<< HEAD
        await ctx.send("hello!")
=======
        """Says hello"""
        member = member or ctx.author
        await ctx.send('Ping {0.name}~'.format(member))
>>>>>>> 8ba92aeafbfa9bc13ad26b590e19d9bf0e110584

def setup(bot):
    bot.add_cog(Tests(bot))
