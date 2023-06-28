from interactions import slash_command, SlashContext, Extension

class attributions(Extension):
    @slash_command(name="attributions", description="Who made this lovely lad?")
    async def attributions(self, ctx: SlashContext):
        await ctx.send("**Made with malicious intent by Ashton Bennet**\nwith interactions.py [https://github.com/interactions-py/interactions.py]\nand PyCAI [https://github.com/kramcat/CharacterAI]\n\n***You should hire me***\nhttps://www.linkedin.com/in/ashtonqlb/\nhttps://github.com/ashtonqlb")

def setup(bot):
    attributions(bot)