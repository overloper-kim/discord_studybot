# command 데코레이터 밑에 있는 함수명이 명령어
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from discord import app_commands, Interaction, ButtonStyle, ui
from discord.ext import commands


load_dotenv()
TOKEN_KEY = os.environ.get("TOKEN_KEY")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.tree.command(name="안녕")
async def test(interaction: Interaction):
  button = ui.Button(style=ButtonStyle.green, label="안녕하세요!")
  view = ui.View()
  view.add_item(button)
  await interaction.response.send_message(view=view)

@bot.event
async def on_ready():
  await bot.tree.sync()
  print(f'Logged in as {bot.user}')

@bot.event
async def setup_hook():
  await bot.load_extension("cogs.timer")
  await bot.load_extension("cogs.user")

bot.run(TOKEN_KEY)