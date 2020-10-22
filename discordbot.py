import discord
import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_message(message):
    if "!語録" in message.content:
        word_list = ["ブンブンハローRed♪Tube","SexkinTV♪every day♪","ひき逃げです","ヒカキンさんのアナ、ゥお借りしたいんです！","OnakinTV♪every day♪","ナイチンチンゲール♪","ウンコの力","ケツの穴が無い！","パンパンパンパンパン！パンパン！","メッサムラムラ！？","ローション！？","最初はブンブンじゃんけん出たー！出た！出たぁ...","あ～ん！ちゃんち～ん！あっちっち～","なんか4545ってこれ誰だ？遊んでんのかな？"]
        await message.channel.send(random.choice(word_list))

bot.run(token)
