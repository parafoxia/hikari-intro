import random

import crescent

plugin = crescent.Plugin()


@plugin.include
@crescent.command(name="dice")
class Dice:
    # The options the command will have are attributes on the class.

    # The `crescent.option` function creates a required int option.
    # Validation is handled for you -- Discord won't let you send
    # the command unless it's a number. How cool is that?!
    number = crescent.option(int, "The number of dice to roll.")

    # These two are the same type, but are optional. We can provide a
    # default value simply by using the `default` kwarg.
    sides = crescent.option(
        int, "The number of sides each die will have.", default=6
    )
    bonus = crescent.option(
        int, "A fixed number to add to the total roll.", default=0
    )

    async def callback(self, ctx: crescent.Context):
        # Option validation
        if self.number > 25:
            await ctx.respond("No more than 25 dice can be rolled at once.")
            return

        if self.sides > 100:
            await ctx.respond("The dice cannot have more than 100 sides.")
            return

        rolls = [random.randint(1, self.sides) for _ in range(self.number)]

        # To send a message, use ctx.respond. Using kwargs, you can make the
        # bot reply to a message (when not sent from a slash command
        # invocation), allow mentions, make the message ephemeral, etc.
        await ctx.respond(
            " + ".join(f"{r}" for r in rolls)
            + (f" + {self.bonus} (bonus)" if self.bonus else "")
            + f" = **{sum(rolls) + self.bonus:,}**"
        )
