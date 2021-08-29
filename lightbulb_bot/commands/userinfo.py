import datetime as dt
import random
import typing as t

import hikari
# import lightbulb  # You may need lightbulb if you extend this.
from lightbulb import slash_commands

from .. import GUILD_ID


# Create a slash command class. The name is automatically set to the
# lower case version of the class name.
class Userinfo(slash_commands.SlashCommand):
    @property
    def options(self) -> list[hikari.CommandOption]:
        # The options the command will have.
        return [
            # This creates a required member option. Validation is
            # handled for you -- Discord won't let you send the command
            # unless it's a valid member. How cool is that?!
            hikari.CommandOption(
                name="target",
                description="The member to get information about.",
                type=hikari.OptionType.USER,
                is_required=True,
            ),
        ]

    @property
    def description(self) -> str:
        # The help text for the command.
        return "Get info on a server member."

    @property
    def enabled_guilds(self) -> t.Optional[t.Iterable[int]]:
        # This sets what guilds the command is enabled in. If this is
        # None, the command is considered global, and can be used in
        # any guild. Otherwise, a list of guild IDs should be passed.
        return (GUILD_ID,)

    async def callback(self, ctx) -> None:
        # Convert the return value to a Member object.
        target = ctx.guild.get_member(int(ctx.options["target"].value))
        if not target:
            await ctx.respond("That user is not in the server.")
            return

        created_at = int(target.created_at.timestamp())
        joined_at = int(target.joined_at.timestamp())
        roles = (await target.fetch_roles())[1:]  # All but @everyone.

        # Function calls can be chained when creating embeds.
        embed = (
            hikari.Embed(
                title="User information",
                description=f"ID: {target.id}",
                # This is what happens when you let a Canadian build a lib d:
                color=hikari.Colour(0x563275),
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
                inline=False
            )
            .add_field(
                name="Joined on",
                value=f"<t:{joined_at}:d> (<t:{joined_at}:R>)",
                inline=False
            )
            .add_field(name="Roles", value=" | ".join(r.mention for r in roles))
        )

        # To send a message, use ctx.respond. Using kwargs, you can make the
        # bot reply to a message (when not send from a slash command
        # invocation), allow mentions, make the message ephemeral, etc.
        await ctx.respond(embed)
