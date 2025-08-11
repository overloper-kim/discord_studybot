"""
회원추가{username} 입력 시 유저 추가 기능 만들기
"""

import discord
from discord.ext import commands
import asyncio

class User(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="사용자_추가")
  async def user(self, ctx, user_name: str):
    nickname = user_name
    await ctx.send(f"{nickname}을(를) 추가하였습니다.");

async def setup(bot):
  await bot.add_cog(User(bot))