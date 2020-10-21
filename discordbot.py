from discord.ext import commands
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
    if "h.goroku" in message.content:
        word_list = ["ブンブンハローRed♪Tube","SexkinTV♪every day♪","ひき逃げです","ヒカキンさんのアナ、ゥお借りしたいんです！","OnakinTV♪every day♪","ナイチンチンゲール♪","ウンコの力","ケツの穴が無い！","パンパンパンパンパン！パンパン！","メッサムラムラ！？","ローション！？","最初はブンブンじゃんけん出たー！出た！出たぁ...","あ～ん！ちゃんち～ん！あっちっち～","なんか4545ってこれ誰だ？遊んでんのかな？"]
        await message.channel.send(random.choice(word_list))

@client.event
async def on_message(message):
    if "h.zimaku" in message.content:
        word_list = ["https://media.discordapp.net/attachments/768422797974175764/768422877372350474/Ek2IB7_UYAAOpsW.png","https://media.discordapp.net/attachments/768422797974175764/768423141583618058/Ek16S95VkAAGqBL.png?width=1194&height=671","https://media.discordapp.net/attachments/768422797974175764/768423170855927808/Ek1zbstU8AAAhEH.png","https://media.discordapp.net/attachments/768422797974175764/768423217470636092/Ek1skJ0VcAUm8gG.png?width=1194&height=671","https://media.discordapp.net/attachments/768422797974175764/768423281497473054/Ek1lsjqUYAAeH1b.png","https://media.discordapp.net/attachments/768422797974175764/768423319313448991/Ek1e1TAVMAEGHlg.png","https://media.discordapp.net/attachments/768422797974175764/768423444517355580/Ek1X9yhUcAE62X_.png","https://media.discordapp.net/attachments/768422797974175764/768423491497361438/Ek1RGR5VMAAWbJX.png","https://media.discordapp.net/attachments/768422797974175764/768423536897294346/Ek1KO_kU8AMheiy.png","https://media.discordapp.net/attachments/768422797974175764/768423582991777832/Ek1DXVxUUAEMg1l.png","https://media.discordapp.net/attachments/768422797974175764/768423629510803496/Ek08gEDU8AAr0Du.png","https://media.discordapp.net/attachments/768422797974175764/768423677858414632/Ek01oifU8AIv7-Y.png?width=1194&height=671"]
        await message.channel.send(random.choice(word_list))

bot.run(token)
