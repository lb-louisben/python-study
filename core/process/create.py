# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : create.py
@Author     : louis
@Date       : 5/11/23 15:51 

@aim: 如何创建进程
"""

# way 1
from multiprocessing import Process
import time


def func(name):
    print(f'{name}, we need to take a bus!!!!')
    time.sleep(5)
    print(f'{name}, we arrived.')

class MyProcess:
    def __init__(self, name):
        super().__init__()
        self.process_name = name

    def run(self):
        print(f'{self.process_name}任务开始')
        time.sleep(4)
        print(f'{self.process_name}任务完成')

if __name__ == '__main__':
    '''
    方法一：
    '''
    # # 得到进程的操作对象
    # p1 = Process(target=func, args=('Alex',))
    # # 创建进程
    # p1.start()
    '''
    方法二：面向对象
    '''
    p2 = MyProcess('写作业')
    p2.run()

    print("main process.")
