import numpy as np
import math
import random
from cplane import Plane
from bomber import Bomber
from guideradar import GuideRadar

class Helicopter(Bomber):
    def __init__(self, id, init_data):
        #初始化数据
        self.init_data = init_data
        #飞机的数量
        self.id = id
        #飞机携带的雷达
        self.radar = GuideRadar()
        #保存数据
        self.Q = []
        #飞机的各种属性 最大速度  最大加速度 爬升率
        self.plane_attr = [140, 30, 200]