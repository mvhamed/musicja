from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app

# vc on
@app.on_message(filters.video_chat_started)
async def zed(_, msg):
       await msg.reply("تم بدأ محادثه صوتيه")
# vc off
@app.on_message(filters.video_chat_ended)
async def zed2(_, msg):
       await msg.reply("تم إغلاق المحادثه الصوتيه")

# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def zed3(app:app, message:Message):
           text = f"- قام {message.from_user.mention}\n - بدعوة : "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"{user.first_name} "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass
