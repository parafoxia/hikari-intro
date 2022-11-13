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
@tanjun.as_slash_command("userinfo", "Get info on a server member.", dm_enabled=False)
async def command_userinfo(ctx: tanjun.abc.Context, target: hikari.InteractionMember) -> None:
    created_at = int(target.created_at.timestamp())
    joined_at = int(target.joined_at.timestamp())

    # Create a list of roles, formatting them into role mentions.
    # The @everyone role's ID is the guild's ID, which we filter out.
    roles = [f"<@&{role}>" for role in target.role_ids if role != ctx.guild_id]

    # Function calls can be chained when creating embeds.
    embed = (
        hikari.Embed(
            title="User information",
            description=f"ID: `{target.id}`",
            colour=hikari.Colour(0x563275),
            # Doing it like this is important.
            timestamp=dt.datetime.now().astimezone(),
        )
        .set_author(name=str(target))
        .set_footer(
            text=f"Requested by {ctx.member.display_name}",
            icon=ctx.member.display_avatar_url,
        )
        .set_thumbnail(target.display_avatar_url)
        # These are just a number of example fields.
        .add_field(name="Discriminator", value=target.discriminator, inline=True)
        .add_field(name="Bot?", value=str(target.is_bot), inline=True)
        .add_field(name="No. of roles", value=str(len(roles)), inline=True)
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
        .add_field(name="Roles", value=" | ".join(roles) if roles else "No roles")
    )

    # To send a message, use ctx.respond. Using kwargs, you can make the
    # bot reply to a message (when not sent from a slash command
    # invocation), allow mentions, make the message ephemeral, etc.
    await ctx.respond(embed)


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    # This loads the component, and is necessary in EVERY module,
    # otherwise you'll get an error.
    client.add_component(component.copy())
