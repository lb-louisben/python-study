# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : create_process.py
@Author     : louis
@Date       : 5/3/23 15:58 
"""

from multiprocessing import Process
import time

def func(name):
    print(f'{name}任务开始')
    time.sleep(5)
    print(f'{name}任务结束')

if __name__ == '__main__':
    p = Process(target=func, args=('学习',))
    p.start()
    print('main process')

