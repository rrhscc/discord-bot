import discord
from discord.ext import commands
games = {}
players = {}

class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, member: discord.Member = None, bet = None):
        if member is None:
            await ctx.send("Please specify a member to play.)
        if bet is None or not (isinstance(amount, float) or isinstance(amount, int)):
            await ctx.send("Please specify a bet amount. Both you and your opponent will have to have at least this much money.)
        
        await ctx.send(f'Hello {member.name}!')
    
def setup(bot):
    bot.add_cog(TicTacToe(bot))
