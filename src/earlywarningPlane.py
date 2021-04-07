import numpy as np
import math
import random
from cplane import Plane
from bomber import Bomber
from reconnaissancePlane import ReconnaissancePlane
from earlyWarningControlRadar import EarlyWarningControlRadar

class EarlyWarningPlane(ReconnaissancePlane):
    def __init__(self, id, init_data):
        #初始化数据
        self.init_data = init_data
        #飞机的数量
        self.id = id
        #飞机携带的雷达
        self.radar = EarlyWarningControlRadar()
        #保存数据
        self.Q = []
        #爬升率 随高度上升爬升率下降
        self.rate_of_climb = [305, 283, 100, 12]
        if(self.init_data[2] > 0 and self.init_data[2] < 1000):
            #飞机的各种属性 最大速度 加速度
            self.plane_attr = [1470, 30, self.rate_of_climb[0]]
        if(self.init_data[2] > 1000 and self.init_data[2] < 10000):
            self.plane_attr = [1470, 30, self.rate_of_climb[1]]
        if(self.init_data[2] > 10000 and self.init_data[2] < 17000):
            self.plane_attr = [1470, 30, self.rate_of_climb[2]]
        if(self.init_data[2] >= 17000):
            self.plane_attr = [1470, 30, self.rate_of_climb[3]]