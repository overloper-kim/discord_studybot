# command 데코레이터 밑에 있는 함수명이 명령어
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from discord import app_commands, Interaction, ButtonStyle, ui

load_dotenv()
TOKEN_KEY = os.environ.get("TOKEN_KEY")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.tree.command(name="안녕")
async def test(interaction: Interaction):
    button = ui.Button(style=ButtonStyle.green, label="안녕하세요!")
    view = ui.View()
    view.add_item(button)
    await interaction.response.send_message(view=view)


@bot.tree.command(name="도움")
async def tests(message):
    embed = discord.Embed(
        title="너굴맨의 선물 🎁",
        description="모든 명령어는 / 를 붙여주면 됩니다.",
        color=0xf6c41f
    )
    embed.set_author(name="DEV BY OVERLOPER")
    thumbnail = discord.File('./asset/nuri_draw_me.jpg', filename='nuri_draw_me.jpg')
    embed.set_thumbnail(url="attachment://nuri_draw_me.jpg")
    embed.add_field(name="도움", value="해당 이 봇의 명령어 및 기능을 알려줍니다.", inline=False)
    embed.add_field(name="통계", value="요청 기준 일주일 동안 공부한 시간 등 통계하여 파일을 제공합니다.", inline=False)
    embed.add_field(name="메뉴", value="식사나 디저트 중 등록된 메뉴를 랜덤으로 추천합니다.", inline=False)
    embed.add_field(name="공부", value="공부 전용 타이머이며 학습 시간을 계산합니다.", inline=False)
    embed.add_field(name="스트레칭", value="스트레칭 시간을 알람으로 알려줍니다.(기본 설정: 1시간)", inline=False)
    embed.add_field(name="설정", value="타이머 등 해당 봇을 설정할 수 있습니다.", inline=False)
    embed.set_footer(text="추가 기능은 카톡으로 문의 부탁드립니다.")
    await message.channel.send(file=thumbnail, embed=embed)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user}')

@bot.event
async def setup_hook():
    await bot.load_extension("cogs.timer")
    await bot.load_extension("cogs.user")

bot.run(TOKEN_KEY)
