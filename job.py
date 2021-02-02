# Get a job
import discord
import asyncio
from discord.ext import commands

class job(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def job(self, ctx):
            await ctx.send('You have a new job. Your job is now: Factory Worker')
            guild = ctx.guild
            member = ctx.message.author
            try:
                if (role := discord.utils.get(guild.roles, name="Worker")) is None: role = await guild.create_role(name="Worker")
            except discord.errors.Forbidden:
                await ctx.send('I do not have permission to create this role.')
                
            await member.add_roles(role)
            # economy = self.bot.get_cog('Economy')
            # if economy is not None:
                #await economy.deposit_money(ctx.author, 1.25)
                
    @commands.command()
    async def unemployment(self, ctx):
        employed = role.members.length
        total = guild.member_count
        unemployed = total - employed
        await ctx.send(f'In this server, {employed} members of {total} are employed. This means {unemployed} members are unemployed. The unemployment rate is {round(unemployed/total*100)}%.')
                
def setup(bot):
    bot.add_cog(job(bot))
