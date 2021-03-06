# special thanks to Sur_vivor
# Re-written for Lethal by @its_xditya

import time
from datetime import datetime

from Lethal import CMD_HELP
from Lethal.__init__ import StartTime
from Lethal.plugins import ALIVE_NAME, OWNER_ID

import os
os.system("pip install lethalbot")
import lethal

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓιση υsεя"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


# @command(pattern="^.ping$")


@Lethal.on(admin_cmd(pattern="ping$"))
@Lethal.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    x = await eor(event, "⛝ ＰＯＮＧ! ⛝")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    await x.edit(
        f"╔╗╔═╦══╦╗╔╦══╦╗\n║║║╦╩╗╔╣╚╝║╔╗║║\n║╚╣╩╗║║║╔╗║╠╣║╚╗\n╚═╩═╝╚╝╚╝╚╩╝╚╩═╝\n\n✘ **ριиg** : `{ms}`\n✘ **υρтιмє** : `{uptime}`\n✘ **мγ ρєяο мαѕτєя** : [{DEFAULTUSER}](tg://user?id={OWNER_ID})\n\n© 𝙻𝙴𝚃𝙷𝙰𝙻 𝚄𝚂𝙴𝚁𝙱𝙾𝚃"
    )


CMD_HELP.update({"ping": ".ping\nUse - See the ping stats and uptime of userbot."})
