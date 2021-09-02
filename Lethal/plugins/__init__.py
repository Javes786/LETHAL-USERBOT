#    Lethal - UserBot
#    Copyright (C) 2020 Lethal

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon.tl.types import Channel

from Lethal import *
from Lethal import ALIVE_NAME, bot, lethalver
from Lethal.LethalConfig import Config, Var

# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

LETHALUSER = str(ALIVE_NAME) if ALIVE_NAME else "@DestroyXSupport"

lethal = f"𝙻𝙸𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽: {lethalver}\n"
lethal += f"𝙻𝙾𝙶 𝙶𝚁𝙾𝚄𝙿: {log}\n"
lethal += f"𝙼𝚈 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙱𝙾𝚃: {bots}\n"
lethal += f"𝙻𝚈𝙳𝙸𝙰: {lyd}\n"
lethal += f"𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁: {sudo}\n"
lethal += f"𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈: {pm}\n"
lethal += f"\n𝚅𝙸𝚂𝙸𝚃 @DestroyXSupport 𝙵𝙾𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃.\n"
lethalstats = f"{lethal}"

LETHAL_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# count total number of groups


async def lethal_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
