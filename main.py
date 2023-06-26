# PleaseHireMeBot: The world's first combined Discord bot and CV

import argparse
import random
import logging
import discord
from discord import app_commands
from characterai import PyAsyncCAI

parser = argparse.ArgumentParser(prog='PleaseHireMeBot', description="World's first combined Discord bot and CV", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-r', '--refresh', action="store_true", help="reannounce slash commands to Discord")
parser.add_argument('-v', '--verbose', action="store_true", help="enables verbose logging") 

args = parser.parse_args() # Get entered arguments
logOutput = logging.FileHandler(filename='debug.log', encoding='utf-8', mode='w')

intents = discord.Intents.default() # Asking for default permissions on startup
intents.message_content = True      # as well as the ability to look for message contents
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

@tree.command(name = "ping", description = "Ping the bot.")
async def ping(interaction):
    await interaction.response.send_message("Pong!")
    
@tree.command(name = "roll", description = "Roll a 1d20")
async def roll(interaction):
    await interaction.response.send_message("You rolled a 1d20 and got: " + str(random.randint(1, 20)))

@tree.command(name="flip", description="Flip a coin")
async def flip(interaction):
    await interaction.response.send_message("You flipped a coin and got: " + random.choice(["Heads", "Tails"]))

@tree.command(name="attributions", description="Who made this lovely lad?")
async def attributions(interaction):
    await interaction.response.send_message("**Made with malicious intent by Ashton Bennet**\nwith discord.py [https://github.com/Rapptz/discord.py/]\nand PyCAI [https://github.com/kramcat/CharacterAI]\n\n***You should hire me***\nhttps://www.linkedin.com/in/ashtonqlb/\nhttps://github.com/ashtonqlb")
            
file1 = open(file="tokens/discordToken.txt", mode="r+", encoding="utf-8")
discordToken = file1.read()
file1.close() # Close the file after reading it

if args.verbose:
    print("Verbose logging enabled")
    client.run(discordToken, log_handler=logOutput, log_level=logging.DEBUG)
else:
    client.run(discordToken, log_handler=logOutput, log_level=logging.INFO)