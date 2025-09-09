import discord
from discord.ext import commands
from discord import Interaction, app_commands, ButtonStyle
from discord.ui import View, Button
import asyncio

intents = discord.Intents.default()
intents.message_content = True

class StudyView(View):
  def __init__(self, subject: str):
    super().__init__(timeout=None)
    self.subject = subject
    self.running = True
    self.start_time = 0
    self.task = None
    self.msg = None

    start_btn = Button(label="시작", style=ButtonStyle.green)
    stop_btn = Button(label="정지", style=ButtonStyle.primary)
    end_btn = Button(label="종료", style=ButtonStyle.red)

    start_btn.callback = self.start_callback
    stop_btn.callback = self.stop_callback
    end_btn.callback = self.end_callback

    self.add_item(start_btn)
    self.add_item(stop_btn)
    self.add_item(end_btn)

  async def start_callback(self, interaction: Interaction):
    if not self.running:
      self.running = True
      await interaction.response.send_message(f"🟢 {self.subject} 학습을 시작합니다.", ephemeral=True)
      self.task = asyncio.create_task(self.timer_loop(interaction))

  async def stop_callback(self, interaction: Interaction):
    self.running = False
    await interaction.response.send_message(f"🛑 {self.subject} 학습이 정지 되었습니다.", ephemeral=True)

  async def end_callback(self, interaction: Interaction):
    self.running = False
    if self.task:
      self.task.cancel()
    await interaction.response.send_message(f"{self.subject} 학습을 종료합니다.", ephemeral=True)

    for child in self.children:
      child.disabled = True
    if self.msg:
      await self.msg.edit(view=self)

  async def timer_loop(self):
    embed = discord.Embed(title=self.subject, color=0xf6c41f)
    embed.add_field(name="학습 시간", value=f"⌛ 00:00:00 경과")
    await self.msg.edit(embed=embed, view=self)

    self.start_time = 0
    while True:
      if self.running:
        await asyncio.sleep(1)
        self.start_time += 1
        hour, mins = divmod(self.start_time // 60, 60)
        secs = self.start_time % 60
        timer_text = f"{hour:02d}:{mins:02d}:{secs:02d}"
        embed.set_field_at(0, name="학습 시간", value=f"⌛ {timer_text} 경과")
        await self.msg.edit(embed=embed, view=self)
      else:
        await asyncio.sleep(0.5)

class Study(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="공부", description="학습할 타이틀을 입력하세요.")
  async def study(self, interaction: Interaction, subject: str):
    sub = subject
    view = StudyView(sub)
    await interaction.response.send_message(f"✏️ {sub} 학습 시간 카운트 시작합니다.")

    embed = discord.Embed(
      title=sub,
      color=0xf6c41f
    )

    embed.add_field(name="학습 시간", value=f"⌛ 00:00:00 경과")
    msg = await interaction.followup.send(embed=embed, view=view)
    view.msg = msg  # 메세지 저장
    view.task = asyncio.create_task(view.timer_loop())

async def setup(bot):
  await bot.add_cog(Study(bot))