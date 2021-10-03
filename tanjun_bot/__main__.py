import os
from pathlib import Path

import hikari
import tanjun

# You'll want to change this.
GUILD_ID = 845688627265536010


def create_bot() -> hikari.GatewayBot:
    # Load the token from a secrets file you'll need to create yourself.
    with open("./secrets/token") as f:
        token = f.read().strip()

    # Create the main bot instance with all intents.
    bot = hikari.GatewayBot(token, intents=hikari.Intents.ALL)

    # Create a client from the bot instance. Doing this automatically
    # links the bot and the client together, so you don't need to worry
    # about that.
    #
    # The `set_global_commands` kwarg is useful for testing. If this is
    # set to True, you can use commands in any guild, but they may take
    # an hour to propagate. Passing a guild ID makes them available
    # immediately in the given guild. This can also be set on a
    # per-command basis.
    client = tanjun.Client.from_gateway_bot(bot, set_global_commands=GUILD_ID)

    # Load all modules. This can either take discord.py-like strings,
    # or a series of Path objects.
    client.load_modules(*Path("./tanjun_bot/modules").glob("*.py"))
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
