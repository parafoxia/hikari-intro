import os
from pathlib import Path

import hikari
import crescent


def create_bot() -> crescent.Bot:
    # Load the token from a secrets file you'll need to create yourself.
    with open("./secrets/token") as f:
        token = f.read().strip()

    # Create the main bot instance with all intents.
    bot = crescent.Bot(token, intents=hikari.Intents.ALL)

    # Load all modules. This can either take discord.py-like strings,
    # or a series of Path objects.
    bot.plugins.load_folder("crescent_bot.plugins")
    return bot


if __name__ == "__main__":
    if os.name != "nt":
        # uvloop is only available on UNIX systems, but instead of
        # coding for the OS, we include this if statement to make life
        # easier.
        import uvloop

        uvloop.install()

    # Create and run the bot.
    create_bot().run()
