import numpy as np
import math
import random
class Radar(object):
    def __init__(self):
        #距离 用于计算功率密度
        self.r = []
        #保存数据
        self.Q = []

        #发射功率 平均功率 峰值功率Kw
        self.power = [0.8,30]
        #脉冲宽度 最小值 最大值us
        self.pulse_width = [0.286,8]
        #重复频率  hz
        self.repeat_frequency = [100,10000]
        #工作频率 Mhz (火控雷达根据不同工作模式有不同的工作频率)
        self.working_frequency = [6200,10900]

        self.duty_cycle = [0.2, 1.5]
        #天线增益
        self.G  = 100

    def createData(self,distance):
        Q = []
        self.r = distance
        #雷达数据生成函数
        t=0       #计数
        duty=random.uniform(self.duty_cycle[0],self.duty_cycle[1])  #占空比参数
        repet=random.uniform(self.repeat_frequency[0],self.repeat_frequency[1])      #重复频率系数
        power=self.power
        for i in range(len(self.r)): #在每个时间点做数据生成
            data=[0,0,0,0,0]
            #信号频率
            data[0] = random.uniform(self.working_frequency[0],self.working_frequency[1])
            #占空比
            data[1] = random.uniform(self.duty_cycle[0],self.duty_cycle[1])
            #功率密度(与距离有关)
            data[2] = self.G*(power[1]+power[1]/2*random.uniform(-1,1))/ (4*math.pi*self.r[i]*self.r[i])*1000000   ##功率密度与发生功率及距离有关
            #重复频率
            data[3] = repet
            #脉冲宽度
            data[4] = random.uniform(self.pulse_width[0],self.pulse_width[1]);
            #保留四位小数
            for ii in range (len(data)):
                data[ii]=float('%.4f' % data[ii])
            if data[1]<0:
                data[1]=power[1]
            t=t+1  #计数
            Q.append(data)
        return Q
        



