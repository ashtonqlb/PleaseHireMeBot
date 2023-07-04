import os
import requests
import ffmpeg
from interactions import slash_command, SlashContext, Extension, File


class hat(Extension):
    @slash_command(name="hat", description="Add a party hat to your avatar")
    async def hat(self, ctx: SlashContext):
        avi = requests.get(ctx.author.avatar_url, timeout=10)
        og_filepath = "extensions/assets/hat/temp/" + str(ctx.author_id) + ".png"
        edit_filepath = "extensions/assets/hat/temp/hat-" + str(ctx.author_id) + ".png"
        
        open(og_filepath, "wb").write(avi.content)
        
        stream = ffmpeg.input(og_filepath)
        overlay = ffmpeg.input("extensions/assets/hat/hat.gif")
        
        stream = ffmpeg.overlay(stream, overlay, x=-5, y=-5)
        stream = ffmpeg.output(stream, edit_filepath)
        ffmpeg.run(stream, overwrite_output=True)
                        
        await ctx.send(file=File(filename=edit_filepath, file_type="image/png"))
        os.remove(og_filepath)
        os.remove(edit_filepath)

def setup(bot):
    hat(bot)
