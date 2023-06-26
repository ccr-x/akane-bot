import time

import discord
from discord.ext import commands

from core.config import Configure


class AkaneBot(commands.Bot):
    """
    Creates AkaneBot Object

    :param prefix: The prefix to call the bot
    :type prefix: str
    """
    def __init__(self, prefix):
        super().__init__(intents=discord.Intents.all(), command_prefix=prefix)

        self.config = Configure(self)

    # Checking the login of bot
    async def on_ready(self):
        """ Outputs message to console and logs channel when the bot is online"""
        print(f"Logged in as \n {self.user.name}\n {self.user.id}\n at {time.asctime()}\n ------")
        self.config.__getitem__("bot_token")

    def run(self, **kwargs):
        if self.config.__getitem__("bot_token") is not None or "":
            super().run(self.config.__getitem__("bot_token"))
        else:
            print("Unable to run: No Token")
