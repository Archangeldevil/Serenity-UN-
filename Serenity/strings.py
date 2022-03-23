on_string = """
     「✭USER INFO ✭」
 
⦿ Name -  {name}
⦿ Rank  - {Enforcer}

✭Verified User ✓
"""

# Make sure not to change these too much
# If you still wanna change it change the regex too
scan_request_string = """
$SBAN
「 sʙᴀɴ ᴄᴀʟʟ! 」
**Oғғɪᴄɪᴀʟ:** {enforcer} 
**ᴜsᴇʀ sʙᴀɴɴᴇᴅ:** {spammer}
**ʀᴇᴀsᴏɴ:** `{reason}`
**ʀᴏᴏᴛ:** {chat}
**ᴏʙᴊᴇᴄᴛɪᴠᴇ ᴍᴇssᴇɢᴇ:** `{message}`
"""
forced_scan_string = """
$ENFORCED
**UN Hᴇᴀᴅ:** {ins}
**ᴜsᴇʀ sʙᴀɴɴᴇᴅ:** {spammer}
**ʀᴇᴀsᴏɴ:** `{reason}`
**ʀᴏᴏᴛ:** {chat}
**ᴏʙᴊᴇᴄᴛɪᴠᴇ ᴍᴇssᴇɢᴇ:** `{message}`
"""
group_admin_scan_string = """
$ENFORCED CHAT-SBAN
**UN Hᴇᴀᴅ**: {ins}
*ᴇɴғᴏʀᴄᴇᴅ ᴄʜᴀᴛ**: {t_chat}
**Reason**: `{reason}`
**ʀᴏᴏᴛ**: {chat}
**Chat Owner**: 
`{owner_id}`
**Admins**: `{admins}`
"""

group_admin_request_string = """
$CHAT-BAN
Group Ban Request!
**Oғғɪᴄɪᴀʟ**: {enf}
**ᴇɴғᴏʀᴄᴇᴅ ᴄʜᴀᴛ**: {t_chat}
**Reason**: `{reason}`
***ʀᴏᴏᴛ**: {chat}
**Chat Owner**: 
`{owner_id}`
**Admins**: `{admins}`
"""

revert_request_string = """
$UNSBAN
Unsban request!
**Oғғɪᴄɪᴀʟ:** `{enforcer}`
**ᴜsᴇʀ ᴛᴏ ᴜɴsʙᴀɴ:** `{spammer}`
**ᴜɴsʙᴀɴ ʀᴏᴏᴛ:** {chat}
"""

revert_reject_string = """
$DECLINED
**sʙᴀɴɴᴇᴅ:** `yes`
User is gbanned. Unsban call declined
"""


reject_string = """
$DECLINED
**sʙᴀɴɴᴇᴅ ** `No`
User is not sbanned, Call declined.
"""

proof_string = """
**Case file for** - {proof_id} :
┣━**Rᴇᴀsᴏɴ**: {reason}
┗━**Message**
         ┣━[Nekobin]({paste})
         ┗━[DelDog]({url})"""

scan_approved_string = """
「 sʙᴀɴɴᴇᴅ ʀᴇsᴜʟᴛ 」
**Tᴀʀɢᴇᴛ Usᴇʀ:** {scam}
**Cʀɪᴍᴇ Stats:** `Over 300`
**Rᴇᴀsᴏɴ:** `{reason}`
**Enforcer:** `{enforcer}`
**Cᴀsᴇ Nᴜᴍʙᴇʀ:** `{proof_id}`
"""

bot_gban_string = """
#DestroyDecomposer
**Enforcer:** `{enforcer}`
**Target User:** {scam}
**Reason:** `{reason}`
"""

report_by_user = """
**Report By User**

**Inspector:** {exu}
**Target:** {userr}
**Reason:** {reasonn}
**Reason By User:** {reason}
"""

# https://psychopass.fandom.com/wiki/Crime_Coefficient_(Index)
# https://psychopass.fandom.com/wiki/The_Dominator
