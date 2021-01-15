# def consumer():
#     r = 'start'
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Cunsuming %s...' % n)
#         r = '200 OK'
# def produce(c):
#     r = c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER]] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER]] Cunsumer return %s...' % r)
#     c.close()


# if '__main__' == __name__:
#     c = consumer()
#     produce(c) 


# import asyncio

# @asyncio.coroutine
# def hello():
#     print('Hello world!')
#     r = yield from asyncio.sleep(1)
#     print('Hello again!')

# loop = asyncio.get_event_loop()


# loop.run_until_complete(hello())
# loop.close()


# import threading
# import asyncio

# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()



# import asyncio

# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()

# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.baidu.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# import asyncio

# async def hello():
#      print('Hello world!')
#      r = await asyncio.sleep(1)
#      print('Hello again!')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


import asyncio
from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>Index</h1>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
print('ffff')
print(1)

