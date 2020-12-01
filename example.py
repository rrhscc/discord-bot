import discord
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        msg_split = ctx.message.content.split()
        print(msg_split)
        try:
            await ctx.send(f'Hello {msg_split[1].name}')
            return
        except:
            member = member or ctx.author
            await ctx.send(f'Hello {member.name}')

def setup(bot):
    bot.add_cog(Example(bot))
