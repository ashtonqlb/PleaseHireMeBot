# PleaseHireMeBot: The world's first combined Discord bot and CV
# Proudly made *without* code-enhancing substances (Copilot, Kite, etc.)
# By Ashton Lunken

import argparse
import random
import logging
import discord
import asyncio
from discord import app_commands
from characterai import PyAsyncCAI

parser = argparse.ArgumentParser(prog='PleaseHireMeBot', description="World's first combined Discord bot and CV", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v', '--verbose', action="store_true", help="enables verbose logging") 
args = parser.parse_args() # Get entered arguments

intents = discord.Intents.default() # Asking for default permissions on startup
intents.message_content = True      # as well as the ability to look for message contents
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client) # Add all commands to command tree

logOutput = logging.FileHandler(filename='debug.log', encoding='utf-8', mode='w')

file1 = open(file="tokens/discordToken.txt", mode="r+", encoding="utf-8")
discordToken = file1.read()
file1.close() # Close the file after reading it

file2 = open(file="tokens/caiToken.txt", mode="r+", encoding="utf-8")
caiToken = file2.read()
file2.close

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
    
@tree.command(name="flip", description="Flip a coin") #Feature reversion: you can only flip 1 coin at once, but I hope to eventually embed a nice little .gif for each flip later down the line
async def flip(interaction):
        await interaction.response.send_message("You flipped a coin and got: " + random.choice(["`Heads`", "`Tails`"]))

@tree.command(name="attributions", description="Who made this lovely lad?")
async def attributions(interaction):
    await interaction.response.send_message("**Made with malicious intent by Ashton Bennet**\nwith discord.py [https://github.com/Rapptz/discord.py/]\nand PyCAI [https://github.com/kramcat/CharacterAI]\n\n***You should hire me***\nhttps://www.linkedin.com/in/ashtonqlb/\nhttps://github.com/ashtonqlb")
            
@tree.command(name="hal", description="Talk to HAL9000")
async def hal(interaction, message: str):
    async def hal_backend():
        caiClient = PyAsyncCAI(caiToken)
        char = "bXFRSGkcr0gP3-udUZNWk-JvOr7nfemTFQAfxjUSFjM"
        chat = await caiClient.chat.get_chat(char)
        history_id = chat['external_id']
        participants = chat['participants']

        if not participants[0]['is_human']:
            tgt = participants[0]['user']['username']
        else:
            tgt = participants[1]['user']['username']

        while True:
            data = await caiClient.chat(char, message, history_external_id=history_id, tgt=tgt)

            name = data['src_char']['participant']['name']
            text = data['replies'][0]['text']

            response = f"**{name}:**  {text}"
            return response  # Return the response from hal_backend
    
    response = await asyncio.run(hal_backend())  # Store the response in a variable
    await interaction.response.send_message(response)  # Send the response in the message

# @tree.command(name="cow", description="GNU cowsay")

# @tree.command(name="fortune", description="GNU fortune")

@tree.command(name="fizzbuzz", description="Obligatory fizzbuzz")
async def fizzbuzz(interaction, ceil: int = 100):
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


if args.verbose:
    print("Verbose logging enabled")
    client.run(discordToken, log_handler=logOutput, log_level=logging.DEBUG)
else:
    client.run(discordToken, log_handler=logOutput, log_level=logging.INFO)