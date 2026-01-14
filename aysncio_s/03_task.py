import asyncio
import time

async def test1():
    print('='*50)
    print('test1开始时间：',time.time())
    for _ in range(3):
        print('------')
        await asyncio.sleep(1)
        print('++++++')
    print('test1结束时间：',time.time())
    print('='*50)

async def test2():
    print('='*50)
    print('test2开始时间：',time.time())
    for _ in range(5):
        print('*******')
        await asyncio.sleep(1)
        print('$$$$$$$')
    print('test2结束时间：',time.time())
    print('='*50)


async def main():
    print('='*50)
    task1=asyncio.create_task(test1())
    task2=asyncio.create_task(test2())
    tasks=[task1,task2]
    print('test1结束没?',task1.done())
    print('test2结束没?',task2.done())
    '''await的意思是等后面的任务运行结束'''
    await asyncio.wait(tasks)
    print('test1结束没?',task1.done())
    print('test2结束没?',task2.done())
    print('='*50)


if __name__=='__main__':
    start_time=time.time()
    asyncio.run(main())
    stop_time=time.time()
    print('总花费：',stop_time-start_time)