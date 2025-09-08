import discord
from discord.ext import commands
from discord import Interaction, app_commands

intents = discord.Intents.default()
intents.message_content = True

class Study(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="공부", description="공부할 과목을 입력하세요.")
  async def study(self, interaction: Interaction, subject: str):
    sub = subject
    await interaction.response.send_message(f"✏️ {sub} 과목을 시작합니다.")

async def setup(bot):
  await bot.add_cog(Study(bot))