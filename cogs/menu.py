import discord
from discord.ext import commands
from discord import Interaction, ButtonStyle, ui

class Menu(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    @commands.command(name="메뉴")
    async def menu(self, ctx, keyword: str):
      """메뉴를 추천합니다. (keyword = 식사 or 디저트)"""
      input_keyword = keyword
    
      if (input_keyword == "식사"):
        await ctx.send(f"🍙식사 메뉴가 랜덤으로 나옵니다!")
      elif (input_keyword == "디저트"):
        await ctx.send(f"🧁디저트 메뉴가 랜덤으로 나옵니다!")
      else:
        await ctx.send(f"잘못된 명령어 입니다.")

async def setup(bot):
  await bot.add_cog(Menu(bot))