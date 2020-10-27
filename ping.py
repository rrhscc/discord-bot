import discord
from discord.ext import commands

class Ping(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
      
  @commands.command()
  async def botping(self,ctx):
      await ctx.send(f"Bot ping is {self.bot.latency}")
      
def setup(bot):
    bot.add_cog(Ping(bot))
