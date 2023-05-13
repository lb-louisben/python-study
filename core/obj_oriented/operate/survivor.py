# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : survivor.py
@Author     : louis
@Date       : 5/12/23 16:23 
"""

class Survivor:
    clazz = '求生者'
    def __init__(self, real_name, job):
        self.real_name = real_name
        self.job = job

class Decode(Survivor):
    category = '破译'

class Assist(Survivor):
    category = '辅助'

class Contain(Survivor):
    category = '牵制'

class Rescue(Survivor):
    category = '救援'



class Move:
    def __init__(self, sur_name, run_speed, walk_speed, squat_speed, crawl_speed):
        self.__sur_name = sur_name
        self.__run_speed = run_speed
        self.__walk_speed = walk_speed
        self.__squat_speed = squat_speed
        self.__crawl_speed = crawl_speed

    def get_name(self):
        print(self.__sur_name)

    def set_run_speed(self, run_speed):
        self.__run_speed = run_speed
