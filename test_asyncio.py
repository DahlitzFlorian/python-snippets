import asyncio
import aiohttp
import async_timeout


urls = [
    "http://www.google.com",
    "http://www.yandex.ru",
    "http://www.python.org"]


async def call_url(url):
    print('Starting {}'.format(url))
    response = None
    async with aiohttp.ClientSession() as session:
        async with async_timeout.timeout(10):
            async with session.get(url) as response:
                data = await response.text()
    print('{}: {} bytes: {}'.format(url, len(data), data))
    return data


futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
