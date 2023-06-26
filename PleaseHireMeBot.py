# PleaseHireMeBot: The world's first combined Discord bot and CV

import argparse
import logging
import discord
from discord import app_commands
from characterai import PyAsyncCAI

# parser = argparse.ArgumentParser(prog='PleaseHireMeBot', description="World's first combined Discord bot and CV", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.add_argument('-r', '--refresh', action="store_true") #redefine global commands
# parser.add_argument('-v', '--verbose', action="store_true") #enable debug logging

# args = parser.parse_args() # Get entered arguments
logOutput = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default() # Asking for default permissions on startup
intents.message_content = True      # as well as the ability to look for message contents
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync() # Reannounces commands to Discord. Set this to a flag eventually
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
@tree.command(name = "commandname", description = "My first application Command")
async def first_command(interaction):
    await interaction.response.send_message("Hello!")
            
f = open(file="secret.txt", mode="r+", encoding="utf-8") # This file contains your discord API key and nothing else. For obvious reasons, I have not included it in the program itself
client.run(token = f.read(), log_handler=logOutput, log_level=logging.DEBUG) # Execute the program. TODO: MAKE IT SO THAT YOU CAN TOGGLE LOG LEVEL BASED ON ARGUMENTS PASSED IN