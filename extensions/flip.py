import random
from interactions import slash_command, SlashContext, Extension


class flip(Extension):
    @slash_command(
        name="flip", description="Flip a coin"
    )  # Feature reversion: you can only flip 1 coin at once, but I hope to eventually embed a nice little .gif for each flip later down the line
    async def flip(self, ctx: SlashContext):
        await ctx.send(
            "You flipped a coin and got: " + random.choice(["`Heads`", "`Tails`"])
        )


def setup(bot):
    flip(bot)
