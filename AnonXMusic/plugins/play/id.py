import asyncio
from pyrogram import Client, filters
from AnonXMusic import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
#BiLaL


iddof = []
app.on_message(filters.command(["قفل الايدي","تعطيل الايدي"])
    & filters.group
)
async def iddlock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("تم معطل من قبل \n√")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي بنجاح √")
   else:
      return await message.reply_text("لازم تكون ادمن \n√")

app.on_message(filters.command(["فتح الايدي","تفعيل الايدي"])
    & filters.group
)
async def iddopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("الايدي مفعل من قبل √")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح الايدي بنجاح √")
   else:
      return await message.reply_text("لازم تكون ادمن \n√")




app.on_message(filters.command(["ايدي","id","ا"])
    & filters.group
)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f""" - ꪀᥲ️︎ꪔᥱ︎ :{message.from_user.mention}\n- u᥉ᥱ︎ɾ :@{message.from_user.username}\n- Ꭵძ . :`{message.from_user.id}`\nႦᎥ᥆ :{usr.bio}\nᥴ𝗁ᥲ️ƚ: {message.chat.title}\n𝚒𝚍 𝚐𝚛𝚘𝚞𝚋 :`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )



iddof = []

app.on_message(filters.command(["جمالي"])
    & filters.group
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا مز انت \n※ \n🐉: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
       
