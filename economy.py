import discord
from discord.ext import commands

economy_dict = {}

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Returns false if there is not enough money in member's bank
    async def withdraw_money(self, member, money):
        if economy_dict[member.id] is None:
            economy_dict[member.id] = 0
        if economy_dict[member.id] - money < 0:
            return false
        economy_dict[member.id] -= money
        return true

    async def deposit_money(self, member, money):
        if economy_dict[member.id] is None:
            economy_dict[member.id] = 0
        economy_dict[member.id] += money
        return true
    
    async def amount(self, member):
        if economy_dict[member.id] is None:
            economy_dict[member.id] = 0
        return economy_dict[member.id]
    
    @commands.command()
    async def balance(self, ctx):
        amt = await self.amount(self, ctx.author)
        await ctx.send(f"You have ${amt}")
    
def setup(bot):
    bot.add_cog(Economy(bot))
