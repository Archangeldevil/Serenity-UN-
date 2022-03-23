from Serenity import (
    System,
    system_cmd,
    make_collections,
    INSPECTORS,
    SIBYL,
    ENFORCERS,
    Sibyl_logs,
)
from Serenity.strings import on_string
import logging
import importlib
import asyncio
import time

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
) 

from Serenity.plugins import to_load

HELP = {}
IMPORTED = {}
FAILED_TO_LOAD = {}

for load in to_load:
    try:
        imported = importlib.import_module("Serenity.plugins." + load)
        if not hasattr(imported, "__plugin_name__"):
            imported.__plugin_name__ = imported.__name__

        if not imported.__plugin_name__.lower() in IMPORTED:
            IMPORTED[imported.__plugin_name__.lower()] = imported

        if hasattr(imported, "help_plus") and imported.help_plus:
            HELP[imported.__plugin_name__.lower()] = imported
    except Exception as e:
        print(f"Error while loading plugin: {load}")
        print("------------------------------------")
        print(e)
        FAILED_TO_LOAD[load] = e
        print("------------------------------------")


@System.on(system_cmd(pattern=r"status", allow_enforcer=True))
async def status(event):
    msg = await event.reply("Connecting to Serenity Database")
    time.sleep(1)
    await msg.edit("Initialising ▫️◾️▫️")
    time.sleep(0.1)
    await msg.edit("Initialising ◾️▫️◾️")
    time.sleep(0.1)
    await msg.edit("Initialising ▫️◾️▫️")
    time.sleep(0.1)
    await msg.edit("Initialising ◾️▫️◾️")
    time.sleep(0.1)
    await msg.edit("Initialising ▫️◾️▫️")
    time.sleep(0.1)
    await msg.edit("Initialising ◾️▫️◾️")
    time.sleep(0.1)
    await msg.edit("Initialising ▫️◾️▫️")
    time.sleep(2)
    await msg.edit("Connection successful!")
    time.sleep(1)
    senderx = await event.get_sender()
    if event.sender.id in SIBYL:
        user_status = "**Chief**"
    elif event.sender.id in INSPECTORS:
        user_status = "**UN Head**"
    else: 
        user_status = "**Official**"
    time.sleep(1)
    await msg.edit(on_string.format(Enforcer=user_status, name=senderx.first_name))


@System.on(system_cmd(pattern="serenity stats"))
async def stats(event):
    msg = f"Processed {System.processed} messages since last restart."
    msg += f"\n{len(ENFORCERS)} Enforcers & {len(INSPECTORS)} Inspectors"
    g = 0
    async for d in event.client.iter_dialogs(limit=None):
        if d.is_channel and not d.entity.broadcast:
            g += 1
        elif d.is_group:
            g += 1
    msg += f"\nModerating {g} Groups"
    await event.reply(msg)


# @System.on(system_cmd(pattern=r"help", allow_slash=False, allow_inspectors=True))
# async def send_help(event):
#     try:
#         help_for = event.text.split(" ", 1)[1].lower()
#     except IndexError:
#         msg = "List of plugins with help text:\n"
#         for x in HELP.keys():
#             msg += f"`{x.capitalize()}`\n"
#         await event.reply(msg)
#         return
#     if help_for in HELP:
#         await event.reply(HELP[help_for].help_plus)
#     else:
#         return


async def main():
    try:
        await make_collections()
        me = await System.bot.get_me()
        System.bot.id = me.id
    except Exception as e:
        FAILED_TO_LOAD["main"] = e
    await System.start()
    await System.catch_up()
    if FAILED_TO_LOAD:
        msg = "Few plugins failed to load:"
        for plugin in FAILED_TO_LOAD:
            msg += f"\n**{plugin}**\n\n`{FAILED_TO_LOAD[plugin]}`"
        await System.send_message(Sibyl_logs, msg)
    else:
        await System.send_message(Sibyl_logs, "I'm alive!")
    await System.run_until_disconnected()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
