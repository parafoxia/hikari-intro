import arc
import hikari

# Load the token from a secrets file you'll need to create yourself.
with open("./secrets/token") as f:
    token = f.read().strip()

# Create the main bot instance.
bot = hikari.GatewayBot(token)
# Give the bot to arc.
client = arc.GatewayClient(bot)

# Load all extensions. This can either take discord.py-like strings,
# or a series of Path objects.
client.load_extensions_from("./arc_bot/extensions")


if __name__ == "__main__":
    # Run the bot.
    bot.run()
