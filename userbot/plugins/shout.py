"""Shouts a message in MEME way
usage: .shout message
originaly from : @corsicanu_bot
"""

import sys
from telethon import events, functions
from userbot.utils import admin_cmd
import random


@borg.on(events.NewMessage(pattern=r"\.shout", outgoing=True))
async def shout(args):
    if args.fwd_from:
        return
    msg = "```"
    messagestr = args.text
    messagestr = messagestr[7:]
    text = " ".join(messagestr)
    result = [' '.join(list(text))]
    result.extend(
        f'{symbol} ' + '  ' * pos + symbol
        for pos, symbol in enumerate(text[1:])
    )

    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    await args.edit("`" + ("\n" + result) + "`")
        
    
    
