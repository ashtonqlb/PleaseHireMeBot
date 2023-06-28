# PleaseHireMeBot: The world's first combined Discord bot and CV
# Proudly made *without* code-enhancing substances (Copilot, Kite, etc.)
# By Ashton Lunken

import os
import argparse
import logging
from interactions import Client, Intents, listen

parser = argparse.ArgumentParser(
    prog='PleaseHireMeBot', 
    description="World's first combined Discord bot and CV", 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

parser.add_argument('-v', '--verbose', action="store_true", help="enables verbose logging") 
args = parser.parse_args() # Get entered arguments

bot = Client(
    intents=Intents.DEFAULT, 
    sync_interactions=True, 
    asyncio_debug=True, 
    )

# @listen()
# async def setup_hook():

@listen()
async def on_ready():
    print(f"Ready!\nLogged in as {bot.user}")

logOutput = logging.FileHandler(filename='debug.log', encoding='utf-8', mode='w')

# @slash_command(name="cow", description="GNU cowsay")
print ("Loading extensions...")
for f in os.listdir("./extensions"):
    if f.endswith(".py"):
        bot.load_extension("extensions." + f[:-3])
        print(f"Loaded {f}")

file = open(file="tokens/discordToken.txt", mode="r+", encoding="utf-8")
token = file.read()
file.close() # Close the file after reading it

if args.verbose:
    print("Verbose logging enabled")
    bot.start(token)
else:
    bot.start(token)