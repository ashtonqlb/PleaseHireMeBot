from interactions import slash_command, SlashContext, Extension


class ping(Extension):
    @slash_command(name="ping", description="Ping the bot.")
    async def ping(self, ctx: SlashContext):
        await ctx.send("Pong!")


def setup(bot):
    ping(bot)
