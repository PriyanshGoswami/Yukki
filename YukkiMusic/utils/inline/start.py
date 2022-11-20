from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app

def start_pannel(_):
    buttons = []

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"‎‎‎‎‎‎‎‎ㅤ",
                url=f"https://t.me/toga_robot?startgroup=true",
            ),
        ],
     ]
    return buttons
