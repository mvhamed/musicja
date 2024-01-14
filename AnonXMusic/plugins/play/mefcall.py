from pyrogram import filters, Client
from AnonXMusic import app
import asyncio
from pyrogram.types import VideoChatEnded
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonXMusic.core.call import Anon
from AnonXMusic.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError, AlreadyJoinedError


AUDIO_FILE_PATH = "./AnonXMusic/assets/call.mp3"

async def handle_group_call(client, chat_id):
    
        assistant = await group_assistant(Anon, chat_id)
        await assistant.join_group_call(chat_id, AudioPiped(AUDIO_FILE_PATH), stream_type=StreamType().pulse_stream)
        participants = await assistant.get_participants(chat_id)

        
        text = "الناس الموجودين في المكالمة:\n\n"
        for idx, participant in enumerate(participants, start=1):
            user = await client.get_users(participant.user_id)
            mut_status = "يتحدث" if not participant.muted else "ساكت"
            text += f"{idx}➤{user.mention}➤{mut_status}\n"

        text += f"\nعددهم: {len(participants)}\n✔️"

     
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(chat_id)

    except NoActiveGroupCall:
        await message.reply("المكالمة مغلقة مسبقاً")
    except TelegramServerError:
        await message.reply("يرجى إعادة إرسال الأمر، هناك مشكلة في خادم التليجرام")
    except AlreadyJoinedError:

        await handle_group_call(client, chat_id)

async def handle_video_chat_ended(client, message):
    duration = message.video_chat_ended.duration
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    duration_text = (
        f"{days} أيام" if days > 0 else
        f"{hours} ساعة" if hours > 0 else
        f"{minutes} دقيقة" if minutes > 0 else
        f"{seconds} ثانية"
    )

    await message.reply(f"- تم انهاء مكالمة الفيديو مدتها {duration_text}")

@app.on_message(filters.regex("^مين في المكالمة$"))
async def start_group_call(client, message):
    await handle_group_call(client, message.chat.id)

@app.on_message(filters.video_chat_ended)
async def video_chat_ended_handler(client, message):
    await handle_video_chat_ended(client, message)
