# For @UniBorg

# Courtesy @yasirsiddiqui

"""

.kickme

"""


import time

from telethon.tl.functions.channels import LeaveChannelRequest

from Lethal import CMD_HELP
from Lethal.utils import admin_cmd


@Lethal.on(admin_cmd(pattern="kickme", outgoing=True))
async def leave(e):
    x = bot.me
    name = x.first_name
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit(f"`{name} has left this group, bye!!.`")

        time.sleep(3)

        if "-" in str(e.chat_id):

            await borg(LeaveChannelRequest(e.chat_id))

        else:

            await e.edit("`This is Not A Chat. Please use this in groups :/`")


CMD_HELP.update({"kickme": ".kickme\nUse - Leave the group."})
