import asyncio
import math
import os
import shutil
import time
from datetime import datetime as dt
from platform import python_version as pyver
from datetime import datetime
import heroku3
import requests
from telethon.utils import resolve_invite_link
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Serenity.plugins.officials import add_enforcers, add_inspector, rem_enforcers, rem_inspector
from Serenity import ENFORCERS, INSPECTORS, session
from Serenity import System, system_cmd
from Serenity import Sibyl_logs
import sys
from datetime import datetime as dt
from urllib.parse import urlparse, urlunparse
import heroku3
import os
import re

async def restart():
    await System.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

try:
    from Serenity import HEROKU_API_KEY, HEROKU_APP_NAME

    heroku_conn = heroku3.from_key(HEROKU_API_KEY)
    app = heroku_conn.app(HEROKU_APP_NAME)
    config = app.config()
    HEROKU = True
except BaseException:
    HEROKU = False


@System.on(system_cmd(pattern=r"ping", allow_enforcer=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    pong = await event.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await pong.edit("Pong!\n{}".format(ms))

@System.on(system_cmd(pattern=r"addarm", allow_inspectors=True))
async def addenf(event) -> None:
    if event.message.reply_to_msg_id:
        replied = await event.get_reply_message()
        if replied:
            u_id = replied.sender.id
        else:
            return
    else:
        u_id = event.text.split(" ", 2)[1]
        try:
            u_id = (await System.get_entity(u_id)).id
        except BaseException:
            await event.reply(
                "I dont know whose that user anyway!, I have to add "
            )
    if u_id in ENFORCERS:
        await System.send_message(event.chat_id, "That person is already an Official!")
        return
    if HEROKU:
        config["ENFORCERS"] = os.environ.get("ENFORCERS") + " " + str(u_id)
    else:
        await add_enforcers(u_id)
        await System.send_message(event.chat_id, "Added to officials, Restarting...")
        await restart()
    await System.send_message(
        event.chat_id, f"Added [{u_id}](tg://user?id={u_id}) to Officla"
    )


@System.on(system_cmd(pattern=r"rmarm", allow_inspectors=True))
async def rmenf(event) -> None:
    if event.message.reply_to_msg_id:
        replied = await event.get_reply_message()
        u_id = replied.sender.id
    else:
        u_id = event.text.split(" ", 2)[1]
    try:
        u_id = (await System.get_entity(u_id)).id
    except BaseException:
        await event.reply("Invalid ID/Username!")
    u_id = int(u_id)
    if HEROKU:
        str(u_id)
        ENF = os.environ.get("ENFORCERS")
        if ENF.endswith(str(u_id)):
            config["ENFORCERS"] = ENF.strip(" " + str(u_id))
        elif ENF.startswith(str(u_id)):
            config["ENFORCERS"] = ENF.strip(str(u_id) + " ")
        else:
            config["ENFORCERS"] = ENF.strip(" " + str(u_id) + " ")
    else:
        await rem_enforcers(u_id) 
        await System.send_message(
            event.chat_id, "Removed from Official, Restarting..."
        )
        await restart()
    await System.send_message(
        event.chat_id, f"Removed [{u_id}](tg://user?id={u_id}) from Official"
    )


@System.on(system_cmd(pattern=r"official", allow_inspectors=True))
async def listuser(event) -> None:
    msg = "Enforcers:\n"
    for z in ENFORCERS:
        try:
            user = await System.get_entity(z)
            msg += f"•[{user.first_name}](tg://user?id={user.id}) | {z}\n"
        except BaseException:
            msg += f"•{z}\n"
    await System.send_message(event.chat_id, msg)


@System.on(system_cmd(pattern=r"join", allow_inspectors=True))
async def join(event) -> None:
    try:
        link = event.text.split(" ", 1)[1]
    except BaseException:
        return
    private = re.match(
        r"(https?://)?(www\.)?t(elegram)?\.(dog|me|org)/joinchat/(.*)", link
    )
    if private:
        await System(ImportChatInviteRequest(private.group(5)))
        await System.send_message(event.chat_id, "Joined chat!")
        await System.send_message(
            Sibyl_logs,
            f"{(await event.get_sender()).first_name} made Serenity System join {private.group(5)}",
        )
    else:
        await System(JoinChannelRequest(link))
        await System.send_message(event.chat_id, "Joined chat!")
        await System.send_message(
            Sibyl_logs,
            f"{(await event.get_sender()).first_name} made Sibyl join {link}",
        )


@System.on(system_cmd(pattern=r"addva"))
async def addins(event) -> None:
    if event.reply:
        replied = await event.get_reply_message()
        if replied:
            u_id = replied.sender.id
        else:
            return
    else:
        u_id = event.text.split(" ", 2)[1]
    try:
        u_id = (await System.get_entity(u_id)).id
    except BaseException:
        await event.reply("Ivalid ID/Username!")
        return
    if u_id in INSPECTORS:
        await System.send_message(event.chat_id, "That person is already an UN Head!")
        return
    if HEROKU:
        config["INSPECTORS"] = os.environ.get("INSPECTORS") + " " + str(u_id)
    else:
        await add_inspector(u_id)
        await System.send_message(event.chat_id, "Added to UN Head, Restarting...")
        await restart()
    await System.send_message(
        event.chat_id, f"Added [{u_id}](tg://user?id={u_id}) to UN HEAD"
    )


@System.on(system_cmd(pattern=r"rmva"))
async def rmins(event) -> None:
    if event.message.reply_to_msg_id:
        replied = await event.get_reply_message()
        u_id = replied.sender.id
    else:
        u_id = event.text.split(" ", 2)[1]
    try:
        u_id = (await System.get_entity(u_id)).id
    except BaseException:
        await event.reply("Ivalid ID/Username!")
    if u_id not in INSPECTORS:
        await System.send_message(event.chat_id, "Is that person even an UN Head?")
        return
    u_id = str(u_id)
    if HEROKU:
        ENF = os.environ.get("INSPECTORS")
        if ENF.endswith(u_id):
            config["INSPECTORS"] = ENF.strip(" " + str(u_id))
        elif ENF.startswith(u_id):
            config["INSPECTORS"] = ENF.strip(str(u_id) + " ")
        else:
            config["INSPECTORS"] = ENF.strip(" " + str(u_id) + " ")
    else:
        await rem_inspector(u_id)
        await System.send_message(
            event.chat_id, "Removed from UN Head, Restarting..."
        )
        await restart()
    await System.send_message(
        event.chat_id,
        f"Removed Veteran status of [{u_id}](tg://user?id={u_id}), Now that user is an Official.",
    )

@System.on(system_cmd(pattern=r"veterans", allow_inspectors=True))
async def listuserI(event) -> None:
    msg = "Inspectors:\n"
    for z in INSPECTORS:
        try:
            user = await System.get_entity(z)
            msg += f"•[{user.first_name}](tg://user?id={user.id}) | {z}\n"
        except BaseException:
            msg += f"•{z}\n"
    await System.send_message(event.chat_id, msg)


@System.on(system_cmd(pattern=r"resolve", allow_inspectors=True))
async def resolve(event) -> None:
    try:
        link = event.text.split(" ", 1)[1]
    except BaseException:
        return
    match = re.match(
        r"(https?://)?(www\.)?t(elegram)?\.(dog|me|org)/joinchat/(.*)", link
    )
    if match:
        try:
            data = resolve_invite_link(match.group(5))
        except BaseException:
            await System.send_message(
                event.chat_id, "Couldn't fetch data from that link"
            )
            return
        await System.send_message(
            event.chat_id,
            f"Info from hash {match.group(5)}:\n**Link Creator**: {data[0]}\n**Chat ID**: {data[1]}",
        )


@System.on(system_cmd(pattern=r"out"))
async def leave(event) -> None:
    try:
        link = event.text.split(" ", 1)[1]
    except BaseException:
        return
    c_id = re.match(r"-(\d+)", link)
    if c_id:
        await System(LeaveChannelRequest(int(c_id.group(0))))
        await System.send_message(
            event.chat_id, f"Serenity left id[-{c_id.group(1)}]"
        )
    else:
        await System(LeaveChannelRequest(link))
        await System.send_message(event.chat_id, f"Serenity • UN  has left chat[{link}]")


@System.on(system_cmd(pattern=r"get_redirect ", allow_inspectors=True))
async def redirect(event) -> None:
    try:
        of = event.text.split(" ", 1)[1]
    except BaseException:
        return
    of = urlunparse(urlparse(of, "https"))
    async with session.get(of) as r:
        url = r.url
    await System.send_message(event.chat_id, f"URL: {url}")


help_plus = """
Help!
`addarm` - Adds a user as an Armature.
Format : addenf <user id / as reply>
`rmarm` - Removes a user from Armature.
Format : rmenf <user id / as reply>
`enforcers` - Lists all enforcers.
`addva` - Adds a user as an Veteran.
Format : addins <user id / as reply>
`rmva` - Removes a user from Veteran.
Format : rmins <user id / as reply>
`inspector` - Lists all Armature.
`join` - Joins a chat.
Format : join <chat username or invite link>
`leave` - Leaves a chat.
Format : leave <chat username or id>
`resolve` - Resolve a chat invite link.
Format : resolve <chat invite link>
`get_redirect` - Follows redirect of a link.
Format : get_redirect <URL>
**Notes:**
`/` `?` `.` `!` are supported prefixes.
**Example:** `/addarm` or `?addarm` or `.addarm`
"""

__plugin_name__ = "extras"
