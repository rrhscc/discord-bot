# blackjack
import discord
import asyncio
from discord.ext import commands

class shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx):
        m = await ctx.send('Welcome to the shop? React with 1 to buy: Christmas decor for $10.')
        await m.add_reaction("1️⃣")
           

        def check(reaction, user):
          return user == ctx.author and str(reaction.emoji) == "1️⃣"
            
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit('timed out. :(')
          
        else:   
            ctx.send("You bought: a christmas decor!!")
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                if not economy.withdraw_money(ctx.author, 10):
                    await ctx.send('You do not have enough money for this item!')
                try:
                    username = "🎄 " + ctx.message.author.name + " 🎄"
                    await ctx.message.author.edit(nick=username)
                    await ctx.send(f'Nickname was changed.')
                except discord.errors.Forbidden:
                    await ctx.send('I\'m not powerful enough to change your nickname.')
                    economy.deposit_money(ctx.author, 10)
                
                return
        
def setup(bot):
    bot.add_cog(shop(bot))
