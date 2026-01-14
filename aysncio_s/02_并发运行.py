import asyncio

async def test1():
    for _ in range(3):
        print('------')
        await asyncio.sleep(1)#在程序运行的时候，会检测到awit延时，此时不管延时内容是多少都会将主动权交给其他任务。
        print('++++++')

async def test2():
    for _ in range(5):
        print('*******')
        await asyncio.sleep(1)
        print('$$$$$$$')


'''在main中创建新的协程对象，在这里面将test1和test2结合。'''
async def main():
    await asyncio.gather(test1(),test2())

if __name__=='__main__':
    asyncio.run(main())