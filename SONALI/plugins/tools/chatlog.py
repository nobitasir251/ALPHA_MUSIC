
import random

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import RPCError
from pyrogram.enums import ParseMode

from config import LOGGER_ID as LOG_GROUP_ID
from SONALI import app


photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]


async def get_group_link(chat):
    """Get an invite link without crashing when permissions are missing."""
    try:
        if chat.username:
            return f"https://t.me/{chat.username}"

        return await app.export_chat_invite_link(chat.id)

    except RPCError as e:
        print(f"Could not get invite link for {chat.id}: {e}")
        return None


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(client, message: Message):
    chat = message.chat

    # Only log when this bot itself is added to a group.
    if not any(member.id == app.id for member in message.new_chat_members):
        return

    link = await get_group_link(chat)

    try:
        count = await app.get_chat_members_count(chat.id)
    except RPCError as e:
        print(f"Could not get member count for {chat.id}: {e}")
        count = "Unavailable"

    added_by = (
        message.from_user.mention
        if message.from_user
        else "Unknown User"
    )

    chat_name = chat.title or "Unknown Group"
    chat_username = f"@{chat.username}" if chat.username else "Private Group"
    link_text = (
        f'<a href="{link}">CLICK HERE</a>'
        if link
        else "Unavailable — grant invite-link permission"
    )

    msg = (
        "📝 <b>Music Bot Added to a New Group</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"📌 <b>Chat Name:</b> {chat_name}\n"
        f"🍂 <b>Chat ID:</b> <code>{chat.id}</code>\n"
        f"🔐 <b>Username:</b> {chat_username}\n"
        f"🛰 <b>Chat Link:</b> {link_text}\n"
        f"📈 <b>Group Members:</b> {count}\n"
        f"🤔 <b>Added By:</b> {added_by}"
    )

    buttons = []
    if link:
        buttons.append(
            [InlineKeyboardButton("See Group 👀", url=link)]
        )

    try:
        await app.send_photo(
            chat_id=LOG_GROUP_ID,
            photo=random.choice(photo),
            caption=msg,
            reply_markup=InlineKeyboardMarkup(buttons) if buttons else None,
            parse_mode=ParseMode.HTML,
        )
    except RPCError as e:
        print(f"Could not send group-add log: {e}")


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client, message: Message):
    left_member = message.left_chat_member

    if not left_member or left_member.id != app.id:
        return

    remove_by = (
        message.from_user.mention
        if message.from_user
        else "Unknown User"
    )

    title = message.chat.title or "Unknown Group"
    username = (
        f"@{message.chat.username}"
        if message.chat.username
        else "Private Chat"
    )

    left = (
        "✫ <b><u>#LEFT_GROUP</u></b> ✫\n\n"
        f"<b>Chat Title:</b> {title}\n\n"
        f"<b>Chat ID:</b> <code>{message.chat.id}</code>\n\n"
        f"<b>Username:</b> {username}\n\n"
        f"<b>Removed By:</b> {remove_by}\n\n"
        f"<b>Bot:</b> @{app.username}"
    )

    try:
        await app.send_photo(
            chat_id=LOG_GROUP_ID,
            photo=random.choice(photo),
            caption=left,
            parse_mode=ParseMode.HTML,
        )
    except RPCError as e:
        print(f"Could not send group-removal log: {e}")
