import discord
from discord.ext import commands
games = {}
players = {}

class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tictactoe(self, ctx, *, member: discord.Member = None, bet = None):
        if member is None:
            await ctx.send("Please specify a member to play.)
        if bet not None and (not (isinstance(bet, float) or isinstance(bet, int))):
            await ctx.send("Please specify a valid bet amount. Both you and your opponent will have to have at least this much money.)
        
        m = await ctx.send(f"{ctx.author.name} has challenged {member.name} to TicTacToe! The pool is {'${:,.2f}'.format(bet*2)} requiring **{'${:,.2f}'.format(bet)}** from each player.\n{member.mention} must accept with ✅ to play.")
        await m.add_reaction("✅")
        
        def check(reaction, user):
            return user == member and str(reaction.emoji) == "✅"
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            try:
                await m.edit(content = 'timed out. :(')
            except: pass
            return
        else:
            economy = self.bot.get_cog('Economy')
            author_withdraw = await economy.withdraw_money(ctx.author, bet)
            if not author_withdraw:
                await ctx.send(f"{ctx.author.mention} doesn't have enough money.")
                return
            member_withdraw = await economy.withdraw_money(member, bet)
            if not member_withdraw:
                await ctx.send(f"{member.mention} doesn't have enough money.")
                await economy.deposit_money(ctx.author, bet)
                return
            
    
def setup(bot):
    bot.add_cog(TicTacToe(bot))
