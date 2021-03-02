# Get a job
import discord
from discord.ext import commands
import random as rand
import asyncio


async def find_current_job(member):
    for r in member.roles:
        if r.name in Job.LIST_OF_JOBS:
            return r

    return None


async def find_job_members(guild, job_role):
    count = 0
    for _ in (r for r in (member.roles for member in guild.members) if r == job_role):
        count += 1

    return count


class Job(commands.Cog):
    # ADD NEW JOBS HERE
    LIST_OF_JOBS = {
        "Worker": {"Wage": 10, "Total Occupancy": 10},
        "CEO": {"Wage": 50, "Total Occupancy": 1}
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def job(self, ctx):
        guild = ctx.guild
        member = ctx.message.author
        possible_job = rand.choice(list(Job.LIST_OF_JOBS.keys()))
        current_job = await find_current_job(member)

        if current_job is not None:
            if current_job.name == possible_job:
                await ctx.send(f"You weren't able to find a new job. Your current job is still `{current_job.name}`.")
                return

        if (role := discord.utils.get(guild.roles, name=possible_job)) is not None:
            current_occupancy = await find_job_members(guild, role)
            print(current_occupancy)
            if current_occupancy >= Job.LIST_OF_JOBS[possible_job]["Total Occupancy"]:
                await ctx.send(f"You weren't able to find a new job. Your current job is still `{current_job.name}`.")
                return

        m = await ctx.send(f"There is an available position as `{possible_job}`.\n"
                           f"It pays `{'${:,.2f}'.format(Job.LIST_OF_JOBS[possible_job]['Wage'])}`.\n"
                           f"React with a ✅ within 30 seconds to accept the position.")
        await m.add_reaction("✅")

        def check(reaction, user):
            return user == member and str(reaction.emoji) == "✅"

        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit(content="Time ran out.")
            return
        else:
            if role is None:
                try:
                    role = await guild.create_role(name=possible_job)
                except discord.Forbidden:
                    await ctx.send("I am not allowed to create roles.")
                    return

            if current_job is not None:
                await member.remove_roles(current_job)

            await member.add_roles(role)
            await ctx.send(f"You are now hired as `{possible_job}`!")

    @commands.command(aliases=['nomorejob', 'quit'])
    async def resign(self, ctx):
        current_job = await find_current_job(ctx.author)
        if current_job is None:
            await ctx.send("You don't have a job to remove!")
            return
        m = await ctx.send(f"Are you sure you want to resign from your job as `{current_job.name}`? "
                           f"React with ✅ to confirm.")
        await m.add_reaction("✅")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "✅"

        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit(content="Time ran out.")
            return
        else:
            ctx.author.remove_roles(current_job)
            await ctx.send(f"You have resigned from your job as `{current_job.name}`.")

    @commands.command()
    async def work(self, ctx):
        current_job = await find_current_job(ctx.message.author)
        if current_job is not None:
            # economy = self.bot.get_cog('Economy')
            wage = Job.LIST_OF_JOBS[current_job.name]['Wage']
            # if economy is not None:
                # await economy.deposit_money(ctx.author, wage)
            await ctx.send(f"You gained `{'${:,.2f}'.format(wage)}` ")
        else:
            await ctx.send("You're not hired. Try using *job.")


def setup(bot):
    bot.add_cog(Job(bot))
