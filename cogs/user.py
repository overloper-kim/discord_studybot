import discord
from discord.ext import commands
from discord import Interaction, app_commands

intents = discord.Intents.default()
intents.message_content = True

class User(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="등록", description="사용자 이름을 입력하세요.")
  async def user(self, interaction: Interaction, user_name: str):
    nickname = user_name
    await interaction.response.send_message(f"✅ {nickname} 님을 추가하였습니다.")

async def setup(bot):
  await bot.add_cog(User(bot))