import datetime as dt

import hikari
import tanjun

# Create the component. There's no need to subclass it like you would
# a cog in discord.py.
component = tanjun.Component()


# This sets up a slash command interface to work with.
@component.with_slash_command
# This creates a required member option. Validation is handled for you
# -- Discord won't let you send the command unless it's a valid member.
# How cool is that?!
@tanjun.with_member_slash_option("target", "The member to get information about.")
# This sets the name and help for the command.
@tanjun.as_slash_command("userinfo", "Get info on a server member.")
async def command_userinfo(ctx: tanjun.abc.Context, target: hikari.Member) -> None:
    created_at = int(target.created_at.timestamp())
    joined_at = int(target.joined_at.timestamp())
    roles = (await target.fetch_roles())[1:]  # All but @everyone.

    # Function calls can be chained when creating embeds.
    embed = (
        hikari.Embed(
            title="User information",
            description=f"ID: {target.id}",
            colour=hikari.Colour(0x563275),
            # Doing it like this is important.
            timestamp=dt.datetime.now().astimezone(),
        )
        .set_author(name="Information")
        .set_footer(
            text=f"Requested by {ctx.member.display_name}",
            icon=ctx.member.avatar_url,
        )
        .set_thumbnail(target.avatar_url)
        # These are just a number of example fields.
        .add_field(name="Discriminator", value=target.discriminator, inline=True)
        .add_field(name="Bot?", value=target.is_bot, inline=True)
        .add_field(name="No. of roles", value=len(roles), inline=True)
        .add_field(
            name="Created on",
            value=f"<t:{created_at}:d> (<t:{created_at}:R>)",
            inline=False,
        )
        .add_field(
            name="Joined on",
            value=f"<t:{joined_at}:d> (<t:{joined_at}:R>)",
            inline=False,
        )
        .add_field(name="Roles", value=" | ".join(r.mention for r in roles))
    )

    # To send a message, use ctx.respond. Using kwargs, you can make the
    # bot reply to a message (when not send from a slash command
    # invocation), allow mentions, make the message ephemeral, etc.
    await ctx.respond(embed)


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    # This loads the component, and is necessary in EVERY module,
    # otherwise you'll get an error.
    client.add_component(component.copy())
