import datetime as dt

import hikari
import lightbulb

from typing import Union

# The options the command will have. This creates a required member
# option. Validation is handled for you -- Discord won't let you
# send the command unless it's a valid member. How cool is that?!
@lightbulb.option("target", "The member to get information about.", hikari.User)
# Disable the slash command from being visible & useable in DMs
@lightbulb.app_command_permissions(dm_enabled=False)
# Convert the function into a command
@lightbulb.command("userinfo", "Get info on a server member.", pass_options=True)
# Define the types of command that this function will implement
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def user_info(ctx: lightbulb.Context, target: Union[hikari.InteractionMember, hikari.Member, hikari.User]) -> None:
    # This slash command won't be available in DMs, but the
    # prefix command will be, so we do some validation
    if not ctx.guild_id:
        await ctx.respond("This command may only be user in servers.")
        return

    # Convert the option into a Member object if lightbulb couldn't resolve it automatically.
    # If an invalid user was passed as the target (with prefix command), lightbulb will raise
    # the lightbulb.ConverterFailure error. (This example does not handle this problem).
    member = (
        target
        if isinstance(target, (hikari.Member, hikari.InteractionMember))
        else ctx.bot.cache.get_member(ctx.guild_id, target)
    )
    if not member:
        await ctx.respond("That user is not in this server.")
        return

    created_at = int(member.created_at.timestamp())
    joined_at = int(member.joined_at.timestamp())

    # Create a list of roles, formatting them into role mentions.
    # The @everyone role's ID is the guild's ID, which we filter out.
    roles = [f"<@&{role}>" for role in member.role_ids if role != ctx.guild_id]

    # Function calls can be chained when creating embeds.
    embed = (
        hikari.Embed(
            title="User information",
            description=f"ID: `{member.id}`",
            colour=hikari.Colour(0x563275),
            # Doing it like this is important.
            timestamp=dt.datetime.now().astimezone(),
        )
        .set_author(name=str(member))
        .set_footer(
            text=f"Requested by {ctx.member.display_name}",
            icon=ctx.member.display_avatar_url,
        )
        .set_thumbnail(member.display_avatar_url)
        # These are just a number of example fields.
        .add_field(name="Discriminator", value=member.discriminator, inline=True)
        .add_field(name="Bot?", value=str(member.is_bot), inline=True)
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

    # To send a message, use ctx.respond. Using kwargs, you can make
    # the bot reply to a message (when not sent from a slash command
    # invocation), allow mentions, make the message ephemeral, etc.
    await ctx.respond(embed)


def load(bot: lightbulb.BotApp):
    bot.command(user_info)


def unload(bot: lightbulb.BotApp):
    bot.remove_command(user_info)
