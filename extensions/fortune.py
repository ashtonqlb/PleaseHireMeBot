import random
import re
from interactions import slash_command, SlashContext, Extension


class fortune(Extension):
    def readFortunes(self, fortune_file):
        with open(fortune_file, mode="r", encoding="utf-8") as f:
            contents = f.read()

        lines = [line.rstrip() for line in contents.split("\n")]
        delimiter = re.compile(r"^%$")

        fortunes = []
        temp = []

        def add(buf):
            parsed_fortune = "\n".join(buf)
            if parsed_fortune.strip():
                fortunes.append(parsed_fortune)

        for line in lines:
            if delimiter.match(line):
                add(temp)
                temp = []
                continue

            temp.append(line)

        if temp:
            add(temp)

        return fortunes

    @slash_command(name="fortune", description="GNU fortune")
    async def fortune(self, ctx: SlashContext):
        fortunes = list(self.readFortunes("extensions/assets/fortune/fortunes2"))
        message = fortunes[random.randint(0, len(fortunes) - 1)]
        await ctx.send(message)


def setup(bot):
    fortune(bot)
