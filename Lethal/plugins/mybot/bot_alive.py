

import os
from telethon import Button, events

from Lethal import ALIVE_NAME, bot

currentversion = "0.1"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓєτнαℓ"
ASSIS_PIC = os.environ.get("ASSIS_PIC", None)
if ASSIS_PIC is None:
    PM_IMG = "https://telegra.ph/file/af3b74010808a26480693.jpg"
else:
    PM_IMG = ASSIS_PIC


pm_caption = " ►**ɦɛʏʏ ʏօʊʀ ǟֆֆɨֆȶǟռȶ ɨֆ `օռʟɨռɛ`\n\n"
pm_caption += "► **Sʏsᴛᴇᴍ sᴛᴀᴛs**\n"
pm_caption += "► **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ:** `1.23.0` \n"
pm_caption += f"► **ℓєτнαℓ ᴀssɪᴛᴀɴᴛ ᴠᴇʀsɪᴏɴ** : `{currentversion}`\n"
pm_caption += f"► **Mʏ ᴍᴀsᴛᴇʀ** : {DEFAULTUSER} \n"
pm_caption += "► **ℓєτнαℓ ʟɪᴄᴇɴsᴇ** : [GNU General Public License v3.0](https://github.com/Javes786/LETHAL-USERBOT/blob/master/LICENSE)\n"
pm_caption += "► **Cᴏᴘʏʀɪɢʜᴛ** :[ℓєτнαℓ](https://github.com/Javes786/LETHAL-USERBOT)\n"
light = [[Button.url("✧ʀᴇᴘᴏsɪᴛᴏʀʏ✧",
                     "https://github.com/Javes786/LETHAL-USERBOT"),
          Button.url("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ",
                     "https://t.me/DestroyXSupport")]]


@tgbot.on(events.NewMessage(pattern="^/alive",
                            func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption, buttons=light)
