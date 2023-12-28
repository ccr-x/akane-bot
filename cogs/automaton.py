import discord
from discord.ext import commands
from discord import app_commands

from core.client import AkaneBot


class Help(commands.Cog):

    def __init__(self, bot: AkaneBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Automaton cog loaded')

    @commands.command(pass_context=True)
    async def auto_bump(self, ctx):

        try:
            # TODO: Set up automation somewhere else and create check here
            
            # TODO: Place asynchronous timer that runs the next code every two hours

            # TODO: Create time variable that contains current time stamp of the 2 hours delay

            # Send message every time it has succesfully run the code
            await ctx.send(f"Bumped server! \n Next bump is in {time}")

        # Send error code
        except Exception:
            await ctx.send(f"Something went wrong. Check error code for furher information: \n {Exception}")




async def setup(bot):
    await bot.add_cog(Help(bot), guilds=[discord.Object(id=1123380624531656725)])