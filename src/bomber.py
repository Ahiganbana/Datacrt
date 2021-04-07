from terrainTrackingRadar import TerrainTrackingRadar
from cplane import Plane
import random
import math
import numpy as np

class Bomber(Plane):
    """
    轰炸机
    拥有左迂回和右迂回
    直线、转弯、爬升、俯冲的行动模式
    """
    def __init__(self, id, init_data):
        #init_data包括 初始x,y,z,距离,仰角,速度,切向加速度,法相加速度
        self.init_data = init_data
        #飞机的最大速度,最大加速度,最大爬升率
        self.plane_attr = [850, 20, 35]
        self.id = id
        self.radar = TerrainTrackingRadar()
        self.Q=[]
    
    def round_left(self, p0, t):
        """
        左迂回轨迹函数
        p0:初始序列
        t : 时间
        """
        p1 = p0
        radius = random.uniform(7000,7500)
        w = p1[5] / radius
        for i in range(int(t*100)):   #每0.01秒产生一个数据
            data = [0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(len(p1)):
                data[j]=p1[j]
            #x坐标
            p1[0] = p1[5] * 1/100 * (math.sin(p1[3])) + p1[0]
            #y坐标
            p1[1] = p1[5] * 1/100 * (math.cos(p1[3])) + p1[1]
            #距离
            p1[4] = math.sqrt(p1[0]*p1[0] + p1[1]*p1[1] + p1[2]*p1[2])
            #切向加速度
            p1[6] = 0
            #速度                       
            p1[5] = p1[5] + 1/100*p1[6]
            #print(data)
            #第二段迂回阶段
            if (i/100 >= t / 3) and (i / 100 < 2* t / 3) and (p1[5]*math.sin(p1[4]) < self.plane_attr[0]):
                #x坐标
                p1[0] = p1[5] * 1/100 * (math.sin(p1[3])) + p1[0]
                #y坐标
                p1[1] = p1[5] * 1/100 * (math.cos(p1[3])) + p1[1]
                #法向加速度 
                p1[7] = w*w*radius
                #航向角
                p1[3] = p1[3] + 1 / 100 * w
                
            elif i/100 >= 2 * t / 3:
                #x坐标
                p1[0] = p1[5] * 1/100 * (math.sin(p1[3])) + p1[0]
                #y坐标
                p1[1] = p1[5] * 1/100 * (math.cos(p1[3])) + p1[1]                
                p1[7] = 0
                p1[3] = p0[3]
            self.Q.append(data)
        # self.radar.amount = len(self.Q)
        # #print(self.Q)
        # self.Q = np.array(self.Q)
        # #print(len(self.Q))
        # self.radar.createData(self.Q[:,4])
    
    def round_right(self, p0, t):
        p1 = p0
        p1[3] = p1[3] + math.pi
        self.round_left(p1, t)