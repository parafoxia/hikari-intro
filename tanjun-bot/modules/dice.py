import random

# import hikari  # You may need hikari if you extend this.
import tanjun

# Create the component. There's no need to subclass it like you would
# a cog in discord.py.
component = tanjun.Component()


# This sets up a slash command interface to work with.
@component.with_slash_command
# This creates a required int option. Validation is handled for you --
# Discord won't let you send the command unless it's a number. How cool
# is that?!
@tanjun.with_int_slash_option("number", "The number of dice to roll (max: 25).")
# These next two are the same, but are optional. Setting a default value
# automatically marks it as optional.
@tanjun.with_int_slash_option("sides", "The number of sides each die will have.", default=6)
@tanjun.with_int_slash_option("bonus", "A fixed number to add to the total roll.", default=0)
# This sets the name and help for the command.
@tanjun.as_slash_command("dice", "Roll one or more dice.")
async def command_dice(ctx: tanjun.abc.Context, number: int, sides: int, bonus: int) -> None:
    if number > 25:
        await ctx.respond("No more than 25 dice can be rolled at once.")
        return

    if sides > 100:
        await ctx.respond("The dice cannot have more than 100 sides.")
        return

    rolls = [random.randint(1, sides) for i in range(number)]

    # To send a message, use ctx.respond. Using kwargs, you can make the
    # bot reply to a message (when not send from a slash command
    # invocation), allow mentions, make the message ephemeral, etc.
    await ctx.respond(
        " + ".join(f"{r}" for r in rolls)
        + (f" + {bonus} (bonus)" if bonus else "")
        + f" = **{sum(rolls) + bonus:,}**"
    )


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    # This loads the component, and is necessary in EVERY module,
    # otherwise you'll get an error.
    client.add_component(component.copy())
