import discord
import asyncio
from discord.ext import commands

class chnick(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
      
  @commands.command()
  async def chnick(ctx, *, member: discord.Member, nick):
    msg_split = ctx.content.split()
    if msg_split.length > 0:
        username = msg_split[1].name or nick
        await member.edit(nick="🎄" + username + "🎄")
        await ctx.send(f'Nickname was changed.')
        return
        
    await ctx.send(f'Do the command with your desired nickname')
    
      
def setup(bot):
    bot.add_cog(chnick(bot))
