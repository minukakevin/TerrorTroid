"""Send Chat Actions
Syntax: .scha <option> <time in sec>
        scha options: Options for sca 

typing
contact
game
location
voice
round
video
photo
document
cancel"""

import asyncio
from uniborg.util import admin_cmd
 
 
@borg.on(admin_cmd("scha ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    action = input_str if (input_str := event.pattern_match.group(1)) else "typing"
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(86400)  # type for 10 seconds
