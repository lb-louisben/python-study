# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : login.py
@Author     : louis
@Date       : 5/10/23 10:35 
"""

input_username = input("请输入用户名>>>").strip()
input_password = input("请输入密码>>>").strip()

with open('../../data/userinfo', mode='rt', encoding='utf-8') as f:
   for line in f:
       username, password = line.strip().split('=====')
       if username == input_username and password == input_password:
           print('登录成功'.center(80,'-'))
           break
   else:
       print('登录失败，用户名或密码错误'.center(80,'-'))