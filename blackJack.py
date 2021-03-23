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
        house_amount = random.randint(0,10)
        m = await ctx.send(f'Welcome to Blackjack! Your starting amount is: {player_amount}. React to add more.')
        
        await m.add_reaction("✅")
        await m.add_reaction("🛑")
           

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "✅"

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit(content = 'timed out. :(')
            return
        
        new_amount = (player_amount + random.randint(0,10))
        new_house_amount = (house_amount + random.randint(0,10))
        
        if (new_amount > 21):
            ctx.send(f'Your new amount is: {new_amount}. You lost. Nice job.')
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                await economy.withdraw_money(ctx.author, money)
        
        elif (new_amount > new_house_amount):
            ctx.send(f'Your new amount is: {new_amount} and bot amount is: {new_house_amount}. You win. Amazing.')
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                await economy.deposit_money(ctx.author, money * 1.25)
                
        else: 
            ctx.send(f'You lose by the house. RIP.')
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                await economy.withdraw_money(ctx.author, money)
                
        player_amount = new_amount

def setup(bot):
    bot.add_cog(blackJack(bot))
