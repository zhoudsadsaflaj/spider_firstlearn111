import asyncio

async def test():
    print('----test----')
    return 100


def callback_after_done(task_obj):
    print('task:',task_obj)
    print('状态:',task_obj.done())
    print('返回值:',task_obj.result())
    print('')

async def main():
    task=asyncio.create_task(test())
    task.add_done_callback(callback_after_done)
    tasks=[task]
    
    await asyncio.wait(tasks)

if __name__=='__main__':
    asyncio.run(main())