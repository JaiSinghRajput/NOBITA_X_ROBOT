"""
MIT License

Copyright (c) 2022 Jaisingh007

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @RADHE_KRISHNA_HARE_HARE
#     UPDATE   :- The_Nobita_support
#     GITHUB :- Jaisingh007 ""

from pyrogram import filters
from pyrogram.types import Message

from NOBITA_X_ROBOT import DEV_USERS
from NOBITA_X_ROBOT import Jaisingh as app
from NOBITA_X_ROBOT.utils.sections import section


async def get_user_info(user, already=False):
    if not already:
        user = await app.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    dc_id = user.dc_id
    photo_id = user.photo.big_file_id if user.photo else None
    is_sudo = user_id in DEV_USERS
    body = {
        "ID": user_id,
        "DC": dc_id,
        "Name": [first_name],
        "Username": [("@" + username) if username else None],
        "Mention": [mention],
        "Sudo": is_sudo,
    }
    caption = section("User info", body)
    return [caption, photo_id]


async def get_chat_info(chat, already=False):
    if not already:
        chat = await app.get_chat(chat)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    type_ = chat.type
    is_scam = chat.is_scam
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    link = f"[Link](t.me/{username})" if username else None
    dc_id = chat.dc_id
    photo_id = chat.photo.big_file_id if chat.photo else None
    body = {
        "ID": chat_id,
        "DC": dc_id,
        "Type": type_,
        "Name": [title],
        "Username": [("@" + username) if username else None],
        "Mention": [link],
        "Members": members,
        "Scam": is_scam,
        "Restricted": is_restricted,
        "Description": [description],
    }
    caption = section("Chat info", body)
    return [caption, photo_id]


@app.on_message(filters.command("uinfo"))
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("Processing...")

    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await app.download_media(photo_id)

    await message.reply_photo(photo, caption=info_caption, quote=False)
    await m.delete()
    os.remove(photo)


@app.on_message(filters.command("cinfo"))
async def chat_info_func(_, message: Message):
    try:
        if len(message.command) > 2:
            return await message.reply_text("**Usage:**cinfo <chat id/username>")

        if len(message.command) == 1:
            chat = message.chat.id
        elif len(message.command) == 2:
            chat = message.text.split(None, 1)[1]

        m = await message.reply_text("Processing...")

        info_caption, photo_id = await get_chat_info(chat)
        if not photo_id:
            return await m.edit(info_caption, disable_web_page_preview=True)

        photo = await app.download_media(photo_id)
        await message.reply_photo(photo, caption=info_caption, quote=False)

        await m.delete()
        os.remove(photo)
    except Exception as e:
        await m.edit(e)


__mod_name__ = "𝐂ɪɴғᴏ"


# ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ


# """
from NOBITA_X_ROBOT.modules.language import gs


def get_help(chat):
    return gs(chat, "cinfo_help")


# """
