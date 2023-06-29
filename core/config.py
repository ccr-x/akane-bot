import os
from copy import deepcopy

from dotenv import load_dotenv

load_dotenv()


class Configure:
    """
    Creates configuration dictionary for the bot
    :param bot: requires the bot object to be connected to the configuration
    :type bot: AkaneBot
    """
    base_config = {
        "activity_type": int,
        "bot_token": str,
        "guild_id": int,
        "log": str,
        "owner": str,
        "status": str,
        "cai_token": str,
        "char_token": str,
    }

    def __init__(self, bot):
        self.bot = bot
        self.cache = {}

        self.load_cache_env()

    def load_cache_env(self):
        try:
            data = deepcopy(self.base_config)

            data.update({k.lower(): self.base_config[k.lower()](v) for k, v in os.environ.items()
                         if k.lower() in self.base_config})

            self.cache = data

            return data

        except Exception as err:
            print(f"Something went wrong: {err}")

    def __getitem__(self, item):
        try:
            return self.cache[item]
        except Exception as err:
            print(f"Unable to return requested item. Check error for more information: \n{err}")
