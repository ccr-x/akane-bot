import asyncio
import discord
import os

from core import config
from core.client import AkaneBot

from discord.ext import commands

# Create Akane bot
bot = AkaneBot('.')

bot.remove_command('help')


# Load all cogs
async def load():
    for file in os.listdir('./cogs'):  # Check for all files inside of cogs directory
        if file.endswith('.py'):  # Check if file ends with .py
            await bot.load_extension(f'cogs.{file[:-3]}')  # Remove .py


async def main():
    await load()
    await bot.run()


asyncio.run(main())
