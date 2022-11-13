import os
from pathlib import Path

import hikari
import tanjun
from hikari import Intents


# To use the GUILD_MEMBERS intent, you will need to enable it
# on the Discord Developer Portal for your application
INTENTS = Intents.GUILD_MEMBERS | Intents.GUILDS

def create_bot() -> hikari.GatewayBot:
    # Load the token from a secrets file you'll need to create yourself.
    with open("./secrets/token") as f:
        token = f.read().strip()

    # Create the main bot instance with all intents.
    bot = hikari.GatewayBot(token, intents=INTENTS)

    # Create a client from the bot instance. Doing this automatically
    # links the bot and the client together, so you don't need to worry
    # about that.
    client = tanjun.Client.from_gateway_bot(bot)
    # Stop the client from listening for messages
    client.set_message_accepts(tanjun.MessageAcceptsEnum.NONE)

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
