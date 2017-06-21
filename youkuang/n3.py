# -*- coding: utf-8 -*-
"""

"""
import asyncio


async def http_get(host=''):
    """http fetch."""
    reader, writer = await asyncio.open_connection(host=host, port=80)

    writer.write(b'\r\n'.join([
        b'GET / HTTP/1.1',
        b'Host: %b' % host.encode('utf-8'),
        b'Connection: close',
        b'', b''
    ]))

    async for line in reader:
        print('>>> ', line)

    writer.close()


async def coro(name, lock):
    print('coro {}: waiting for lock.'.format(name))
    async with lock:
        print('->', name)
        await asyncio.sleep(1)
        print()

loop = asyncio.get_event_loop()

if __name__ == '__main__':
    loop.run_until_complete(http_get('baidu.com'))
    loop.close()
