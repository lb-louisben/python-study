# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : producer_consumer_problem.py
@Author     : louis
@Date       : 5/3/23 18:13 
"""
import random
import time
from multiprocessing import Queue, Process, set_start_method, JoinableQueue


def producer(name, food, queue):
    for i in range(8):
        time.sleep(random.randint(1,3))
        print(f'{name}生产了{food}{i}')
        queue.put(f'{food}{i}')



def consumer(name, queue):
    while True:
        food = queue.get()
        time.sleep(random.randint(1,3))
        print(f'{name}吃了{food}')

        queue.task_done()   # 告诉队列已经拿走了一个数据，并且已经处理完啦


if __name__ == '__main__':
    set_start_method('fork')

    queue = JoinableQueue()
    p1 = Process(target=producer, args=('中华小当家', '黄金炒饭', queue))
    p2 = Process(target=producer, args=('神厨小富贵', '佛跳墙', queue))

    c1 = Process(target=consumer, args=('张三', queue))
    c2 = Process(target=consumer, args=('里斯', queue))

    p1.start()
    p2.start()

    c1.daemon = True
    c2.daemon = True

    c1.start()
    c2.start()

    p1.join()
    p2.join()

    queue.join()    # 等待队列中所有数据被取完