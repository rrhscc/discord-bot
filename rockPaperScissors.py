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
            economy = self.bot.get_cog('Economy')
            if economy is not None:
                withdraw = await economy.withdraw_money(ctx.author, money)
                if not withdraw:
                    await ctx.send("You do not have enough money!")
                    return
                
                m = await ctx.send("Pick 'rock', 'paper, or 'scissors'")
                await m.add_reaction("🪨")
                await m.add_reaction("📃")
                await m.add_reaction("✂️")
                
                def check(reaction, user):
                    return user == ctx.author and (str(reaction.emoji) == "🪨" or str(reaction.emoji) == "📃" or str(reaction.emoji) == "✂️")

                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                except asyncio.TimeoutError:
                    await m.edit('timed out. :(')
                
                options = ['rock', 'paper', 'scissors']
                emojiOptions = ['🪨', '📃', '✂️']
                
                choice = options[ emojiOptions.index(str(reaction.emoji)) ]
                botChoice = random.choice(options)
                msgstring = f'Bot choice: {botChoice}\nYour choice: {choice}\n'
                if choice == botChoice:
                    msgstring+="It's a tie!"
                    result = 0
                elif len(choice) + len(botChoice) == 9:
                    if choice == 'paper':
                      msgstring+="You won!"
                      result = 1
                    else:
                      msgstring+="You lost :/"
                      result = -1
                elif len(choice) + len(botChoice) == 13:
                    if choice == 'scissors':
                      msgstring+="You won!"
                      result = 1
                    else:
                      msgstring+='You lost :/'
                      result = -1
                elif len(choice) + len(botChoice) == 12:
                    if choice == 'rock':
                      msgstring+='You won!'
                      result = 1
                    else:
                      msgstring+='You lost :/'
                      result = -1
                
                await ctx.send(msgstring)
                
                if result == 1:
                    await economy.deposit_money(ctx.author, money * 1.5)
                elif result == -1:
                    await economy.deposit_money(ctx.author, money * 0.5)
                else:
                    await economy.deposit_money(ctx.author, money)
def setup(bot):
    bot.add_cog(rockPaperScissors(bot))
