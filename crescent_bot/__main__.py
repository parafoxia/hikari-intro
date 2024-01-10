import crescent
import hikari

# Load the token from a secrets file you'll need to create yourself.
with open("./secrets/token") as f:
    token = f.read().strip()

# Create the main bot instance with all intents.
bot = hikari.GatewayBot(token, intents=hikari.Intents.ALL)
client = crescent.Client(bot)

# Load all modules. This can either take discord.py-like strings,
# or a series of Path objects.
client.plugins.load_folder("crescent_bot.plugins")


if __name__ == "__main__":
    # Run the bot.
    bot.run()
