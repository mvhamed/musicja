import asyncio
import random
from AnonXMusic.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup)
from pyrogram import filters, Client
from AnonXMusic import app
from config import *

@app.on_message(~filters.private)
async def booot(client: Client, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(client, chat_id):
       try:
        await add_served_chat(client, chat_id)
        chats = len(await get_served_chats(client))
        bot_username = client.me.username
        dev = await get_dev(bot_username)
        username = f"https://t.me/{message.chat.username}" if message.chat.username else None
        mention = message.from_user.mention if message.from_user else message.chat.title
        await client.send_message(dev, f"**تم تفعيل محادثة جديدة تلقائياً واصبحت {chats} محادثة**\nNew Group : [{message.chat.title}]({username})\nId : {message.chat.id} \nBy : {mention}", disable_web_page_preview=True)
        await client.send_message(chat_id, f"**تم رفع البوت بنجاح ايها العضو اللطيف 🥷**")
        return 
       except:
          pass
    message.continue_propagation()
