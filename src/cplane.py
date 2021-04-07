import numpy as np
import math
import random
from matplotlib import pyplot as plt
from cradar import Radar
class Plane(object):
    """
    飞机实体类,维护飞机的各种属性
    """
    def __init__(self, id, p0):
        self.p0 = p0          #初始数据
        self.radar = Radar(1)
        #保存数据
        self.Q = []
        self.plane_attr = [650, 30, 35]

    #加速度生成函数
    def creata(self, t, amax, aa): #aa是加加速度，设为常数
        if t <= (2*math.sqrt(amax/aa)):
            a = amax-aa*math.pow((t-math.sqrt(amax/aa)), 2)
        else:
            a = 0
        return a
    #爬升俯冲时间生成函数，爬升时当前高度越高，则将要爬升的高度越小即时间越短，反之，时间越长。俯冲可类比之
    def creatT(self, z, Fz):
        t = 0
        if Fz < 0:  #判断是俯冲
            if z <= 10000:
                t = 20 * math.exp((z - 10000) / 3000)
            else:
                t = 20 * (2-math.exp((10000-z) / 3000))
        elif Fz > 0: #判断是爬升
            if z <=10000:
                t = 20 * (2-math.exp((z - 10000) / 3000))
            else:
                t = 20 * math.exp((10000-z) / 3000)
        #时间较小则忽略不计，即当前高度不允许爬升或俯冲
        if t >= 1:
            return t
        else:
            return 0
    #直线动作函数
    def trackline(self, p0, t, F, amax, aa, vmax):
        p1 = p0
        for i in range(int(t*100)):   #每0.01秒产生一个数据
            data = [0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(len(p1)):
                data[j]=p1[j]
            p1[0] = p1[5] * 1/100 * (math.sin(p1[3])) + p1[0] #X坐标
            p1[1] = p1[5] * 1/100 * (math.cos(p1[3])) + p1[1] #Y坐标
            p1[5] = p1[5] + 1/ 100 * p1[6]                    #速度
            p1[4] = 0                                           #俯仰角
            p1[7] = 0                                           #法向加速度
            if (F > 0)&(p1[5] <= vmax):         #加速不超过最大速度
                p1[6] = self.creata(1/100*i, amax, aa)          #切向加速度
            elif (F < 0)&(p1[5] > 70):         #减速
                p1[6] = 0 - self.creata(1/ 100 * i, amax, aa)
            else:        #匀速
                p1[6] = 0
            self.Q.append(data)

    def trackturn(self, p0, t, a):
        p1 = p0
        # F = random.randint(-1, 2)
        for i in range(int(t * 100)):
            data = [0, 0, 0, 0, 0, 0, 0,0]
            for j in range(len(p1)):
                data[j] = p1[j]
            p1[0] = p1[5] * 1/100 * (math.sin(p1[3])) + p1[0]
            p1[1] = p1[5] * 1/100 * (math.cos(p1[3])) + p1[1]
            p1[3] = (p1[3] + 1/100 * a/p1[5])  #a 法向加速度

            # 航向角在0-2π内
            if p1[3] >= 2*math.pi:
                p1[3] = p1[3]-2*math.pi
            if p1[3] < 0:
                p1[3] = p1[3]+2*math.pi
            p1[5] = p1[5] + 1/ 100 * p1[6]  # 切向加速度
            # if (F>0)&(p1[5]<=vmax):         #加速
            #      p1[6] = self.creata(1/100*i,amax,aa)
            # elif (F<0)&(p1[5]>70):         #减速
            #      p1[6] =0 - self.creata(1/ 100 * i, amax, aa)
            # else:        #匀速
            #      p1[6]=0
            p1[7] = a
            self.Q.append(data)
        return 0
    #爬升俯冲动作函数
    def trackdive(self, p0, t, a1, a2, t1):
        t11 = 0
        p1 = p0
        for i in range(int(t * 100)):
            data = [0, 0, 0, 0, 0, 0, 0,0]
            for j in range(len(p1)):
                data[j] = p1[j]
            p1[0] = p1[5] * 1/100 * math.sin(p1[3])*math.cos(p1[4]) + p1[0]
            p1[1] = p1[5] * 1/100 * math.cos(p1[3])*math.cos(p1[4]) + p1[1]
            p1[2] = p1[5] * 1/100 * math.sin(p1[4]) + p1[2]
            p1[6] = -0.2                     #切向加速度
            if(math.sin(p1[4] != 0)):
                p1[5] = self.plane_attr[2] / math.sin(p1[4]) + 1 / 100 * p1[6]
            if (i/100 < t1) :   #第一段动作俯仰角变化
                p1[7] = a1
                p1[4] = p1[4] + 1/ 100 * p1[7]/ p1[5]
                t11 = i/100
            elif i/100 >= (t-t11)-2/100:                #第三段动作俯仰角回变
                p1[7] = a2
                p1[4] = p1[4] + 1 / 100 * a2 / p1[5]
            else:                                      #中间动作以一定角度直线下降
                p1[7] = 0
            self.Q.append(data)
        return 0

     #转弯的轨迹
    def turn_trace(self, p0, radius,t) :
        """
        用于描述转弯的轨迹
        参数 : 
        p0 : 飞机的初始参数[x,y,z,航向角,仰角,速度,切向加速度,法向加速度]
        radius: 转弯的角度
        """
        p1 = p0
        xp,yp,zp = self.turning_center(p1, radius)
        #print(xp,yp,zp)
        for i in range(int(t*100)):   #每0.01秒产生一个数据
            data = [0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(len(p1)):
                data[j]=p1[j]
            w = p1[5]/radius
            #x坐标
            p1[0] = p1[5] * 1/100 * (math.sin(p1[3])) + p1[0]
            #y坐标
            p1[1] = p1[5] * 1/100 * (math.cos(p1[3])) + p1[1]
            #航向角
            p1[3] = (p1[3] + 1/100 * w)
            # p1[0] = xp + math.sin(p1[3]) * radius
            # p1[1] = yp + math.cos(p1[3]) * radius
            #z坐标
            p1[2] = zp
                            
            #航向角在0-2π内
            if p1[3] >= 2*math.pi:
                p1[3] = p1[3]-2*math.pi
            if p1[3] < 0:
                p1[3] = p1[3]+2*math.pi

            p1[5] = p1[5] + 1/ 100 * p1[6]  # 切向加速度
            p1[7] = w*w*radius
            #print(data)
            self.Q.append(data)

    def turning_center(self, p0, radius):
        p1 = p0
        coordinate = [0, 0, 0]
        coordinate[0] = p1[0] + radius * math.sin(p1[3])
        coordinate[1] = p1[1] + radius * math.cos(p1[3])
        coordinate[2] = p1[2]
        return coordinate

    def createRadar(self):
        self.radar.amount = len(self.Q)
        self.Q = np.array(self.Q)
        self.radar.createData(self.Q[:4])


