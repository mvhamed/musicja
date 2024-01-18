from pyrogram.enums import ChatMemberStatus
from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app

@app.on_message(filters.command(["/help", "الاوامر", "اوامر",": الاوامر :"], ""))
async def starhelp(client: Client, message: Message):
      if await joinch(message):
            return
    bot = await client.get_me()
    photo = bot.photo.big_file_id
    photo = await client.download_media(photo)
    await message.reply_photo(
        photo=photo,
        caption=f"[⌯ ᭙ᥱᥣᥴ᥆ꪔᥱ ƚ᥆ 𝗁ᥱᥣρ ᥉᥆υᖇᥴᥱ  ⌯](https://t.me/{gh})",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("اللغة العربية 🇪🇬", callback_data="arbic")
                        ],
                        [   
                            InlineKeyboardButton("English language 🇺🇲", callback_data="english")
                        ],
                        [
                            InlineKeyboardButton(f"ժᥱ᥎ ᥉᥆υᖇᥴᥱ : ⌯", url=f"https://t.me/{DEV_USER}")
                        ],
                        [
                            InlineKeyboardButton("ᥲ️ժժ ƚ𝗁ᥱ Ⴆ᥆ƚ ƚ᥆ Y᥆υᖇ ᘜᖇ᥆υρ : ⌯", url="https://t.me/{bot.username}?startgroup=true")
                        ],
                    ]                         
                )
            )
    try:
      os.remove(photo)
    except:
       pass
  
