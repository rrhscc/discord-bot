#roulette
#VERY VERY WIP
import discord
import asyncio
import random
from discord.ext import commands

class roulette(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roulette(self, ctx):
        await ctx.send("Welcome to roulette! What would you like to bet?\n1st : first 12 numbers = 3x\n2nd : second 12 numbers = 3x\n3rd : third 12 numbers = 3x\nOdd : odd number = 2x\nEven : even number = 2x\nNumber 1-36 = 10x\n0 or 00 = 20x")
        user = ctx.author
        def check(message):
            return message.author == user
        bet = await self.bot.wait_for('message', timeout = 10, check=check)
        bet = bet.content
        if bet.lower() == "1st" or bet.lower() == "2nd" or bet.lower() == "3rd" or bet.lower() == "odd" or bet.lower() == "even" or bet == "0" or bet == "00":
            print("oknotint")
        elif int(bet) == bet:
            print("okint")
        else:
            print("notok")
        await ctx.send("How much would you like to bet on " + bet)
        user = ctx.author
        def check(message):
            return message.author == user
        money = await self.bot.wait_for('message', timeout = 10, check=check)
        money = money.content
        if int(money) == money:
            print("alsook")
        else:
            print("notalsook")
        await ctx.send("Spinning roulette wheel!")
        result = random.randint(0, 38) + 1
        await ctx.send("Landed on : " + str(result))
        if bet.lower() == "1st":
            print("1st")
        elif bet.lower() == "2nd":
            print("2nd")
        elif bet.lower() == "3rd":
            print("3rd")
        elif bet.lower() == "even":
            print("even")
        elif bet.lower() == "odd":
            print("odd")
        elif int(bet) == bet:
            print(bet)
        else:
            print("error oops")

def setup(bot):
    bot.add_cog(roulette(bot))
