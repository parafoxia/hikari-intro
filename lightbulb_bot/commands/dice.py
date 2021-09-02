import random
import typing as t

import hikari
import lightbulb
from lightbulb import slash_commands

from .. import GUILD_ID


# Create a slash command class. The name is automatically set to the
# lower case version of the class name.
class Dice(slash_commands.SlashCommand):
    # The help text for the command.
    description: str = "Roll one or more dice."
    # This sets what guilds the command is enabled in. If this is
    # None, the command is considered global, and can be used in
    # any guild. Otherwise, a list of guild IDs should be passed.
    enabled_guilds: t.Optional[t.Iterable[int]] = (GUILD_ID,)
    # The options the command will have.
    options: list[hikari.CommandOption] = [
        # This creates a required int option. Validation is handled
        # for you -- Discord won't let you send the command unless
        # it's a number. How cool is that?!
        hikari.CommandOption(
            name="number",
            description="The number of dice to roll.",
            type=hikari.OptionType.INTEGER,
            is_required=True,
        ),
        # These next two are the same, but are optional. We will
        # have to work out a default value later.
        hikari.CommandOption(
            name="sides",
            description="The number of sides each die will have.",
            type=hikari.OptionType.INTEGER,
            is_required=False,

        ),
        hikari.CommandOption(
            name="bonus",
            description="A fixed number to add to the total roll.",
            type=hikari.OptionType.INTEGER,
            is_required=False,
        ),
    ]

    async def callback(self, ctx) -> None:
        # Get the value from the required option.
        number = ctx.option_values.number
        # Get the value from the optional options, or set a default
        # value if none is available.
        sides = getattr(ctx.options.get("sides"), "value", 6)
        bonus = getattr(ctx.options.get("bonus"), "value", 0)

        if number > 25:
            await ctx.respond("No more than 25 dice can be rolled at once.")
            return

        if sides > 100:
            await ctx.respond("The dice cannot have more than 100 sides.")
            return

        rolls = [random.randint(1, sides) for _ in range(number)]

        # To send a message, use ctx.respond. Using kwargs, you can make the
        # bot reply to a message (when not send from a slash command
        # invocation), allow mentions, make the message ephemeral, etc.
        await ctx.respond(
            " + ".join(f"{r}" for r in rolls)
            + (f" + {bonus} (bonus)" if bonus else "")
            + f" = **{sum(rolls) + bonus:,}**"
        )


def load(bot: lightbulb.Bot):
    bot.add_slash_command(Dice)


def unload(bot: lightbulb.Bot):
    bot.remove_slash_command("dice")
