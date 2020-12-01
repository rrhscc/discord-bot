import discord
import asyncio
from discord.ext import commands

class chnick(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
      
  @commands.command()
  async def chnick(self, ctx):
    msg_split = ctx.message.content.split(" ", 1) #limits to 1 split
    if len(msg_split) > 1:
        username = "🎄 " + msg_split[1].strip() + " 🎄"
        try:
            await ctx.message.author.edit(nick=username)
            await ctx.send(f'Nickname was changed.')
        except discord.errors.Forbidden:
            await ctx.send(f'I\'m not powerful enough to change your nickname, but you might be! Set your nickname to {username}.')
        return
        
    await ctx.send(f'Do the command with your desired nickname')
    
      
def setup(bot):
    bot.add_cog(chnick(bot))
