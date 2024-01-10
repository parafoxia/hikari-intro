import lightbulb

# Load the token from a secrets file you'll need to create yourself.
with open("./secrets/token") as f:
    token = f.read().strip()

# Create the main bot instance
bot = lightbulb.BotApp(token)

# Load all extensions.
bot.load_extensions_from("./lightbulb_bot/commands")


if __name__ == "__main__":
    # Run the bot.
    bot.run()
