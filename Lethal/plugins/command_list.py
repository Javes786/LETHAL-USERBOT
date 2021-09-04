# Join @LethalHelp for custom plugins

import asyncio

import requests

from Lethal import CMD_HELP


@Lethal.on(admin_cmd(pattern="cmds", outgoing=True))
@Lethal.on(sudo_cmd(pattern="cmds", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    tele = await eor(event, "`Searching for all plugins...`")
    cmd = "ls Lethal/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = (
        OUTPUT
    ) = f"Here is the list of plugins found in 'main' branch of Lethal.\n{o}\n\nUse .help <cmd_name> to learn how a paticular plugin works.\nConsider joining @DesTRoYxSupport for help!"
    await event.edit("`Plugins extracted, pasting it...`")
    message = OUTPUT
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    await event.edit(
        f"`All plugins available in` **Lethal** `can be found` [here]({https://github.com/Javes786/LETHAL-USERBOT/Lethal/Plugins})!!"
    )


CMD_HELP.update(
    {"command_list": ".cmds\nUse - Get the list of all plugins in the userbot."}
)
