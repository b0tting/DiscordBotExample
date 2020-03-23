# bot.py
import configparser
import re
import discord
import emoji
import json
import random

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.search("ak?47", message.content.lower()):
        await message.channel.send(file=discord.File("resources/guncat.gif"))
    elif "poopie" in message.content.lower():
        await message.channel.send(emoji.emojize(':poop:'))
    elif "corona" in message.content.lower():
        await message.channel.send(file=discord.File("resources/corona.jpg"))
    elif "grap" in message.content.lower():
        with open('resources/moppen.json', 'r', encoding="utf8") as f:
            allemoppen = json.load(f)
            jokes = allemoppen["jokes"]
            await message.channel.send(random.choice(jokes))


config = configparser.ConfigParser()
config.read('config.ini')
client.run(config["discord"]["token"])
# Code here never runs, CTRL-C to quit
