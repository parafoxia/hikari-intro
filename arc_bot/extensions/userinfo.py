import arc
import hikari

plugin = arc.GatewayPlugin("userinfo")


@plugin.include
@arc.slash_command("userinfo", "Get info on a server member.", is_dm_enabled=False)
async def user_info(
    ctx: arc.GatewayContext,
    # The options the command will have. This creates a required user
    # option. Validation is handled for you -- Discord won't let you
    # send the command unless it's a valid user. How cool is that?!
    target: arc.Option[hikari.User, arc.UserParams("The member to get information about.")],
) -> None:
    # If the user is not a member, we can't access guild-specific information.
    if not isinstance(target, hikari.Member):
        await ctx.respond("This command can only be used on a server member.", flags=hikari.MessageFlag.EPHEMERAL)
        return

    created_at = int(target.created_at.timestamp())
    joined_at = int(target.joined_at.timestamp())
    roles = target.get_roles()

    # Function calls can be chained when creating embeds.
    embed = (
        hikari.Embed(title="User information", description=f"ID: {target.id}", colour=hikari.Colour(0x563275))
        .set_author(name="Information")
        .set_footer(text=f"Requested by {ctx.author.username}", icon=ctx.author.avatar_url)
        .set_thumbnail(target.avatar_url)
        # These are just a number of example fields.
        .add_field(name="Bot?", value=str(target.is_bot), inline=True)
        .add_field(name="No. of roles", value=str(len(roles)), inline=True)
        .add_field(name="Created on", value=f"<t:{created_at}:d> (<t:{created_at}:R>)", inline=False)
        .add_field(name="Joined on", value=f"<t:{joined_at}:d> (<t:{joined_at}:R>)", inline=False)
        .add_field(name="Roles", value=" | ".join(r.mention for r in roles))
    )

    # To send a response, use ctx.respond.
    await ctx.respond(embed=embed)


@arc.loader
def load(client: arc.GatewayClient):
    client.add_plugin(plugin)


@arc.unloader
def unload(client: arc.GatewayClient):
    client.remove_plugin(plugin)
