import discord
import random
from discord.ext import commands

class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx, *, member: discord.Member = None, bet = None):
        if member is None:
            await ctx.send("Please specify a member to play.")
            return
        if bet is None or not (isinstance(amount, float) or isinstance(amount, int)):
            await ctx.send("Please specify a bet amount. Both you and your opponent will have to have at least this much money.")
            return
        
        m = await ctx.send(f"{ctx.author.name} has challenged {member.name} to a coinless coinflip! The pool is {'${:,.2f}'.format(bet*2)} requiring **{'${:,.2f}'.format(bet)}** from each player.\n{member.mention} must accept with ✅ to coinflip.")
        def check(reaction, user):
            return user == member and str(reaction.emoji) == "✅"
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit('timed out. :(')
            return
        else:
            economy = self.bot.get_cog('Economy')
            author_balance = await economy.withdraw_money(ctx.author, bet)
            if not author_balance:
                await ctx.send(f"{author.mention} doesn't have enough money.")
                return
            member_balance = await economy.withdraw_money(member, bet)
            if not member_balance < bet:
                await ctx.send(f"{member.mention} doesn't have enough money.")
                await economy.deposit_money(ctx.author, bet)
                return
            winner = random.choice((ctx.author, member))
            await ctx.send(f"{winner.mention} won! They get {'${:,.2f}'.format(bet*2)}")
            await economy.deposit_money(winner, bet*2)
    
def setup(bot):
    bot.add_cog(Coinflip(bot))
