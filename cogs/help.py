import discord
from discord.ext import commands
from discord import app_commands

from core.client import AkaneBot


class Help(commands.Cog):

    def __init__(self, bot: AkaneBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cog loaded')

    # TODO: Does not work
    @app_commands.command(name="help", description="Helps you getting to know the bot")
    async def help(self, ctx):
        user = ctx.message.author
        embed = discord.Embed()

        # Set bot author
        embed.set_author(name="_ccr", url="https://github.com/ccr-x",
                         icon_url="https://avatars.githubusercontent.com/u/32170529?v=4")

        await user.send(user, embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot), guilds=[discord.Object(id=1123380624531656725)])