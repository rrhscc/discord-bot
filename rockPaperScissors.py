import discord
import asyncio
import random
from discord.ext import commands
#=======================#
class rockPaperScissors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rps','rockpaperscissors'])
    async def rockPaperScissors(self, ctx, money: int):
        m = await ctx.send(f"Welcome To 'Rock, Paper, Scissors!' React with ✅ to begin.")
        await m.add_reaction("✅")  

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "✅"

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit('timed out. :(')
        else:
            await ctx.send('POGCHAMP')
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                await economy.withdraw_money(ctx.author, money)
                

                choice = input("Pick 'rock', 'paper, or 'scissors': ")
                options = ['rock', 'paper', 'scissors']
                botChoice = random.choice(options)
                print(f'Bot choice: {botChoice}\tYour choice: {choice}')
                if choice == botChoice:
                    print("It's a tie!")
                    result = 0
                elif len(choice) + len(botChoice) == 9:
                    if choice == 'paper':
                      print("You won!")
                      result = 1
                    else:
                      print("You lost :/")
                      result = -1
                elif len(choice) + len(botChoice) == 13:
                    if choice == 'scissors':
                      print("You won!")
                      result = 1
                    else:
                      print('You lost :/')
                      result = -1
                elif len(choice) + len(botChoice) == 12:
                    if choice == 'rock':
                      print('You won!')
                      result = 1
                    else:
                      print('You lost :/')
                      result = -1
                if result == 1:
                    await economy.deposit_money(ctx.author, money * 1.25)
                elif result == -1:
                    await economy.withdraw_money(ctx.author, money - result)
def setup(bot):
    bot.add_cog(rockPaperScissors(bot))
