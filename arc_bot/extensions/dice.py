import random

import arc

plugin = arc.GatewayPlugin("dice")


@plugin.include
@arc.slash_command("dice", "Roll some dice.")
async def dice(
    ctx: arc.GatewayContext,
    # The `arc.Option` annotation creates a required int option.
    # Validation is handled for you -- Discord won't let you send
    # the command unless it's a number. How cool is that?!
    number: arc.Option[int, arc.IntParams("The number of dice to roll.", min=1, max=25)],
    # These two are the same type, but are optional. We can provide a
    # default value using the usual Python syntax.
    sides: arc.Option[int, arc.IntParams("The number of sides each die will have.", min=0, max=100)] = 6,
    bonus: arc.Option[int, arc.IntParams("A fixed number to add to the total roll.", min=0)] = 0,
) -> None:
    rolls = [random.randint(1, sides) for _ in range(number)]

    # To send a message, use ctx.respond.
    await ctx.respond(
        " + ".join(f"{r}" for r in rolls) + (f" + {bonus} (bonus)" if bonus else "") + f" = **{sum(rolls) + bonus:,}**"
    )


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)


@arc.unloader
def unload(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
