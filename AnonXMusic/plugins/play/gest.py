import asyncio
import random
from AnonXMusic.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup)
from pyrogram import filters, Client
from AnonXMusic import app
from config import *

bot_name = {}
botname = {}

name = "جورجينا"

@app.on_message(filters.regex("تعيين اسم البوت")& filters.private & SUDOERS, group=7113)
async def set_bot_name(client, message):
    global name
    ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

caesar_responses = [
    "اسمي {name} يصحبي",
    "يسطا قولتلك اسمي {name} الاه",
    "نعم يحب",
    "قول يقلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يعم والله بحبك بس ناديلي ب {name}",
    "تعرف بالله هحبك أكتر لو ناديتلي {name}",
    "اي ي معلم مين مزعلك",
    "متصلي على النبي كدا",
    "مش فاضيلك نصايح وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج على أخوك",
    "انجز عايزني أشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا",
    "ورحمة أبويا اسمي {name}",
]

@app.on_message(filters.command(["بوت", "البوت"], ""), group=71135)
async def bottttt(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    bar = random.choice(selections).format(BOT_NAME)
    await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
    
#مقدم من القيصر صاحب العظمه @c_a_s_e_r_h                
#قناه سورس القيصر صاحب العظمه  @COURSE_CAESAR
