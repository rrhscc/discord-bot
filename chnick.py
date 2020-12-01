import discord
import asyncio
from discord.ext import commands

class chnick(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
      
  @commands.command(pass_context=True)
  async def chnick(ctx, *, nick, member: discord.Member):
    username = nick or ctx.message.author.display_name
    await member.edit(nick="🎄" + username + "🎄")
    await ctx.send(f'Nickname was changed for {member.mention} ')
      
def setup(bot):
    bot.add_cog(chnick(bot))
