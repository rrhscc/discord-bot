import discord
from discord.ext import commands
from discord.ext.commands import errors

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        pass

def setup(bot):
    bot.add_cog(Errors(bot))
