# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : identity5.py
@Author     : louis
@Date       : 5/10/23 14:38 
"""


class Survivors:
    count = 0
    def __init__(self, sur_name, category, run_speed, walk_speed, squat_speed, crawl_speed):
        self.sur_name = sur_name
        self.category = category
        self.run_speed = run_speed
        self.walk_speed = walk_speed
        self.squat_speed = squat_speed
        self.crawl_speed = crawl_speed
        self.property = []
        Survivors.count += 1

    def set_survivor_run_speed(self, speed_plus):
        self.run_speed += speed_plus

    def get_survivor_data(self):
        print(f'求生者姓名: {self.sur_name}, 类型: {self.category}, 跑动速度: {self.run_speed}, '
              f'走路速度: {self.walk_speed}, 蹲走速度: {self.squat_speed}, 爬行速度: {self.crawl_speed}')

    def get_prop(self, prop_name):
        self.property += prop_name

s1 = Survivors('伊莱·克拉克', '辅助', 3.8, 2.11, 1.14, 0.44)
s1.get_prop('役鸟')
s1.get_survivor_data()
