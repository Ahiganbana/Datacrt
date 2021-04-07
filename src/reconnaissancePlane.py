import numpy as np
import math
import random
from cplane import Plane
from matplotlib import pyplot as plt
from groundSurveillanceRadar import GroundSurveillanceRadar

class ReconnaissancePlane(Plane):
    """
    侦察机类 具有之前的飞机具有的直飞,转弯,俯冲,爬升的动作
    同时具有8字飞行,S型飞行,环形飞行的轨迹
    可能的意图有侦察和电子干扰
    参数说明: 
    init_data:初始化数据
    """
    def __init__(self, id, init_data):
        self.id = id
        #init_data包括 初始x,y,z,距离,仰角,速度,切向加速度,法相加速度
        self.init_data = init_data
        #飞机的最大速度,最大加速度,最大爬升率
        self.plane_attr = [860, 20, 35];
        self.radar = GroundSurveillanceRadar()
        self.Q=[];

    #匀速S型轨迹
    def s_trace(self, p0, radis, t):
        self.turn_trace(p0, radis, t/2)
        p1 = self.Q[len(self.Q) - 1]
        # #print(p1)
        p0[0] = p1[0]
        p0[1] = p1[1]
        p0[3] = p0[3] - math.pi
        self.flip(p0[0],p0[1],p0,radis,t/2)

    #对称轨迹的翻转
    def flip(self,a, b, p0, radius, t):
        p1 = p0
        tmp = self.Q
        for i in range(len(tmp) - 1,-1,-1):   #每0.01秒产生一个数据
            data = [0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(len(p1)):
                data[j]=p1[j]
            w = p1[5]/radius
            p1[0] = 2*a - tmp[i][0]
            p1[1] = 2*b - tmp[i][1]
            p1[3] = (p1[3] + 1/100 * w)
            # p1[0] = xp + math.sin(p1[3]) * radius
            # p1[1] = yp + math.cos(p1[3]) * radius
                            
            #航向角在0-2π内
            if p1[3] >= 2*math.pi:
                p1[3] = p1[3]-2*math.pi
            if p1[3] < 0:
                p1[3] = p1[3]+2*math.pi

            p1[5] = p1[5] + 1/ 100 * p1[6]  # 切向加速度
            p1[7] = w*w*radius
            #print(data)
            self.Q.append(data)
        
