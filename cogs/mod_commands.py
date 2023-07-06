import discord
from discord.ext import commands
from discord import app_commands

from core.client import AkaneBot


class ModCommands(commands.Cog):

    def __init__(self, bot: AkaneBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Mod Command cog loaded')

    @commands.command()
    async def zync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)

        await ctx.send(f'Synced {len(fmt)} command(s) in current guild.')

    # TODO: Add Interaction to make this command working
    @app_commands.command(name="sync", description="Sync all commands with current guild")
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)

        await ctx.send(f'Synced {len(fmt)} command(s) in current guild.')


async def setup(bot):
    await bot.add_cog(ModCommands(bot), guilds=[discord.Object(id=1123380624531656725)])