import discord
from discord.ext import commands
from discord import Interaction, app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

class Menu(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="메뉴", description="메뉴를 추천합니다. (keyword = 식사 or 디저트)")
  async def menu(self, interaction: Interaction, keyword: str):
    """메뉴를 추천합니다. (keyword = 식사 or 디저트)"""
    input_keyword = keyword
    if (input_keyword == "식사"):
      await interaction.response.send_message(f"🍙식사 메뉴가 랜덤으로 나옵니다!")
    elif (input_keyword == "디저트"):
      await interaction.response.send_message(f"🧁디저트 메뉴가 랜덤으로 나옵니다!")
    else:
      await interaction.response.send_message(f"잘못된 명령어 입니다.")

async def setup(bot):
  await bot.add_cog(Menu(bot))