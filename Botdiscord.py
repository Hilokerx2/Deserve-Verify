import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

# กำหนดชื่อที่อนุญาต
allowed_names = ["Shiro", "ชื่อ2", "ชื่อ3"]
user_names = {}  # เก็บชื่อผู้ใช้และชื่อที่เลือก

# สร้างบอท
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def Verifys(ctx, *, name: str):
    user_id = ctx.author.id  # รหัสผู้ใช้ Discord ของคนที่เรียกใช้คำสั่ง

    if name in allowed_names:
        if name in user_names.values():
            await ctx.send("ชื่อนี้ถูกใช้ไปแล้ว กรุณาเลือกชื่ออื่น.")
        else:
            user_names[user_id] = name
            await ctx.send(f"คุณได้ตั้งชื่อเป็น: {name}")
    else:
        await ctx.send("ชื่อที่คุณใส่ไม่ถูกต้อง กรุณาใช้ชื่อที่กำหนดไว้")

@bot.command()
async def Check(ctx):
    user_id = ctx.author.id
    name = user_names.get(user_id, "คุณยังไม่ได้ตั้งชื่อ")
    await ctx.send(f"ชื่อของคุณคือ: {name}")


server_on()
# ใส่ Token ของบอทที่นี่
bot.run(os.getenv('TOKEN'))
