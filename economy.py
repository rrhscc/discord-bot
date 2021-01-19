import discord
from discord.ext import commands
import sqlite3
conn = sqlite3.connect('database.db')
# CREATE TABLE bank (id INTEGER PRIMARY KEY, price REAL)
c = conn.cursor()

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Returns false if there is not enough money in member's bank
    async def withdraw_money(self, member, money):
        output = c.execute("SELECT price FROM bank WHERE id=?", [member.id]).fetchone()
        print(output)
        if output == None:
            c.execute("INSERT INTO bank (id, price) VALUES (?, ?)", [member.id, 0])
            return False
        update = c.execute("UPDATE bank SET price=price-? WHERE id=? AND price>=?", [money, member.id, money])
        print(update)
        return output[0] >= money

    async def deposit_money(self, member, money):
        output = c.execute("SELECT price FROM bank WHERE id=?", [member.id]).fetchone()
        print(output)
        if output == None:
            c.execute("INSERT INTO bank (id, price) VALUES (?, ?)", [member.id, money])
            return True
        update = c.execute("UPDATE bank SET price=price+? WHERE id=?", [money, member.id, money])
        print(update)
        return True
    
    async def amount(self, member):
        output = c.execute("SELECT price FROM bank WHERE id=?", [member.id]).fetchone()
        print(output)
        if output == None:
            c.execute("INSERT INTO bank (id, price) VALUES (?, ?)", [member.id, 0])
            return 0
        return output[0]
    
    @commands.command()
    async def balance(self, ctx):
        amt = await self.amount(ctx.author)
        await ctx.send(f"You have {'${:,.2f}'.format(amt)}")
        
    @commands.command()
    async def burn(self, ctx, amount: float = None):
        if amount == None:
            await ctx.send(f"Please specify an amount to burn")
            return
        if amount < 0:
            await ctx.send(f"Please specify a positive amount to burn")
            return
        success = await self.withdraw_money(ctx.author, amount)
        if success:
            await ctx.send(f"Burned successfully")
            return
        await ctx.send(f"You do not have enough money to burn.")
    
def setup(bot):
    bot.add_cog(Economy(bot))
