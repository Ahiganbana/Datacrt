import numpy as np
import math
import random
from matplotlib import pyplot as plt
from firecontrolradar import FireControlRadar
from cplane import Plane

class Fighter(Plane):
    """
    战斗机 
    具有的动作:
    直线 转弯 爬升 俯冲 筋斗 上升转弯
    """
    def __init__(self, id, init_data):
        #初始化数据
        self.init_data = init_data
        #飞机的编号
        self.id = id
        #飞机携带的雷达
        self.radar = FireControlRadar()
        #保存数据 
        self.Q = []
        #爬升率 随高度上升爬升率下降
        self.rate_of_climb = [305, 283, 100, 12]
        if(self.init_data[2] > 0 and self.init_data[2] < 1000):
            #飞机的各种属性 最大速度 加速度 爬升率
            self.plane_attr = [1470, 30, self.rate_of_climb[0]]
        if(self.init_data[2] > 1000 and self.init_data[2] < 10000):
            self.plane_attr = [1470, 30, self.rate_of_climb[1]]
        if(self.init_data[2] > 10000 and self.init_data[2] < 17000):
            self.plane_attr = [1470, 30, self.rate_of_climb[2]]
        if(self.init_data[2] >= 17000):
            self.plane_attr = [1470, 30, self.rate_of_climb[3]]
        
    def turn_up(self):
        """
        上升转弯机动
        """
        t = self.creatT(self.init_data[2], 1) / 3
        t1 = random.uniform(t / 4, t / 2)  #生成第一段动作运动时间
        a1 = random.uniform(5,10)
        a2 = 0 - a1
        self.trackdive(self.init_data, t, a1, a2, t1)
        v = self.Q[len(self.Q) - 1][5]
        radius = (v*t) / (2*math.pi)
        print(radius)
        self.turn_trace(self.init_data, abs(radius), t)
    
    def turn_trace(self, p0, radius, t):
        """
        上升过后完成转弯（小半径、回旋到最开始的位置）
        """
        p1 = p0
        #下降的速率
        za = self.plane_attr[2]
        #p1[4] = random.uniform( -math.pi / 2, -math.pi)
        for i in range(int(t * 100)):
            data = [0, 0, 0, 0, 0, 0, 0,0]
            for j in range(len(p1)):
                data[j] = p1[j]
            w = p1[5]/radius

            p1[0] = 1/3.94 * p1[5] * 1/100 * math.sin(p1[3]) * math.cos(p1[4]) + p1[0]
            p1[1] = 5.5 * p1[5] * 1/100 * math.cos(p1[3]) * math.cos(p1[4]) + p1[1]
            p1[2] = p1[2] - za * 1 / 100
            #俯仰角改变
            p1[4] = p1[4] + 1/ 100 * p1[7] / p1[5]
            #航向角改变
            p1[3] = (p1[3] + 1/100 * w)
            #p1[0] = p1[5] * 1/100 * math.sin(p1[3]) + p1[0]
            #p1[1] = p1[5] * 1/100 * math.cos(p1[3]) + p1[1]
            #p1[4] = p1[4] + p1[5] * 1/100 / radius*math.pi
            #速度                     
            p1[5] = p1[5] + 1/100 * p1[6]
            #切向加速度
            p1[6] = -1
            p1[7] = w * w / radius
            self.Q.append(data)


    def somersault(self, p0, t):
        """
        筋斗机动
        """
        p1 = p0
        amax = self.plane_attr[1]
        vmax = self.plane_attr[0]
        #第一阶段 直线飞行加速
        self.trackline(p0, t / 3, 1, amax, 3, vmax)
        #第二阶段 爬升阶段
        t1 = self.creatT(p1[2], 1)
        v = self.Q[len(self.Q) - 1][5]
        print(v)
        radius = (v*t1) / (2*math.pi)
        print(radius)
        self.vertical_rise(p1, t1, radius/2)
        #print(self.Q[0])
        #print("-----")
        #第三阶段 直线飞行阶段
        #self.trackdive(p0, t1 / 2, a1, a2, t2, self.plane_attr[2])
        self.trackline(p0, t / 3, 1, amax, 3, vmax)
        #print(self.Q[len(self.Q) - 1])
    
    def vertical_rise(self, p0, t, radius):
        """
        飞机的垂直上升运动
        """
        p1 = p0
        for i in range(int(t*100)):   #每0.01秒产生一个数据
            data = [0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(len(p1)):
                data[j]=p1[j]
            if(p1[2] > 0 and p1[2] < 1000):
                za = 305
            elif(p1[2] >= 1000 and p1[2] < 10000):
                za = 100
            elif(p1[2] >= 1000 and p1[2] < 17000):
                za = 58
            else:
                za = 12
            w = p1[5] / radius
            #x坐标
            p1[0] = p1[5] * 1/100 * math.sin(p1[3])*math.cos(p1[4]) + p1[0]
            #y坐标
            p1[1] = p1[5] * 1/100 * math.cos(p1[3])*math.cos(p1[4]) + p1[1]
            #z坐标
            #1[2] = p1[5] * 1/100 * math.sin(p1[4]) + p1[2]
            p1[2] = p1[2] + 1/2 * za * (1/100 * 1/100) + p1[5] * 1/100 * math.sin(p1[4])
            #p1[2] = self.rate_of_climb[0] * 1/ 100 + p1[2]
            #航向角
            #p1[3] = p1[3] + 1 / 100 * w
            #俯仰角改变
            p1[4] = p1[4] + 1/ 100 * p1[7] / p1[5]
            p1[5] = p1[5] + 1/ 100 * p1[6]  # 切向加速度
            p1[6] = -1
            p1[7] = w*w*radius
            #print(data)
            self.Q.append(data)

    


