from interactions import (
    slash_command,
    slash_option,
    SlashContext,
    Extension,
    OptionType,
)
def message_function():
    def wrapper(func):
        return slash_option(
                name="message",
                description="Add a message",
                required=False,
                opt_type=OptionType.STRING
                )(func)
    return wrapper

def eyes_function():
    def wrapper(func):
        return slash_option(
                name="eyes",
                description="Choose custom eyes",
                required=False,
                opt_type=OptionType.STRING
                )(func)
    return wrapper

def tongue_function():
    def wrapper(func):
        return slash_option(
                name="tongue",
                description="Choose a custom tongue",
                required=False,
                opt_type=OptionType.STRING
                )(func)
    return wrapper

class Cow(Extension):
    @slash_command(name="cow", description="")
    async def cow(self, ctx: SlashContext):
        await ctx.send("Use the subcommands `say` or `think`")
          
    @cow.subcommand(sub_cmd_name="say", sub_cmd_description="GNU cowsay")      
    @message_function()
    @eyes_function()
    @tongue_function()
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


    @cow.subcommand(sub_cmd_name="think", sub_cmd_description="GNU cowthink")
    @message_function()
    @eyes_function()
    @tongue_function()    
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
    Cow(bot)
       