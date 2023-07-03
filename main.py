# PleaseHireMeBot: The world's first combined Discord bot and CV
# Proudly made *without* code-enhancing substances (Copilot, Kite, etc.)
# By Ashton Lunken

# TODO: Fix memory leak in /hal command by ending the coroutine. I need to read the documentation to get a better understanding of how that works.

import os
import argparse
import logging
from interactions import Client, Intents, listen

parser = argparse.ArgumentParser(
    prog="PleaseHireMeBot",
    description="World's first combined Discord bot and CV",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
    "-v", "--verbose", action="store_true", help="enables verbose logging"
)
parser.add_argument(
    "-s", "--silent", action="store_true", help="disables all console output"
)
args = parser.parse_args()  # Get entered arguments

logging.basicConfig(filename="debug.log", filemode="w")
debug_log = logging.getLogger("PleaseHireMeBot")
if args.silent is False:
    if args.verbose:
        debug_log.setLevel(logging.DEBUG)
    else:
        debug_log.setLevel(logging.INFO)


bot = Client(
    intents=Intents.DEFAULT,
    sync_interactions=True,
    asyncio_debug=True,
    logger=debug_log,
)


@listen()
async def on_ready():
    print(f"Ready!\nLogged in as {bot.user}")


# @slash_command(name="cow", description="GNU cowsay")
print("Loading extensions...")
for f in os.listdir("./extensions"):
    if f.endswith(".py"):
        bot.load_extension("extensions." + f[:-3])
        print(f"Loaded {f}")

file = open(file="tokens/discordToken.txt", mode="r", encoding="utf-8")
token = file.read()
file.close()  # Close the file after reading it

bot.start(token)
