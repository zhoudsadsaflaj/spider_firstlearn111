import asyncio

async def test1():
    print(1111111)
    return 100

async def main():
    task=asyncio.create_task(test1())
    tasks=[task]
    await asyncio.wait(tasks)
    print('状态：',task.done())
    print('返回值：',task.result())
    

if __name__=='__main__':
    asyncio.run(main())