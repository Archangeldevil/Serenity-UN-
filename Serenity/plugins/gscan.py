from .. import System, Sibyl_logs, GBAN_MSG_LOGS, Sibyl_approved_logs as kek
from telethon.tl.functions.channels import GetFullChannelRequest
from .MONGO_DB.gbans import update_gban
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
from Serenity import System, system_cmd

@System.on(system_cmd(pattern="gscan ?(.*)", allow_inspectors=False))
async def group_info(event):
    args = event.pattern_match.group(1)
    tq = args.split(" ")
    id_1 = tq[0].strip()
    id = f"{id_1} "
    try:
        reasons = args.split(id)
        reason = reasons[1]
    except Exception:
        return await event.reply("Enter a reason")
    if event.is_reply:
     try:
      gay=await event.reply('Connecting to Serenity • UN core for Judgement')
      entity = await event.client.get_entity(str(id))
      totallist = await event.client.get_participants(
            entity, filter=ChannelParticipantsAdmins)
      for user in (await event.client.get_participants(entity, filter=ChannelParticipantsAdmins)):      
              ch_full = await event.client(GetFullChannelRequest(channel=entity))
     except Exception as e:
      await gay.edit(str(e))
    if not event.reply_to_msg_id:
       return await event.reply('Reply to msg to add it as proof')
    msg = "**#GSCANREQUEST**"
    msg += f"**ID**: `{entity.id}`"
    msg += f"\n**Title**: `{entity.title}`"
    msg += f"\n**Datacenter**: `{entity.photo.dc_id}`"
    msg += f"\n**Video PFP**: `{entity.photo.has_video}`"
    msg += f"\n**Supergroup**: `{entity.megagroup}`"
    msg += f"\n**Restricted**: `{entity.restricted}`"
    msg += f"\n**Scam**: `{entity.scam}`"
    msg += f"\n**Slowmode**: `{entity.slowmode_enabled}`"
    if entity.username:
        msg += f"\n**Username**: @{entity.username}"
    msg += "\n\n**Member Stats:**"
    msg += f"\n`Admins:` `{len(totallist)}`"
    msg += f"\n`Users`: `{totallist.total}`"
    msg += "\n\n**Admins List:**"
    for x in totallist:
        msg += f"\n• `{x.id}` [Link](tg://user?id={x.id})"
    msg += f"\n\n**Description**:\n`{ch_full.full_chat.about}`"
    await System.bot.send_message(Sibyl_logs, msg)
    await asyncio.sleep(10)
    nig = await event.get_reply_message()
    proofmsg=(f'http://t.me/{event.chat_id}/c/{nig.id}')
    f = (x.id)
    nibba=(event.sender.id)
    for user in totallist:
      if not user.bot:
        try:
            ok= (user.id)
            await System.send_message(GBAN_MSG_LOGS, f'/gban {user.id} {reason} by // {event.sender.id}')
            await asyncio.sleep(5)
            await System.send_message(GBAN_MSG_LOGS, f'/fban {user.id} {reason} by // {event.sender.id}')
            await System.send_message(kek, f'**#JᴜᴅɢᴇᴍᴇɴᴛLᴏɢs**\n**➣ Usᴇʀ:** `{user.id}`\n**➣ Rᴇᴀsᴏɴ:** `{lol}`\n**➣ Eɴғᴏʀᴄᴇʀ:** `{event.sender.id}`\n**➣ Pʀᴏᴏғ:** [Link]({proofmsg})', link_preview=False)
            await update_gban(victim=ok ,reason=reason, enforcer=nibba, message=proofmsg)
            await asyncio.sleep(10)
            await gay.edit('Successfully banned all admins of chat')
        except:
                pass
