from cradar import Radar
import random
import math

class FireControlRadar(Radar):
    def __init__(self):
        super().__init__()
        #发射功率 平均功率 峰值功率Kw
        self.power = [0.25,20]
        #脉冲宽度 最小值 最大值us
        self.pulse_width = [0.286,8]
        #重复频率  hz
        self.repeat_frequency = 9030
        #工作频率 Mhz (火控雷达根据不同工作模式有不同的工作频率)
        self.working_frequency1 = [6200,10900]
        self.working_frequency2 = [9700,9900]
        #占空比
        self.duty_cycle = [0.2, 1.5]

    def createData(self,distance):
        Q = []
        self.r  = distance
        setrad=0 #标志位
        t=0       #计数
        duty = random.uniform(self.duty_cycle[0],self.duty_cycle[1])  #占空比参数
        repet = self.repeat_frequency      #重复频率系数
        power = self.power
        for i in range(len(self.r)): #在每个时间点做数据生成
            data=[0,0,0,0,0]
            #根据模式选择不同的频率波段
            #为0的时候选择working_frequency1作为频率波段
            if setrad==0:
                #信号频率
                data[0] = random.uniform(self.working_frequency1[0],self.working_frequency1[1])
                #占空比
                data[1] = random.uniform(self.duty_cycle[0],self.duty_cycle[1])
                #功率密度(与距离有关)
                data[2] = self.G*(power[1]+power[1]/2*random.uniform(-1,1))/\
                        (4*math.pi*self.r[i]*self.r[i])*1000000   ##功率密度与发生功率及距离有关
                #重复频率
                data[3] = self.repeat_frequency
                #脉冲宽度
                data[4] = random.uniform(self.pulse_width[0],self.pulse_width[1]);
                #保留四位小数
                for ii in range (len(data)):
                    data[ii]=float('%.4f' % data[ii])
                if data[2] < 0:
                    data[2] = power[1]
                t=t+1  #计数
            Q.append(data)
        return Q