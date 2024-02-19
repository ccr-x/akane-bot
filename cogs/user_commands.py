import discord
from discord.ext import commands
from discord import app_commands

import requests

from core.client import AkaneBot


class UserCommands(commands.Cog):

    def __init__(self, bot: AkaneBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('User Command cog loaded')

    @app_commands.command(name="hello", description="Greet ya fellow server mate")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hi")

    @app_commands.command(name="ping", description="Returns pong")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong")

    @app_commands.command(name="facts", description="Tells you a fact about your chosen number")
    async def facts(self, interaction: discord.Interaction, number: str):
        response = requests.get(f"http://numbersapi.com/{number}")
        embed = discord.Embed(description=response.text)
        await interaction.response.send_message(embed=embed)

    # # TODO: Interaction taking too long and fails
    # @app_commands.command(name="talk", description="Talk with Akane herself")
    # async def talk(self, interaction: discord.Interaction, message: str):
    #     # Create view
    #     view = discord.ui.View(timeout=None)
    #
    #     # Get user author
    #     message = message.replace("/talk ", interaction.message.author.name + ": ")
    #
    #     # chat with the character
    #     data = await self.bot.ai_client.chat.send_message('D8tGHd25fa20HnyaQYqMjPQr46hpqFyR8dwmQnL4wiA', message)
    #
    #     # Get response
    #     message = data['replies'][0]['text']
    #
    #     # Send response
    #     await interaction.response.send_message(message, ephemeral=False)
    #
    # # TODO: Temporary fix to problem above, but are unable to use it using the / command prefix
    # @commands.command(pass_context=True)
    # async def talk(self, ctx):
    #     # Get user author
    #     message = ctx.message.content
    #     message = message.replace("/talk ", ctx.message.author.name + ": ")
    #
    #     # chat with the character
    #     data = ""
    #     async with ctx.typing():
    #         data = await self.bot.ai_client.chat.send_message('D8tGHd25fa20HnyaQYqMjPQr46hpqFyR8dwmQnL4wiA', message)
    #
    #     # Get response
    #     message = data['replies'][0]['text']
    #
    #     # Send response
    #     await ctx.send(message)


async def setup(bot):
    await bot.add_cog(UserCommands(bot), guilds=[discord.Object(id=1123380624531656725)])
