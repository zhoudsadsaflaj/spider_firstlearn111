from aiohttp import ClientSession
import asyncio

tasks=[]
url='https://baidu.com'

async def get_baidu(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response= await response.text()
            print(response)

if __name__=='__main__':
    asyncio.run(get_baidu(url))