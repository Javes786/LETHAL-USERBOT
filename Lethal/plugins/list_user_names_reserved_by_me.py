# For @UniBorg
# (c) Shrimadhav U K
# PLUGINS KI MAA CHODNE WALA AMAAN :)
from telethon import functions, events

from Lethal import CMD_HELP
from Lethal.utils import admin_cmd, sudo_cmd


@Lethal.on(admin_cmd(pattern=r"listmyusernames", outgoing=True))
@Lethal.on(sudo_cmd(pattern=r"listmyusernames", outgoing=True, allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    result = await Lethal(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


CMD_HELP.update(
    {
        "list_user_names_reserved_by_me": ".listmyusernames\nUse - List all usernames you have reserved."
    }
)
