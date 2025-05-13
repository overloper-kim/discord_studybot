import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN_KEY = os.environ.get("TOKEN_KEY")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
  await ctx.send(f"hello {bot.user}")

bot.run(TOKEN_KEY)