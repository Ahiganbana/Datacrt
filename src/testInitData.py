import random
import math
import pandas as pd
from firecontrolradar import FireControlRadar
from earlyWarningControlRadar import EarlyWarningControlRadar
from groundSurveillanceRadar import GroundSurveillanceRadar
from guideradar import GuideRadar
from terrainTrackingRadar import TerrainTrackingRadar

class CreateInitdata(object):
    def __init__(self):
        self.ptype = random.randint(0, 4)
        self.radar = self.createRadarData()

    def createData(self):
        #x y z 速度 航向角 俯仰角 距离
        init_data = [1000, 1000, 5000, 200, 0, 0, 0]
        if(self.ptype == 0):
            init_data[3] = random.randint(800, 860)
            init_data[2] = random.uniform(12000, 15000)
        if(self.ptype == 1):
            init_data[3] = random.randint(900, 1100)
            init_data[2] = random.uniform(7000, 12000)
        if(self.ptype == 2):
            init_data[3] = random.randint(750, 950)
            init_data[2] = random.uniform(8000, 10000)
        if(self.ptype == 3):
            init_data[3] = random.randint(250, 350)
            init_data[2] = random.uniform(1000, 2000)
        if(self.ptype == 4):
            init_data[3] = random.randint(800, 1000)
            init_data[2] = random.uniform(7000, 10000)
        init_data[4] = random.uniform(0, 2 * math.pi)
        init_data[5] = random.uniform(0, 2 * math.pi)
        init_data[6] = math.sqrt(init_data[0] * init_data[0] + init_data[1] * init_data[1] + init_data[2] * init_data[2])
        return init_data
    
    def createRadarData(self):
        #脉冲宽度 雷达频率 占空比 功率密度 重复频率
        if(self.ptype == 0):
            #侦察机
            radar = GroundSurveillanceRadar()
        if(self.ptype == 1):
            #战斗机
            radar = FireControlRadar()
        
        if(self.ptype == 2):
            #预警机
            radar = EarlyWarningControlRadar()
        if(self.ptype == 3):
            #直升机
            radar = GuideRadar()
        if(self.ptype == 4):
            #轰炸机
            radar = TerrainTrackingRadar()
        return radar

    def createMuldata(self):
        finalData = []
        for i in range(5000):
            self.ptype = random.randint(0, 4)
            tmpp = self.createData()
            radar = self.createRadarData()
            tmpr = radar.createData([tmpp[6]])
            tmp = tmpp + tmpr[0]
            for j in range(len(tmp)):
                tmp[j]=float('%.4f' % tmp[j])
            finalData.append(tmp)
        return finalData
    
    def saveData(self, datal, path):
        name_list = ['x坐标', 'y坐标', '高度', '速度', '俯仰角','航向角','距离','雷达频率','占空比','功率密度','重复频率','脉冲宽度',]
        test = pd.DataFrame(columns = name_list, data = datal)
        test.to_csv(path, encoding = 'gbk')

if __name__ == "__main__":
    dataCreater = CreateInitdata()
    datalist = dataCreater.createMuldata()
    dataCreater.saveData(datalist, "./initdata.csv")
    for i in range(len(datalist)):
        if(datalist[i][2] >= 0 and datalist[i][2] < 1000):
            datalist[i][2] = 1
        elif(datalist[i][2] >= 1000 and datalist[i][2] <= 3000):
            datalist[i][2] = 2
        else:
            datalist[i][2] = 3
        if(datalist[i][3] >= 0 and datalist[i][3] <= 600):
            datalist[i][3] = 1
        elif(datalist[i][3] > 600 and datalist[i][3] <= 1800):
            datalist[i][3] = 2
        else:
            datalist[i][3] = 3
    dataCreater.saveData(datalist,"./preInitdata.csv")


