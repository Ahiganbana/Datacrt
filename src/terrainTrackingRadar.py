from cradar import Radar
import random

class TerrainTrackingRadar(Radar):
    """
    地形跟踪雷达
    """
    def __init__(self):
        super().__init__()
        #发射功率 平均功率 峰值功率Kw
        self.power = [0.242,30]
        #脉冲宽度 最小值 最大值us
        self.pulse_width = [0.18,0.22]
        #重复频率  hz
        self.repeat_frequency = [4040,4050]
        #工作频率 Mhz (火控雷达根据不同工作模式有不同的工作频率)
        self.working_frequency = [16700,17000]
        #占空比
        self.duty_cycle = [0.0006,0.001]