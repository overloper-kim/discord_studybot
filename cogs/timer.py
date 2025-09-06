"""
timer 입력 시 60초 이상이면 분으로 표시
"""
import discord
from discord.ext import commands
from discord import Interaction, app_commands, Member, User
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

class Timer(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="타이머", description="시간을 설정해주세요. (시간 기준 초(S) 단위)")
  async def timer(self, interaction: Interaction, seconds: int):
    """타이머를 설정합니다 (예: !timer 5)"""
    input_second = seconds
    if (seconds >= 60) :
      min = seconds / 60
      seconds = seconds % 60
      await interaction.response.send_message(f"⏰ 타이머 시작! \n {int(min)}분 {seconds}초")
      await asyncio.sleep(input_second)
    else:
      await interaction.response.send_message(f"⏰ 타이머 시작! {seconds} 초")
      await asyncio.sleep(seconds)
    
    await interaction.followup.send(f"⏰ {discord.User.name}, 타이머 종료!")

async def setup(bot):
  await bot.add_cog(Timer(bot))