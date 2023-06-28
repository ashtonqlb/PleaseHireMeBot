import random
import re
from interactions import slash_command, SlashContext, Extension

class fortune(Extension):   
    def _read_fortunes(self, fortune_file):
        with open(fortune_file, mode='r', encoding='utf-8') as f:
            contents = f.read()

        lines = [line.rstrip() for line in contents.split('\n')]
        delim = re.compile(r'^%$')

        fortunes = []
        temp = []

        def add_to_list(buf):
            parsed_fortune = '\n'.join(buf)
            if parsed_fortune.strip():
                fortunes.append(parsed_fortune)

        for line in lines:
            if delim.match(line):
                add_to_list(temp)
                temp = []
                continue

            temp.append(line)

        if temp:
            add_to_list(temp)

        return fortunes
    
    @slash_command(name="fortune", description="GNU fortune")
    async def fortune(self, ctx: SlashContext):
        fortunes = list(self._read_fortunes("extensions/assets/fortune/fortunes2"))
        message = fortunes[random.randint(0, len(fortunes) - 1)]
        await ctx.send(message)
        
def setup(bot):
    fortune(bot)