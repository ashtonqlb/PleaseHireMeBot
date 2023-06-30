from interactions import (
    slash_command,
    slash_option,
    OptionType,
    SlashContext,
    Extension,
)


class fizzbuzz(Extension):
    @slash_command(name="fizzbuzz", description="Obligatory fizzbuzz")
    @slash_option(
        name="ceil",
        description="How high to count",
        required=False,
        opt_type=OptionType.INTEGER,
    )
    async def fizzbuzz(self, ctx: SlashContext, ceil: int = 100):
        result = []

        if ceil + 1 > 101:
            await ctx.send("You can't fizzbuzz more than 100 numbers at once!")
            return

        for i in range(1, ceil + 1):
            if i % 15 == 0:
                result.append("FizzBuzz, ")
            elif i % 3 == 0:
                result.append("Fizz, ")
            elif i % 5 == 0:
                result.append("Buzz, ")
            else:
                result.append(str(i) + ", ")
        await ctx.send("".join(result))
