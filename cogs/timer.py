import discord
from discord.ext import commands
import asyncio

class Timer(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def timer(self, ctx, seconds: int):
    """타이머를 설정합니다 (예: !timer 5)"""
    await ctx.send(f"⏰ 타이머 시작! {seconds} 초")
    await asyncio.sleep(seconds)
    await ctx.send(f"⏰ {ctx.author.mention}, 타이머 종료!")

async def setup(bot):
  await bot.add_cog(Timer(bot))