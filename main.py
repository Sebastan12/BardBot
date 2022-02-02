from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
import youtube_dl

def print_hi(name):
    load_dotenv()
    if not os.getenv('BOT_API_TOKEN'):
        print("NO BOT_API_TOKEN found in .env")
        return
    BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
    client = commands.Bot(command_prefix='?', intents=discord.Intents.all())
    client.run(BOT_API_TOKEN)


if __name__ == '__main__':
    print_hi('PyCharm')


