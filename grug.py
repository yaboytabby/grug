import discord
import random
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'MTIwMzU0MzkyOTQ5MzAwNDQzMQ.GWM0z3.hBJhqCldTCqkr52HlN_LOpT0O4wnhEzFAC8jVM'

intents = discord.Intents.default()
intents.messages = True  # This is required to receive on_message events

bot = commands.Bot(command_prefix='!', intents=intents)

# List of random quotes
quotes = [
    "Raggshdfgs",
    "globor",
    "garglesdfvswet",
    "IN A MINUTE",
    "https://tenor.com/view/croods-in-a-minute-gif-16651642220079722751",
    "I'm off to work!",
    "sgrgjwrogjeoirg",
    "gwegje9rgp8ues98dfju",
    
"As a machine learning model developed by OpenAI, I don't have personal opinions. However, if you have a specific topic or question in mind, feel free to ask, and I'll do my best to provide information or assistance based on the data I've been trained on up to my last update in January 2022."
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Reply to every message with a random quote
    await message.channel.send(random.choice(quotes))

    # Continue processing other events
    await bot.process_commands(message)

# Run the bot with the token
bot.run(TOKEN)
