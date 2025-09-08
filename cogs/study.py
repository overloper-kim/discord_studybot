import discord
from discord.ext import commands
from discord import Interaction, app_commands, ButtonStyle
from discord.ui import View, Button
import time

intents = discord.Intents.default()
intents.message_content = True

class StudyView(View):
  def __init__(self, subject: str):
    super().__init__(timeout=None)
    self.subject = subject

    stop_btn = Button(label="정지", style=ButtonStyle.primary)
    stop_btn.callback = self.stop_callback
    self.add_item(stop_btn)

  async def stop_callback(self, interaction: Interaction):
    await interaction.response.send_message(f"🛑 {self.subject} 학습이 정지 되었습니다.", ephemeral=True)

class Study(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="공부", description="학습할 타이틀을 입력하세요.")
  async def study(self, interaction: Interaction, subject: str):
    sub = subject
    await interaction.response.send_message(f"✏️ {sub} 학습 시간 카운트 시작합니다.")

    start_time = int(time.time())
    
    embed = discord.Embed(
      title=sub,
      color=0xf6c41f
    )

    embed.add_field(name="학습 시간", value=f"<t:{start_time}:R>:")

    view = StudyView(sub)
    await interaction.followup.send(embed=embed, view=view)

async def setup(bot):
  await bot.add_cog(Study(bot))