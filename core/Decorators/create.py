# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : create.py
@Author     : louis
@Date       : 5/11/23 16:55 
"""
import time
from functools import wraps


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        input_name = input('请输入账户名称: >>>').strip()
        input_pwd = input('请输入账户密码: >>>').strip()
        with open('../../data/userinfo', mode='rt', encoding='utf-8') as f:
            for line in f:
                username, password = line.strip().split('=====')
                if username == input_name and password == input_pwd:
                    print('登录成功'.center(80, '-'))
                    res = func(*args, **kwargs)
                    return res
                    break
            else:
                print('登录失败，用户名或密码错误'.center(80, '-'))

    return wrapper


@auth
def home():
    """
    this is the home page info
    :return: none
    """
    time.sleep(2)
    print('welcome...')


if __name__ == '__main__':
    home()
    print(home.__doc__)
