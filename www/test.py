import orm
from models import User,Blog,Comment
import asyncio

async def test(loop):
    await orm.create_pool(user='root',password="",db="ZilyWeb",loop=loop)

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()