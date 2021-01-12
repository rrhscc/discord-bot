import discord
from discord.ext import commands
import sqlite3
conn = sqlite3.connect('database.db')
# CREATE TABLE bank (id INTEGER PRIMARY KEY, price REAL)
c = conn.cursor()
economy_dict = {}

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Returns false if there is not enough money in member's bank
    async def withdraw_money(self, member, money):
        if economy_dict.get(member.id, None) is None:
            economy_dict[member.id] = 0
        if economy_dict[member.id] - money < 0:
            return false
        economy_dict[member.id] -= money
        return true

    async def deposit_money(self, member, money):
        if economy_dict.get(member.id, None) is None:
            economy_dict[member.id] = 0
        economy_dict[member.id] += money
        return true
    
    async def amount(self, member):
        output = c.execute("SELECT price FROM bank WHERE id=?", [member.id])
        print(output)
        if output == None:
            output = 0
            c.execute("INSERT INTO bank (id, price) VALUES (?, ?)", [member.id, 0])
        return output[0]
    
    @commands.command()
    async def balance(self, ctx):
        amt = await self.amount(ctx.author)
        await ctx.send(f"You have ${amt}")
    
def setup(bot):
    bot.add_cog(Economy(bot))
