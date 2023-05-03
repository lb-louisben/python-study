# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : mutex.py
@Author     : louis
@Date       : 5/3/23 17:17

fix: 当多个进程操作同一份数据的时候, 会出现数据错乱的问题, 解决方法就是加锁处理
     把并发变成串行,量然牺牲了运行效率,但是保证了数据的安全
"""
import json
import random
import time
from multiprocessing import Process, Lock, set_start_method


# 查票
def search_ticket(name):
    # read the file to get the total tickets number
    with open('./data/tickets', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    print(f'用户{name}查询余票：{dic.get("tickets_num")}')


# 买票
def buy_tickets(name):
    with open('./data/tickets', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    # 模拟网络延迟
    time.sleep(random.randint(1, 5))
    if dic.get("tickets_num") > 0:
        dic["tickets_num"] -= 1
        with open('./data/tickets', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print(f'用户{name}买票成功')
    else:
        print(f'余票不足, 用户{name}买票失败')


def task(name, mutex):
    search_ticket(name)
    mutex.acquire() # 抢锁
    buy_tickets(name)
    mutex.release() # 释放锁


if __name__ == '__main__':
    set_start_method('fork')
    mutex = Lock()
    for i in range(1, 9):
        p = Process(target=task, args=(i, mutex))
        p.start()
