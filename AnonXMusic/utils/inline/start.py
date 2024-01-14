from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
         [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘ ⚡",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ 🕷.️", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇꜱ 🕷️.", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Oᴡɴᴇʀ 🕷️.", url="https://t.me/Mvhmed"
            )
        ],
        [ 
          InlineKeyboardButton(
                text="Lᴀɴɢᴜᴀɢᴇꜱ 🕷️.", callback_data="LG"
            )
        ],
    ]
    return buttons
