from cplane import Plane
from reconnaissancePlane import ReconnaissancePlane
from fighter import Fighter
from helicopter import Helicopter
from bomber import Bomber
from earlywarningPlane import EarlyWarningPlane
from formationUtils import FormationUtils
from cradar import Radar
import random
import math

class PlaneGroup(object):
    """
    飞机组实体类,维护编队中飞机的行为方式.
    """
    def __init__(self, ptype, ftype, num, actionList):
        """
        ptype : 飞机的种类
        ftype : 编队的种类
        num : 飞机组中飞机的数量
        actionList : 飞机组的动作
        trackData : 本组飞机的轨迹数据
        """
        self.ptype = ptype
        self.num = num
        self.ftype = ftype
        self.actionList = actionList
        self.trackData = []
        self.utils = FormationUtils()
        self.radarGroup = Radar()
        self.radarData = []
    def __str__(self):
        return '飞机类型: %s 飞机数量: %d 编队类型: %s 动作: %s' %(self.ptype, self.num, self.ftype, self.actionList)
    def createTrackData(self):
        #[x,y,z,航向角, 距离, 速度, 切向加速度, 法向加速度]
        init_data = [1000, 1000, 5000, 0, 5196, 600, 0, 0]
        if(self.ptype == "侦察机"):
            init_data[5] = random.randint(800, 860)
            init_data[2] = random.uniform(12000, 15000)
            self.plane = ReconnaissancePlane(1, init_data)
        if(self.ptype == "战斗机"):
            init_data[5] = random.randint(900, 1100)
            init_data[2] = random.uniform(7000, 12000)
            self.plane = Fighter(1, init_data)
        if(self.ptype == "预警机"):
            init_data[5] = random.randint(750, 950)
            init_data[2] = random.uniform(8000, 10000)
            self.plane = EarlyWarningPlane(1, init_data)
        if(self.ptype == "直升机"):
            init_data[5] = random.randint(250, 350)
            init_data[2] = random.uniform(1000, 2000)
            self.plane = Helicopter(1, init_data)
        if(self.ptype == "轰炸机"):
            init_data[5] = random.randint(800, 1000)
            init_data[2] = random.uniform(7000, 10000)
            self.plane = Bomber(1, init_data)
        for i in range(len(self.actionList)):
            if(self.actionList[i] == "平飞"):
                t = random.random()*10+5  #生成运动时间
                F = random.randint(-1, 2)  #生成状态（加速，减速，匀速）
                self.plane.trackline(init_data, t, F, self.plane.plane_attr[1], 3, self.plane.plane_attr[0])
            if(self.actionList[i] == "转弯"):
                #print("successfully turn")
                t = random.random()*10+10
                a= random.uniform(10, 20)*random.randrange(-1, 2, 2) #生成切向加速度
                self.plane.trackturn(init_data, t, a)
            if(self.actionList[i]== "俯冲"):
                t = self.plane.creatT(self.plane.init_data[2], -1)  #生成运动时间
                t1 = random.uniform(t / 4, t / 2) #生成第一段动作运动时间
                #t2=t-t1
                a1 = 0-random.uniform(5, 10)
                a2 = 0-a1
                self.plane.trackdive(self.plane.init_data, t, a1, a2, t1)
            if(self.actionList[i] == "上升"):
                t = self.plane.creatT(self.plane.init_data[2], 1)     #生成运动时间
                t1 = random.uniform(t / 4, t / 2)  #生成第一段动作运动时间
                a1 = random.uniform(5,10)
                a2 = 0 - a1
                self.plane.trackdive(self.plane.init_data, t, a1, a2, t1)
            if(self.actionList[i] == "s型"):
                #print("s successfully rec")
                t = random.random() * 10 + 10
                radius = random.randint(2000, 3000)
                self.plane.s_trace(self.plane.init_data, radius, t)
            if(self.actionList[i] == "o型"):
                t = random.random() * 10 + 10
                v = init_data[2]
                radius = (v*t) / (2*math.pi)
                self.plane.turn_trace(self.plane.init_data,1300,t)
            if(self.actionList[i] == "左迂回"):
                t = random.random() * 10 + 10
                self.plane.round_left(self.plane.init_data, t)
            if(self.actionList[i] == "右迂回"):
                t = random.random() * 10 + 10
                self.plane.round_right(self.plane.init_data, t)
            if(self.actionList[i] == "筋斗"):
                t = random.random() * 5 + 5
                self.plane.somersault(self.plane.init_data, t)
            if(self.actionList[i] == "上升转弯"):
                self.plane.turn_up()
        if(self.ftype == "梯形"):
            self.trackData = self.utils.echelonFormation(self.plane.Q, self.num)
        if(self.ftype == "菱形"):
            self.trackData = self.utils.diamondFormation(self.plane.Q, self.num)
        if(self.ftype == "蛇形"):
            self.trackData = self.utils.snakelikeFormation(self.plane.Q, self.num)
        self.radarGroup = self.plane.radar
    def createRadarData(self, distance):
        data = self.plane.radar.createData(distance)
        return data
        