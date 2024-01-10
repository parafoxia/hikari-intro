from pathlib import Path

import hikari
import tanjun

# Load the token from a secrets file you'll need to create yourself.
with open("./secrets/token") as f:
    token = f.read().strip()

# Create the main bot instance.
bot = hikari.GatewayBot(token)

# Create a client from the bot instance. Doing this automatically
# links the bot and the client together, so you don't need to worry
# about that.
client = tanjun.Client.from_gateway_bot(bot)

# Load all modules. This can either take discord.py-like strings,
# or a series of Path objects.
client.load_modules(*Path("./tanjun_bot/modules").glob("*.py"))


if __name__ == "__main__":
    # Run the bot.
    bot.run()
