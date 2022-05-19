import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
Ciao diocane {message.from_user.mention()} !

        Questo è nbot pe ascolta la musica diocane...

Tutti i miei comandi possono essere preceduti da questi segni : ( `/ . • $ ^ ~ + * ?` )
┏━━━━━━━━━━━━━━┓
┣★
┣★ Owner: t.me/sentinella
┣★
┗━━━━━━━━━━━━━━┛

SE HAI DOMANDE, nun te rispondo quindi non me scrive cesso...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aggiungimi al gruppo sacripante"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "Owner: t.me/sentinella"
                    ),
                    InlineKeyboardButton(
                        "Canale: t.me/PolaMusic"
                    )
                ],[
                    InlineKeyboardButton(
                        "Inline", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Canale", url="https://t.me/PolaMusic"
                    )]
            ]
       ),
    )

