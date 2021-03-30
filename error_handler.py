import discord
from discord.ext import commands
from discord.ext.commands import errors

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, errors.MissingRequiredArgument):
            await ctx.send("missing required argument!")
            hlp = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
            await ctx.send_help(hlp)
        

def setup(bot):
    bot.add_cog(Errors(bot))
