from datetime import datetime
from io import BytesIO

import aiohttp
from pyrogram import filters
from pyrogram.types import Message

from SONALI import app
from SONALI.core.call import Sona
from SONALI.utils import bot_sys_stats
from SONALI.utils.decorators.language import language
from SONALI.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()

    caption = _["ping_1"].format(app.mention)

    try:
        timeout = aiohttp.ClientTimeout(total=15)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(PING_IMG_URL) as res:
                res.raise_for_status()

                content_type = res.headers.get("Content-Type", "")
                if not content_type.startswith("image/"):
                    raise ValueError("URL did not return an image")

                image_data = await res.read()

        photo = BytesIO(image_data)
        photo.name = "ping.jpg"

        response = await message.reply_photo(
            photo=photo,
            caption=caption,
        )

    except Exception as e:
        print(f"PING IMAGE ERROR: {e}")
        response = await message.reply_text(caption)

    pytgping = await Sona.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()

    resp = (datetime.now() - start).total_seconds() * 1000

    await response.edit_text(
        _["ping_2"].format(
            resp, app.mention, UP, RAM, CPU, DISK, pytgping
        ),
        reply_markup=supp_markup(_),
    )
