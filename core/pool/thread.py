# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : thread.py
@Author     : louis
@Date       : 5/13/23 17:16 
"""
import time
from concurrent.futures import ThreadPoolExecutor

# default is cpu_count * 5
pool = ThreadPoolExecutor(10)


def task(name):
    print(name)
    time.sleep(3)
    return name + 10


f_list = []

for i in range(50):
    future = pool.submit(task, i)
    f_list.append(future)

pool.shutdown()  # 等待进程池的任务结束后关闭

for f in f_list:
    print('任务结果：', f.result())
