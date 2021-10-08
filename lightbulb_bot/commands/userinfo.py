import datetime as dt
import typing as t

import hikari
import lightbulb
from lightbulb import slash_commands

from .. import GUILD_ID


# Create a slash command class. The name is automatically set to the
# lower case version of the class name.
class Userinfo(slash_commands.SlashCommand):
    # The help text for the command.
    description: str = "Get info on a server member."
    # This sets what guilds the command is enabled in. If this is
    # not defined or is None, the command is considered global, and can
    # be used in any guild. Otherwise, a list of guild IDs should be
    # passed.
    enabled_guilds: t.Optional[t.Iterable[int]] = (GUILD_ID,)
    # The options the command will have. This creates a required member
    # option. Validation is handled for you -- Discord won't let you
    # send the command unless it's a valid member. How cool is that?!
    target: hikari.User = slash_commands.Option("The member to get information about.")

    async def callback(self, ctx: slash_commands.SlashCommandContext) -> None:
        # Convert the Snowflake value to a Member object.
        target = ctx.get_guild().get_member(ctx.options.target)
        if not target:
            await ctx.respond("That user is not in the server.")
            return

        created_at = int(target.created_at.timestamp())
        print(created_at)
        joined_at = int(target.joined_at.timestamp())
        print(joined_at)
        roles = (await target.fetch_roles())[1:]  # All but @everyone.
        print(roles)

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
            .add_field(name="No. of roles", value=len(roles) - 1, inline=True)
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

        # To send a message, use ctx.respond. Using kwargs, you can make
        # the bot reply to a message (when not sent from a slash command
        # invocation), allow mentions, make the message ephemeral, etc.
        await ctx.respond(embed)


def load(bot: lightbulb.Bot):
    bot.add_slash_command(Userinfo)


def unload(bot: lightbulb.Bot):
    bot.remove_slash_command("userinfo")
