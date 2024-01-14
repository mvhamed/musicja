import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AnonXMusic import app
from config import OWNER_ID

@app.on_message(filters.command(['بوت'], prefixes=""))
async def Italymusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    star = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الي مجموعتك ⚡", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 5940413527:
             rank = "مطور السورس"
        elif user_id == OWNER_ID:
             rank = "صاحب البوت يمعلم ⇇ اهلا مطوري الغالي كلو تحت السيطره يمعلم🥹❤️‍🔥"
        elif member.status == 'creator':
             rank = "وه مالك الجروب⇇ يمعلم دخولك رايق سبب حرايق🥹🦋"
        elif member.status == 'administrator':
             rank = "مشرف الجروب⇇ ينهار ابيض كابيه شاي للمعلم هنا يبني 🥹❤️"
        else:
             rank = "**لاسف انت عضو فقير🥺💔**"
    except Exception as e:
        print(e)
        rank = "مش عرفنلو مله ده😒"
    async for photo in client.get_chat_photos("me", limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""اتفضل يـ ⇇: {star} عوز اي🤍🦋\n**وانا بوت يمعلم واسمي ⇇ : {bot_name} 🥺🍓\n**رتبتك يمعلم ⇇ : {rank}""", reply_markup=keyboard)

