import aiohttp
import asyncio

def download_complete_back(task_obj):
    print('下载结果是：',task_obj.result())

async def baidu_spider():
    url='https://www.baidu.com'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response= await response.text()
            return response

async def jingdong_spider():
    url='https://www.jd.com'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response= await response.text()
            return response
        
async def sougou_spider():
    url='https://www.sogou.com'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response= await response.text()
            return response

async def main():
    task_baidu=asyncio.create_task(baidu_spider())
    task_baidu.add_done_callback(download_complete_back)

    task_jingdong=asyncio.create_task(jingdong_spider())
    task_jingdong.add_done_callback(download_complete_back)

    task_sogou=asyncio.create_task(sougou_spider())
    task_sogou.add_done_callback(download_complete_back)

    tasks=[task_baidu,task_jingdong,task_sogou]

    await asyncio.wait(tasks)

if __name__=='__main__':
    asyncio.run(main())