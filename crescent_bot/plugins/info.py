import datetime as dt

import hikari
import crescent

plugin = crescent.Plugin()


@plugin.include
# This command is disabled in dms because we want the user to choose member.
@crescent.command(name="user-info", dm_enabled=False)
class UserInfo:
    # The options the command will have. This creates a required member
    # option.
    target = crescent.option(
        hikari.User, "The member to get the information about."
    )

    async def callback(self, ctx: crescent.Context):
        # If a user uses a user id, they can select a user that isn't
        # in the guild.
        if not isinstance(self.target, hikari.Member):
            await ctx.respond("That user is not in the server.")
            return

        created_at = int(self.target.created_at.timestamp())
        joined_at = int(self.target.joined_at.timestamp())
        roles = (await self.target.fetch_roles())[1:]  # All but @everyone.

        # Function calls can be chained when creating embeds.
        embed = (
            hikari.Embed(
                title="User information",
                description=f"ID: {self.target.id}",
                colour=hikari.Colour(0x563275),
                # Doing it like this is important.
                timestamp=dt.datetime.now().astimezone(),
            )
            .set_author(name="Information")
            .set_footer(
                text=f"Requested by {ctx.member.display_name}",
                icon=ctx.member.avatar_url,
            )
            .set_thumbnail(self.target.avatar_url)
            # These are just a number of example fields.
            .add_field(name="Discriminator", value=self.target.discriminator, inline=True)
            .add_field(name="Bot?", value=self.target.is_bot, inline=True)
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

        # To send a message, use ctx.respond. Using kwargs, you can make
        # the bot reply to a message (when not sent from a slash command
        # invocation), allow mentions, make the message ephemeral, etc.
        await ctx.respond(embed=embed)
