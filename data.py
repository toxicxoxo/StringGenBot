from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton(" 🌸 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🌸 ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton(" 🍁 sᴜᴩᴩᴏʀᴛ 🍁", url="https://t.me/real_homies"),
         InlineKeyboardButton(" 🍁 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🍁", url="https://t.me/HOMIESAttendant"),
        ],
    ]

    START = """
Hᴇʏ {},

Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Sᴏᴜʀᴄᴇ : [Real H.O.M.I.E.S](https://t.me/real_homies)
Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [GOD](https://t.me/HOMIESAttendant) !
    """
