# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : mutex.py
@Author     : louis
@Date       : 5/3/23 17:17 
"""
import json
import random
import time
from multiprocessing import Process


# 查票
def search_ticket(name):
    # read the file to get the total tickets number
    with open('data/tickets', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    print(f'用户{name}查询余票：{dic.get("tickets_num")}')


# 买票
def buy_tickets(name):
    with open('data/tickets', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    # 模拟网络延迟
    time.sleep(random.randint(1, 5))
    if dic.get("tickets_num") > 0:
        dic["tickets_num"] -= 1
        with open('data/tickets', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print(f'用户{name}买票成功')
    else:
        print(f'用户{name}买票失败')


def task(name):
    search_ticket(name)
    buy_tickets(name)


if __name__ == '__main__':
    for i in range(1, 9):
        p = Process(target=task, args=(i,))
        p.start()
