from cradar import Radar
import random

class GuideRadar(Radar):
    def __init__(self):
        super().__init__()
        #发射功率 平均功率 峰值功率Kw
        self.power = [0.05,12]
        #脉冲宽度 最小值 最大值us
        self.pulse_width = [0.286,8]

        #工作频率 Mhz (火控雷达根据不同工作模式有不同的工作频率)
        self.working_frequency = [8000,12500]
        