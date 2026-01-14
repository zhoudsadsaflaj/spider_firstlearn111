import asyncio

def test1():
    '''同步函数'''
    print('i am test1')
    return 1

async def test2():
    '''异步函数'''
    print('i am test2')
    return 2

'''这里直接调用函数实际上是创建了一个协程对象，不会触发内部的内容'''

'''
调用后显示
i am test1
返回值是 1
'''
print('返回值是',test1())
'''
调用后显示：返回值是 <coroutine object test2 at 0x000001D712719600>
'''
print('返回值是',test2())


'''调用异步函数使用asyncio.run来进行运行'''
print(asyncio.run(test2()))

'''
显示为：
i am test2
2
'''