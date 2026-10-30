
import random

from pyrogram import enums
from pyrogram.types import InlineKeyboardButton

import config
from SONALI import app


STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER,
]


def get_button_style(style):
    if getattr(config, "BUTTON_COLOUR", False):
        return {"style": style}
    return {}


def start_panel(_):
    style1 = random.choice(STYLES)
    style2 = random.choice(STYLES)

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                **get_button_style(style1)
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                **get_button_style(style2)
            ),
        ]
    ]

    return buttons


def private_panel(_):
    styles = random.choices(STYLES, k=4)

    owner_username = getattr(config, "OWNER_USERNAME", "").strip("@")

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                **get_button_style(styles[0])
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{owner_username}",
                **get_button_style(styles[1])
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                **get_button_style(styles[2])
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                **get_button_style(styles[3])
            )
        ],
    ]

    return buttons
