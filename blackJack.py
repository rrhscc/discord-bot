# blackjack
import discord
import asyncio
import random
from discord.ext import commands

class blackJack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blackJack(self, ctx, money: int):
        player_amount = random.randint(0,10)
        m = await ctx.send(f'Welcome to Blackjack! Your starting amount is: {player_amount}. React to add more.')
        
    #    m = await ctx.send(f'Welcome To Blackjack! React with ✅ to begin.')
        await m.add_reaction("✅")
        
        
        def coinflip(self):
            return random.randint(0, 1)        

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "✅"

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit('timed out. :(')
        else:
            new_amount = (player_amount + random.randint(0,10))
            await ctx.send('Your new amount is: {new_amount}. Thanks for playing.')
            player_amount = new_amount
          #  await ctx.send('POGCHAMP')
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                await economy.withdraw_money(ctx.author, money)
                if self.coinflip() == 1:
                    await economy.deposit_money(ctx.author, money * 1.25)
            

def setup(bot):
    bot.add_cog(blackJack(bot))
