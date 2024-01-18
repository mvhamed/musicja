import asyncio
from pyrogram import Client, filters
from AnonXMusic import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
#BiLaL


@Client.on_message(
    filters.command(["تعطيل الايدي", "قفل الايدي"], "")
    & filters.group
  
)
async def iddlock(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)  
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("الامر معطل من قبل عزيزي 🚦")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي عزيزي : 🦸")
   else:
      return await message.reply_text("عذرا  عزيزي هذا الامر للادمن الجروب فقط : 🚦")

@Client.on_message(
    filters.command(["فتح الايدي", "تفعيل الايدي"], "")
    & filters.group
  
)
async def iddopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("الايدي مفعل من قبل عزيزي  : 🥷")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم  تفعيل الايدي عزيزي : 🦸")
         
@Client.on_message(filters.command(["ايدي"], ""))
async def muid(client: Client, message):
       if message.chat.id in iddof:
         return await message.reply_text("**- تم تعطيل امر الايدي من قبل المشرفين**")
       user = await client.get_chat(message.from_user.id)
       user_id = user.id
       username = user.username
       first_name = user.first_name
       bioo = user.bio
       photo = user.photo.big_file_id
       photo = await client.download_media(photo)
       if not id.get(message.from_user.id):
         id[user.id] = []
       idd = len(id[user.id])
       await message.reply_photo(photo=photo, caption=f"""ꪗꪮꪊ𝘳 ꪀꪖꪑꫀ ᯒ {first_name}\nꪗꪮꪊ𝘳 𝓲ᦔ ᯒ{user_id}\nꪗꪮꪊ𝘳 ꪊ𝘴ꫀ𝘳 ꪀꪖꪑꫀ ᯒ @{username}\nꪗꪮꪊ𝘳 ᥇𝓲ꪮꪮ ᯒ {bioo}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       first_name, user_id=user_id),                
                ],[                
                    InlineKeyboardButton(
                        "ᥴ𝗁ꪀꪀᥱᥣ ᥱᥣꪀᘜ᥆᥆ꪔ ⌯", url=f"https://t.me/SOURCE_ELNGOM"),
                ],
                [    
                    InlineKeyboardButton(  
                        f"♥️ {idd}", callback_data=f"heart{user_id}")
                ],
            ]
        ),
    )
            


id = {}
@app.on_callback_query(filters.regex("heart"))  
async def heart(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("heart", "")  
    username = int(callback_request)
    usr = await client.get_chat(username)
    if not query.from_user.mention in id[usr.id]:
         id[usr.id].append(query.from_user.mention)
    else:
         id[usr.id].remove(query.from_user.mention)
    idd = len(id[usr.id])
    await query.edit_message_text(f"""ꪗꪮꪊ𝘳 ꪀꪖꪑꫀ ᯒ {usr.first_name}\nꪗꪮꪊ𝘳 𝓲ᦔ ᯒ{usr.id}\nꪗꪮꪊ𝘳 ꪊ𝘴ꫀ𝘳 ꪀꪖꪑꫀ ᯒ @{usr.username}\nꪗꪮꪊ𝘳 ᥇𝓲ꪮꪮ ᯒ {usr.bio}""", reply_markup=InlineKeyboardMarkup(  
            [
                [ 
                    InlineKeyboardButton(
                       usr.first_name, user_id=usr.id),   
                ],[                       
                    InlineKeyboardButton(
                        "ᥴ𝗁ꪀꪀᥱᥣ ᥱᥣꪀᘜ᥆᥆ꪔ ⌯", url=f"https://t.me/SOURCE_ELNGOM"),
                ],
                [  
                    InlineKeyboardButton(  
                        f"♥️ {idd}", callback_data=f"heart{usr.id}")
                ],  
            ]  
        ),  
                                 )

@app.on_message(
    command(["جمالي"])
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
       
