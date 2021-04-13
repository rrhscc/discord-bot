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
        await m.add_reaction("2️⃣")
           

        def check(reaction, user):
          return user == ctx.author and str(reaction.emoji) == "1️⃣" or str(reaction.emoji) == "2️⃣"
            
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit('timed out. :(')
            return
          
        if str(reaction.emoji) == "1️⃣":   
            ctx.send("You bought: a christmas decor!!")
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                if not await economy.withdraw_money(ctx.author, 10):
                    await ctx.send('You do not have enough money for this item!')
                try:
                    username = "🎄 " + ctx.message.author.name + " 🎄"
                    await ctx.message.author.edit(nick=username)
                    await ctx.send(f'Nickname was changed.')
                except discord.errors.Forbidden:
                    await ctx.send('I\'m not powerful enough to change your nickname.')
                    await economy.deposit_money(ctx.author, 10)
             
        elif str(reaction.emoji) == "2️⃣":
            ctx.send("You bought: A rich pass!!")
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                if not await economy.withdraw_money(ctx.author, 100000000000000001097906362944045541740492309677311846336810682903157585404911491537163328978494688899061249669721172515611590283743140088328307009198146046031271664502933027185697489699588559043338384466165001178426897626212945177628091195786707458122783970171784415105291802893207873272974885715430223118335):
                    await ctx.send('You do not have enough money for this!')
                try:
                    username = "💵 " + ctx.message.author.name + " 💵"
                    await ctx.message.author.edit(nick=username)
                    await ctx.send(f'Nickname was changed. Thanks for purchasing rich pass! ')
                except discord.errors.Forbidden:
                    await ctx.send('I\'m not powerful enough to change your nickname.')
                    await economy.deposit_money(ctx.author, 100000000000000001097906362944045541740492309677311846336810682903157585404911491537163328978494688899061249669721172515611590283743140088328307009198146046031271664502933027185697489699588559043338384466165001178426897626212945177628091195786707458122783970171784415105291802893207873272974885715430223118335)
                    
        
def setup(bot):
    bot.add_cog(shop(bot))
    
    
