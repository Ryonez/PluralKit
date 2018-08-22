import asyncio

import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from pluralkit import bot

loop = asyncio.get_event_loop()
loop.run_until_complete(bot.run())
