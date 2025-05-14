# command 데코레이터 밑에 있는 함수명이 명령어
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
async def test(ctx):
  await ctx.send(f"hello {bot.user}")

@bot.event
async def setup_hook():
  await bot.load_extension('cogs.timer')

bot.run(TOKEN_KEY)