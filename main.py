# PleaseHireMeBot: The world's first combined Discord bot and CV
# Proudly made *without* code-enhancing substances (Copilot, Kite, etc.)
# By Ashton Lunken

import argparse
import random
import logging
import discord
from typing import List
from discord.ext import commands
from discord import app_commands
from characterai import PyAsyncCAI

parser = argparse.ArgumentParser(prog='PleaseHireMeBot', description="World's first combined Discord bot and CV", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v', '--verbose', action="store_true", help="enables verbose logging") 

args = parser.parse_args() # Get entered arguments
logOutput = logging.FileHandler(filename='debug.log', encoding='utf-8', mode='w')

intents = discord.Intents.default() # Asking for default permissions on startup
intents.message_content = True      # as well as the ability to look for message contents
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client) # Add all commands to command tree

@client.event
async def on_ready():
    await tree.sync()
    print(f'{client.user} is online')

@tree.command(name = "ping", description = "Ping the bot.")
async def ping(interaction):
    await interaction.response.send_message("Pong!")

@tree.command(name = "roll", description = "Roll a dice. (1d6 by default)")  
async def roll(interaction, dice: int = 1, sides: int = 6):
    results = []  # Initialize an empty list for storing the dice roll results
    total = 0     # Initialize the total to zero
    
    if dice > 100:
        await interaction.response.send_message("You can't roll more than 100 dice at once!")
        return
    elif dice < 1:
        await interaction.response.send_message("You can't roll without dice!")
    
    if sides > 100:
        await interaction.response.send_message("You can't roll a dice with more than 100 sides!")
        return
    elif sides < 2:
        await interaction.response.send_message("You can't roll a dice with less than 2 sides!")
        return

    for i in range(dice):
        roll_result = random.randint(1, sides)  # Generate a random dice roll
        results.append(roll_result)             # Add the roll result to the list
        total += roll_result                    # Add the roll result to the total

    if dice == 1:
        await interaction.response.send_message(f"You rolled a `{dice}d{sides}` and got: `{total}`")
    else:
        results_string = ", ".join(str(result) for result in results)
        await interaction.response.send_message(
            f"You rolled `{dice}d{sides}` and got: `{total}`.\nResults: `{results_string}`"
        )
    
@tree.command(name="flip", description="Flip a coin") #TODO: Fix text formatting bug when flipping more than 1 coin
async def flip(interaction, times_to_flip: int = 1):
    
    results = []
    
    if times_to_flip > 10:
        await interaction.response.send_message("You can't flip more than 10 coins at once!")
        return
    
    if times_to_flip == 1:
        await interaction.response.send_message("You flipped a coin and got: " + random.choice(["Heads", "Tails"]))
    else:
        for i in range(times_to_flip):
            results.append(random.choice(["Heads", "Tails"]) + ",")
        await interaction.response.send_message("You flipped `" + str(times_to_flip) + "` coins and got: " + "".join(results))

@tree.command(name="attributions", description="Who made this lovely lad?")
async def attributions(interaction):
    await interaction.response.send_message("**Made with malicious intent by Ashton Bennet**\nwith discord.py [https://github.com/Rapptz/discord.py/]\nand PyCAI [https://github.com/kramcat/CharacterAI]\n\n***You should hire me***\nhttps://www.linkedin.com/in/ashtonqlb/\nhttps://github.com/ashtonqlb")
            
# @tree.command(name="hal", description="Talk to HAL9000")

# @tree.command(name="cow", description="GNU cowsay")

# @tree.command(name="fortune", description="GNU fortune")

@tree.command(name="fizzbuzz", description="Obligatory fizzbuzz")
async def fizzbuzz(interaction, ceil: int):
    result = []
    
    if ceil + 1 > 101:
        await interaction.response.send_message("You can't fizzbuzz more than 100 numbers at once!")
        return
    
    for i in range(1, ceil + 1):
        if i % 15 == 0:
            result.append("FizzBuzz, ")
        elif i % 3 == 0:
            result.append("Fizz, ")
        elif i % 5 == 0:
            result.append("Buzz, ")
        else:
            result.append(str(i) + ", ")
    await interaction.response.send_message("".join(result))

file1 = open(file="tokens/discordToken.txt", mode="r+", encoding="utf-8")
discordToken = file1.read()
file1.close() # Close the file after reading it

if args.verbose:
    print("Verbose logging enabled")
    client.run(discordToken, log_handler=logOutput, log_level=logging.DEBUG)
else:
    client.run(discordToken, log_handler=logOutput, log_level=logging.INFO)