# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : process.py
@Author     : louis
@Date       : 5/13/23 17:30 
"""

import time
import os
from concurrent.futures import ProcessPoolExecutor

pool = ProcessPoolExecutor()


def call_back(res):
    print('call-back: ', res.result())


def task(name):
    print(name, os.getpid())
    time.sleep(3)
    return name + 11


if __name__ == '__main__':
    f_list = []

    for i in range(50):
        pool.submit(task, i).add_done_callback(call_back)
    #     future = pool.submit(task, i)
    #     f_list.append(future)
    #
    # pool.shutdown()
    #
    # for f in f_list:
    #     print('结果：', f.result())
