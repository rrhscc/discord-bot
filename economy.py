import discord
from discord.ext import commands
import sqlite3

initial_money = 10

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS bank (id INTEGER PRIMARY KEY, price REAL)")
c.execute("CREATE TABLE IF NOT EXISTS daily (id INTEGER PRIMARY KEY, datetime BIGINT)")

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Returns false if there is not enough money in member's bank
    async def withdraw_money(self, member, money):
        output = c.execute("SELECT price FROM bank WHERE id=?", [member.id]).fetchone()
        print(output)
        if output is None:
            if initial_money < money:
                c.execute("INSERT INTO bank (id, price) VALUES (?, ?)", [member.id, initial_money])
                return False
            else:
                c.execute("INSERT INTO bank (id, price) VALUES (?, ?)", [member.id, initial_money-money])
                return True
        update = c.execute("UPDATE bank SET price=price-? WHERE id=? AND price>=?", [money, member.id, money])
        print(update)
        return update is not None

    async def deposit_money(self, member, money):
        output = c.execute("SELECT price FROM bank WHERE id=?", [member.id]).fetchone()
        print(output)
        if output is None:
            c.execute("INSERT INTO bank (id, price) VALUES (?, ?)", [member.id, initial_money + money])
            return True
        update = c.execute("UPDATE bank SET price=price+? WHERE id=?", [money, member.id])
        print(update)
        return True
    
    async def amount(self, member):
        output = c.execute("SELECT price FROM bank WHERE id=?", [member.id]).fetchone()
        print(output)
        if output is None:
            c.execute("INSERT INTO bank (id, price) VALUES (?, ?)", [member.id, initial_money])
            return initial_money
        return output[0]
    
    @commands.command(description="Show your account balance.", aliases=['b', 'bal, 'amount', 'amt'])
    async def balance(self, ctx):
        amt = await self.amount(ctx.author)
        await ctx.send(f"You have {'${:,.2f}'.format(amt)}")

    @commands.command(description="Burn money.")
    async def burn(self, ctx, amount: float = None):
        if amount == None or not (isinstance(amount, float) or isinstance(amount, int)):
            await ctx.send(f"Please specify an amount to burn.")
            return
        if amount < 0:
            await ctx.send(f"Please specify a positive amount to burn.")
            return
        success = await self.withdraw_money(ctx.author, amount)
        if success:
            await ctx.send(f"You successfully burned ${amount}!")
            return
        await ctx.send(f"You do not have enough money to burn.")
                       
                       
    @commands.command(description="Give someone money.")
    async def give(self, ctx, amount: float = None, member: discord.Member = None):
        if amount == None or not (isinstance(amount, float) or isinstance(amount, int)):
            await ctx.send(f"Please specify an amount to give.")
            return
        if amount < 0:
            await ctx.send(f"Please specify a positive amount to give.")
            return
        if member == None:
            await ctx.send(f"Please specify someone to give your money to.")
            return
        success = await self.withdraw_money(ctx.author, amount)
        if success:
            await self.deposit_money(member, amount)
            
            embed_var = discord.Embed(description=f'{str(money)} seashells, just for you, {member.display_name}!')
            embed_var.set_author(name=f'From {ctx.author.display_name}...', icon_url=ctx.author.avatar_url)
            embed_var.set_thumbnail(url=member.avatar_url)

            await ctx.send(embed=embed_var)
            
            return
        await ctx.send(f"You do not have enough money to give.")
    
def setup(bot):
    bot.add_cog(Economy(bot))
