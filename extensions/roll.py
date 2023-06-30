import random
from interactions import (
    slash_command,
    slash_option,
    SlashContext,
    Extension,
    OptionType,
)


class roll(Extension):
    @slash_command(name="roll", description="Roll a dice. (1d6 by default)")
    @slash_option(
        name="dice",
        description="How many dice to roll.",
        required=False,
        opt_type=OptionType.INTEGER,
    )
    @slash_option(
        name="sides",
        description="How many sides the dice should have.",
        required=False,
        opt_type=OptionType.INTEGER,
    )
    async def roll(self, ctx: SlashContext, dice: int = 1, sides: int = 6):
        results = []  # Initialize an empty list for storing the dice roll results
        total = 0  # Initialize the total to zero

        if dice > 100:
            await ctx.send("You can't roll more than 100 dice at once!")
            return
        elif dice < 1:
            await ctx.send("You can't roll without dice!")

        if sides > 100:
            await ctx.send("You can't roll a dice with more than 100 sides!")
            return
        elif sides < 2:
            await ctx.send("You can't roll a dice with less than 2 sides!")
            return

        for i in range(dice):
            roll_result = random.randint(1, sides)  # Generate a random dice roll
            results.append(roll_result)  # Add the roll result to the list
            total += roll_result  # Add the roll result to the total

        if dice == 1:
            await ctx.send(f"You rolled a `{dice}d{sides}` and got: `{total}`")
        else:
            results_string = ", ".join(str(result) for result in results)
            await ctx.send(
                f"You rolled `{dice}d{sides}` and got: `{total}`.\nResults: `{results_string}`"
            )


def setup(bot):
    roll(bot)
