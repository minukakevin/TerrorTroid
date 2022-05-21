#Modded from dagd.py
"""
Animate How To Google
Command .ggl Search Query
By @loxxi
"""

from telethon import events
import os
import requests
import json
from userbot.utils import admin_cmd


@borg.on(admin_cmd("ggl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = f'https://da.gd/s?url=https://lmgtfy.com/?q={input_str.replace(" ", "+")}%26iie=1'

    if response_api := requests.get(sample_url).text:
        await event.edit("[{}]({})\n`Thank me Later 🙃` ".format(input_str,response_api.rstrip()))
    else:
        await event.edit("something is wrong. please try again later.")
