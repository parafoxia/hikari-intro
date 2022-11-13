import random

import lightbulb


# These two are the same type, but are optional. We can provide a
# default value simply by using the `default` kwarg.
@lightbulb.option("bonus", "A fixed number to add to the total roll.", int, default=0)
@lightbulb.option("sides", "The number of sides each die will have.", int, default=6, max_value=100)
# The options the command will have. This creates a required int
# option. Validation is handled for you -- Discord won't let you
# send the command unless it's a number, and only if that number
# is less than or equal to 25. How cool is that?!
@lightbulb.option("number", "The number of dice to roll.", int, max_value=25)
# Convert the function into a command
@lightbulb.command("dice", "Roll one or more dice.")
# Define the types of command that this function will implement
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def dice(ctx: lightbulb.SlashContext) -> None:
    # Extract the options from the context
    number = ctx.options.number
    sides = ctx.options.sides
    bonus = ctx.options.bonus

    # Option validation for prefix commands
    if number > 25:
        await ctx.respond("No more than 25 dice can be rolled at once.")
        return

    if sides > 100:
        await ctx.respond("The dice cannot have more than 100 sides.")
        return

    rolls = [random.randint(1, sides) for _ in range(number)]

    # To send a message, use ctx.respond. Using kwargs, you can make the
    # bot reply to a message (when not sent from a slash command
    # invocation), allow mentions, make the message ephemeral, etc.
    await ctx.respond(
        " + ".join(f"{r}" for r in rolls)
        + (f" + {bonus} (bonus)" if bonus else "")
        + f" = **{sum(rolls) + bonus:,}**"
    )


def load(bot: lightbulb.BotApp) -> None:
    bot.command(dice)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_command(dice)
