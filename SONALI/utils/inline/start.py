import random

from pyrogram.types import InlineKeyboardButton

import config
from SONALI import app


# Button styles: Blue, Green, Red
try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    try:
        from pyrogram.types import ButtonStyle
    except ImportError:
        ButtonStyle = None


STYLES = (
    [
        ButtonStyle.PRIMARY,
        ButtonStyle.SUCCESS,
        ButtonStyle.DANGER,
    ]
    if ButtonStyle
    else []
)


def get_button_style(style):
    if (
        getattr(config, "BUTTON_COLOUR", False)
        and style is not None
    ):
        return {"style": style}
    return {}


def random_style():
    if STYLES:
        return random.choice(STYLES)
    return None


def start_panel(_):
    style1 = random_style()
    style2 = random_style()

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
    styles = [random_style() for _ in range(4)]

    owner_username = getattr(
        config, "OWNER_USERNAME", ""
    ).strip("@")

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
