from jinja2 import Environment, FileSystemLoader
class WebPageView():
  def __init__(self, user: str):
    self.user_name = user


  file_loader = FileSystemLoader("../web/html")
  env = Environment(loader=file_loader)

  template = env.get_template('index.html')

  data = {}

  output = template.render(data)
  print(output)

import discord
from discord.ext import commands
from discord import Interaction, app_commands, ButtonStyle
from discord.ui import View, Button
import asyncio

class Statistics(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="통계", description="통계를 보고싶은 사용자 이름을 입력하세요.")
  async def stat(self, interaction: Interaction, user_name: str):
    user_name = user_name
    
async def setup(bot):
  await bot.add_cog(Statistics(bot))