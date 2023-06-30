from interactions import (
    slash_command,
    slash_option,
    SlashContext,
    Extension,
    OptionType,
)

def msg_option():
    return slash_option(
        name="message",
        description="Add a message",
        required=False,
        opt_type=OptionType.STRING,
    )


def eyes_option():
    return slash_option(
        name="eyes",
        description="Choose custom eyes",
        required=False,
        opt_type=OptionType.STRING,
    )


def tongue_option():
    return slash_option(
        name="tongue",
        description="Choose a custom tongue",
        required=False,
        opt_type=OptionType.STRING,
    )


class cow(Extension):
    @slash_command(name="cow", description="")
    async def cow(self, ctx: SlashContext):
        await ctx.send("Use the subcommands `say` or `think`")

    cow.subcommand(sub_cmd_name="say", sub_cmd_description="GNU cowsay") # WHY. WHAT ARE YOU DOING. THIS IS JUST LIKE THE DOCUMENTATION. WHAT IS YOUR MAJOR MALFUNCTION.

    @msg_option()
    @eyes_option()
    @tongue_option()
    async def cowsay(self, ctx: SlashContext, message="moo", eyes="oo", tongue="__"):
        output = rf"""```
        {message}
         \   ^__^
          \  ({eyes})\_______
             ({tongue})\       )\/
                 ||----w |
                 ||     ||```
        """.format(
            message=message
        )
        await ctx.respond(output)

    cow.subcommand(sub_cmd_name="think", sub_cmd_description="GNU cowthink")

    @msg_option()
    @eyes_option()
    @tongue_option()
    async def cowthink(self, ctx: SlashContext, message="moo", eyes="oo", tongue="__"):
        output = rf"""```
        {message}
         \   ^__^
          \  ({eyes})\_______
             ({tongue})\       )\/
                 ||----w |
                 ||     ||```
        """.format(
            message=message
        )
        await ctx.respond(output)

def setup(bot):
    cow(bot)
       