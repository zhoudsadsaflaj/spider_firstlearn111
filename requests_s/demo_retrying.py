from retrying import retry

import time

num=1

@retry(stop_max_attempt_number=3)
def test():
    global num
    print(f'num={num}')
    num+=1
    time.sleep(1)
    for i in 10:
        print(i)


if __name__=='__main__':
    try:
        test()
    except Exception as e:
        print('产生异常',e)