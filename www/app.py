import logging; logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from  datetime import datetime
from aiohttp import web
import orm,sys
from coroweb import get, add_route, add_static
from jinja2 import environment,FileSystemLoader

@get('/')
def index(request):
    users = yield from User.findAll()
    return {
        '__template__': 'test.html',
        'user': users
    }

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info("server started at http://127.0.0.1:9000...")
    return srv

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()

