# Get a job
import discord
import asyncio
from discord.ext import commands

class job(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def job(ctx):
            await ctx.send('You have a new job. Your job is now: Worker')
            guild = ctx.guild
            await guild.create_role(name="Worker")
            member = ctx.message.author
            role = get(member.server.roles, name="Worker")
            await bot.add_roles(member, role)
            
            
            
            
           # economy = self.bot.get_cog('Economy')
           # if economy is not None:
                #await economy.deposit_money(ctx.author, 1.25)

            

def setup(bot):
    bot.add_cog(job(bot))
