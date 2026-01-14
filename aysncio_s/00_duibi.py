import time
import asyncio

'''同步代码，一次执行一行，总耗时5s'''
# def hello():
#     time.sleep(1)

# def run():
    
#     for _ in range(5):
#         hello()
#         print('HELLO WORLD:%s'%time.time())

"""异步代码，这里总耗时1s"""
async def hello():
    await asyncio.sleep(1)
    print('HELLO WORLD:%s'%time.time())

async def run():
    tasks=list()
    for i in range(500):
        #这里切记使用之前需要先创建任务列表
        tasks.append(asyncio.create_task(hello()))
    
    await asyncio.wait(tasks)

    


if __name__=='__main__':
    #run()
    asyncio.run(run())