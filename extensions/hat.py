import os
import requests
import ffmpeg
from interactions import slash_command, SlashContext, Extension


class hat(Extension):
    @slash_command(name="hat", description="Add a party hat to your avatar")
    async def hat(self, ctx: SlashContext):
        avi = requests.get(ctx.author.avatar_url, timeout=10)
        og_filepath = "extensions/assets/hat/temp/" + str(ctx.author_id) + ".png"
        edit_filepath = "extensions/assets/hat/temp/hat-" + str(ctx.author_id) + ".png"
        
        open(og_filepath, "wb").write(avi.content)
        
        def add_hat(filepath):
            return (
                ffmpeg
                .input(filepath)
                .overlay("extensions/assets/hat/hat.png", x=0, y=0)
                .output(edit_filepath)
                .run()
            )
            
        add_hat(og_filepath)
    
        await ctx.send(ctx.author.avatar_url)
        os.remove(og_filepath)
        os.remove(edit_filepath)

def setup(bot):
    hat(bot)
