# Get a job
import discord
import asyncio
from discord.ext import commands

class job(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def job(self, ctx):
        m = await ctx.send(f'Get a job. React with ✅ to begin.')
        await m.add_reaction("✅")
 
                      
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "✅"
            #newJob = 'Doctor'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit('timed out. :(')
        else:
            await ctx.send('You have a new job. Your job is now: Worker')
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                await economy.deposit_money(ctx.author, 1.25)

            

def setup(bot):
    bot.add_cog(job(bot))
