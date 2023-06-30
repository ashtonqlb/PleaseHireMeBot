from interactions import slash_command, slash_option, SlashContext, Extension, OptionType

def message():
    return slash_option(name="message", description="Add a message", required=False, opt_type=OptionType.STRING)

def eyes():
    return slash_option(name="eyes", description="Choose custom eyes", required=False, opt_type=OptionType.STRING)

def tongue():
    return slash_option(name="tongue", description="Choose a custom tongue", required=False, opt_type=OptionType.STRING)

class cow(Extension):
    @slash_command(name = "cow", description = "")
    async def cow(self, ctx: SlashContext):
        ctx.send()
    
    cow.subcommand(sub_cmd_name="say", sub_cmd_description="GNU cowsay")
    @message()
    @eyes()
    @tongue()
    
    async def cowsay(self, 
                     ctx: SlashContext, 
                     message ="moo",
                     eyes ="oo",
                     tongue = "__"
                     ):
        output = f"""```
        {message}
         \   ^__^
          \  ({eyes})\_______
             ({tongue})\       )\/
                 ||----w |
                 ||     ||```
        """.format(message=message)
        await ctx.respond(output)
        
    cow.subcommand(sub_cmd_name="think", sub_cmd_description="GNU cowthink")
    @message()
    @eyes()
    @tongue()
    
    async def cowthink(self, 
                       ctx: SlashContext, 
                       message ="moo",
                       eyes ="oo",
                       tongue = "__"
                       ):
        output = f"""```
        {message}
         \   ^__^
          \  ({eyes})\_______
             ({tongue})\       )\/
                 ||----w |
                 ||     ||```
        """.format(message=message)
        await ctx.respond(output)

def setup(bot):
    cow(bot)
    