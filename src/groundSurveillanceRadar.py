from cradar import Radar
import random

class GroundSurveillanceRadar(Radar):
    def __init__(self):
        super().__init__()
        #发射功率 平均功率 峰值功率Kw
        self.power = [0.043,45]
        #脉冲宽度 最小值 最大值us
        self.pulse_width = [0.48,0.52]
        #重复频率  hz
        self.repeat_frequency = [1830,1880]
        #工作频率 Mhz (火控雷达根据不同工作模式有不同的工作频率)
        self.working_frequency = [300,1000]