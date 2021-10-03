import os
from importlib import import_module
from pathlib import Path

import hikari
import lightbulb


def create_bot() -> lightbulb.Bot:
    # Load the token from a secrets file you'll need to create yourself.
    with open("./secrets/token") as f:
        token = f.read().strip()

    # Create the main bot instance with all intents.
    bot = lightbulb.Bot(token=token, prefix="!", intents=hikari.Intents.ALL)

    # Gather all slash command files.
    commands = Path("./lightbulb_bot/commands").glob("*.py")

    # Load each slash command extension into the bot.
    for c in commands:
        bot.load_extension(f"lightbulb_bot.commands.{c.stem}")

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
