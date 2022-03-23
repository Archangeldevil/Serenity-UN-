"""
BSD 2-Clause License

Copyright (C) 2022, Awesome-RJ, <https://github.com/Kajukatliii/Serenity>

All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import re
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from Serenity import System, ENFORCERS, INSPECTORS, SIBYL

def Serenity_system_cmd(
    pattern=None,
    allow_Skynet=True,
    allow_enforcer=False,
    allow_inspectors=False,
    allow_slash=True,
    force_reply=False,
    **args
):
    if pattern and allow_slash:
#        args["pattern"] = re.compile(r"[\?\.!/](" + pattern + r")(?!@)")
        args["pattern"] = re.compile(r"[\?\.!/]" + pattern)
    else:
        args["pattern"] = re.compile(r"[\?\.!]" + pattern)
    if allow_Skynet and allow_enforcer:
        args["from_users"] = ENFORCERS
    elif allow_inspectors and allow_Skynet:
        args["from_users"] = INSPECTORS
    else:s
        args["from_users"] = SIBYL
    if force_reply:
        args["func"] = lambda e: e.is_reply
    return events.NewMessage(**args)


@System.on(Serenity_system_cmd(pattern=r"info"))
async def whois(event):
    try:
        to_get = event.pattern_match.group(1)
    except Exception:
        if event.reply:
            replied = await event.get_reply_message()
            to_get = int(replied.sender.id)
        else:
            return
    try:
        to_get = int(to_get)
    except Exception:
        pass
    try:
        data = await System(GetFullUserRequest(to_get))
    except Exception:
        await event.reply("Failed to get data of the user")
        return
    await System.send_message(
        event.chat_id,
        f"Perma Link: [{data.user.first_name}](tg://user?id={data.user.id})\nUser ID: `{data.user.id}`\nAbout: {data.about}",
    )


help_plus = """ Here is Help for **Whois** -
`whois` - get data of the user
**Notes:**
`/` `?` `.` `!` are supported prefixes.
**Example:** `/addenf` or `?addenf` or `.addenf`
"""
__plugin_name__ = "Info"
