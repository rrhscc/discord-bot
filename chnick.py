import discord
import asyncio
from discord.ext import commands

class chnick(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
      
  @commands.command()
  async def chnick(self, ctx, *, member: discord.Member = None):
    print(ctx.message.content)
    msg_split = ctx.message.content.split()
    if len(msg_split) > 0:
        username = msg_split[1].name or member.nick
        await member.edit(nick="🎄" + username + "🎄")
        await ctx.send(f'Nickname was changed.')
        return
        
    await ctx.send(f'Do the command with your desired nickname')
    
      
def setup(bot):
    bot.add_cog(chnick(bot))
