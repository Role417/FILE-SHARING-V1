from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>𝐎𝐍𝐋𝐘 𝐅𝐎𝐑 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐀𝐂 𝐌𝐎𝐕𝐈𝐄𝐒 𝐁𝐎𝐓 🤗</b\n\n️<b>📌 𝗔𝗻𝘆 𝗛𝗲𝗹𝗽 𝗣𝗹𝗲𝗮𝘀𝗲 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗔𝗱𝗺𝗶𝗻 : @ARAKAL_THERAVAD_MOVIES_02_bot</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⟸ Bᴀᴄᴋ", callback_data="start"),
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


