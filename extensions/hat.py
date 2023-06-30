import os
import ffmpeg
from interactions import slash_command, SlashContext, Extension, Embed


class hat(Extension):
    @slash_command(name="hat", description="Add a party hat to your avatar")
    async def hat(self, ctx: SlashContext):
        avi = ctx.author.avatar.save("extensions/assets/temp/")

        open(f"extensions/assets/temp/{avi}", "wb").write(avi.content)
        (  # Overlay the hat
            ffmpeg.input(f"extensions/assets/temp/{avi}")
            .input("extensions/assets/hat.gif")
            .overlay(x=0, y=0)
            .output(f"extensions/assets/temp/hat-{avi}")
            .run()
        )
        os.remove(f"extensions/assets/temp/{avi}")
        await ctx.send(embed=Embed(f"extensions/assets/temp/hat-{avi}"))
        os.remove(f"extensions/assets/temp/hat-{avi}")


def setup(bot):
    hat(bot)
