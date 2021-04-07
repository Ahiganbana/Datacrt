import matplot
import Plane
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import os
import copy
import csv

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from PyQt5 import QtCore, QtGui, QtWidgets
from reconnaissancePlane import ReconnaissancePlane
from bomber import Bomber
from firecontrolradar import FireControlRadar
from guideradar import GuideRadar
from terrainTrackingRadar import TerrainTrackingRadar
from guideradar import GuideRadar
from groundSurveillanceRadar import GroundSurveillanceRadar
from earlyWarningControlRadar import EarlyWarningControlRadar
from fighter import Fighter
from formation1 import Formation
import numpy as np
import math
import random

class Test(FigureCanvas):
    def __init__(self):
        self.Q = []
        self.P = []
        self.rat = 0#放大比例
        self.color = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(20, 20), dpi=60)

        #第二步：在父类中激活Figure窗口
        super(Test, self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        #self.axes=Axes3D(self.fig)

        #self.axes = self.fig.add_subplot(111, projection='3d')
        self.ax = plt.axes(projection='3d')

        self.x = [0, 0]
        self.y = [0, 0]
        self.z = [0, 0]

    def for_test(self):
        # x=Plane.random.uniform(1000, 5000)
        # y=Plane.random.uniform(1000, 5000)
        # z= Plane.random.uniform(5000, 15000)
        x = 1000
        y = 1000
        z = 5000
        #p0=[x,y,z,Plane.random.uniform(0, math.pi),0, Plane.random.uniform(635, 740),0, 0]
        r = math.sqrt(x*x + y*y + z*z)
        p0=[x,y,z,random.uniform(0,math.pi),r, random.uniform(735, 1470),0, 0]
        action = []
        data = ReconnaissancePlane(1, action, p0)
        #data.turn_trace(p0,1300,t)
        t = data.creatT(p0[2], 1)     #生成运动时间
        t1 = random.uniform(t / 4, t / 2)  #生成第一段动作运动时间
        a1 = - random.uniform(5,10)
        a2 = 0 - a1
        data.trackdive(p0, t, a1, a2, t1, data.plane_attr[2])
        M = []
        F = []
        #F.append(data.Q)
        F.append(data.Q)
        M.append(F)
        self.for_plot(M)
    
    def test_round_left_right(self):
        x = 1000
        y = 1000
        z = 5000
        #p0=[x,y,z,Plane.random.uniform(0, math.pi),0, Plane.random.uniform(635, 740),0, 0]
        r = math.sqrt(x*x + y*y + z*z)
        p0=[x,y,z,0,r, random.uniform(735, 1470),0, 0]
        action = []
        bomber = Bomber(1, action, p0)
        t = random.random() * 10 + 10
        bomber.round_left(p0, t)
        #bomber.round_right(p0, t)
        M = []
        F = []
        F.append(bomber.Q)
        M.append(F)
        self.for_plot(M)
        

    
    def for_plot(self, Q):
        xmin = xmax = 0
        ymin = ymax = 0
        #画飞机轨迹
        for ij in range(len(Q)):
            self.Q = Q[ij]

            for i in range (len(self.Q)):
                #获取位置坐标
                X = [j[0] for j in self.Q[i]]
                Y = [j[1] for j in self.Q[i]]
                Z = [j[2] for j in self.Q[i]]

            #self.axes=self.fig.add_subplot(111, projection='3d')
                #self.axes.plot_wireframe(X,Y,Z)
                
                # self.axes.scatter(X[0:1], Y[0:1], Z[0:1], c="k", marker="x") #起始位置
                # self.axes.plot(X[:], Y[:], Z[:], c=self.color[i%7]) #分配不同颜色
                # self.axes.scatter(X[len(X)-2:len(X)-1], Y[len(X)-2:len(X)-1], Z[len(X)-2:len(X)-1], c="k", marker="^")#终点
                self.ax.scatter3D(X[0:1], Y[0:1], Z[0:1], c = "k", marker="x")
                self.ax.plot3D(X, Y, Z, c=self.color[i%7])
                #self.ax.scatter3D(X[int(len(X)/2 - 2) : int(len(X)/2 - 1)],Y[int(len(Y)/2 - 2) : int(len(Y)/2 - 1)], Z[int(len(Z)/2 - 2 ): int(len(Z)/2 - 1)],c="k",marker="o")
                self.ax.scatter3D(X[len(X)-2:len(X)-1], Y[len(X)-2:len(X)-1], Z[len(X)-2:len(X)-1], c = "k" , marker="^")
                #获得坐标的最大范围
                xmin = min(min(X[:]), xmin)
                xmax = max(max(X[:]), xmax)
                ymin = min(min(Y[:]), ymin)
                ymax = max(max(Y[:]), ymax)
        self.x=[xmin,xmax]
        self.y=[ymin,ymax]
        self.z=[0,10000]
        xx,yy=np.meshgrid(self.x,self.y)#设置坐标范围
        zz=xx*0
        #self.axes.plot_surface(xx,yy,zz,cmap=plt.cm.YlGnBu_r,alpha=0.2)#画海平面
        # self.axes.set_zlabel('Z')  # 坐标轴
        # self.axes.set_ylabel('Y')
        # self.axes.set_xlabel('X')

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')


        #self.axes.set_xlim(100, 5000)
        #self.axes.set_ylim(100, 5000)
        self.ax.set_zlim(0,10000)
        self.Xlen=xmax-xmin
        self.Ylen=ymax-ymin
        self.Zlen=10000
        plt.show()
    
    def test_radar(self):
        radar1 = FireControlRadar(100)
        radar2 = GuideRadar(100)
        radar3 = GroundSurveillanceRadar(100)
        radar4 = TerrainTrackingRadar(100)
        radar5 = EarlyWarningControlRadar(100)
        disatance = np.random.randint(1500, 15000, 100)
        radar1.createData(disatance)
        radar2.createData(disatance)
        radar3.createData(disatance)
        radar4.createData(disatance)
        radar5.createData(disatance)
        print("data: ---------------------")
        print(radar1.Q)
        print("------------------------------")
        print(radar2.Q)
        print("------------------------------")
        print(radar3.Q)
        print("------------------------------")
        print(radar4.Q)
        print("------------------------------")
        print(radar5.Q)
        print("------------------------------")
    
    def test_fighter_turnup(self):
        x = 1000
        y = 1000
        z = 5000
        p0=[x,y,z,Plane.random.uniform(0, math.pi),0, Plane.random.uniform(635, 740),0, 0]
        r = math.sqrt(x*x + y*y + z*z)
        #p0=[x,y,z,r,0, 600,0, 0]
        action = []
        t = Plane.random.random() * 5 + 10
        action = []
        data = Fighter(1, p0)
        data.turn_up()
        M = []
        F = []
        #F.append(data.Q)
        F.append(data.Q)
        M.append(F)
        # filename = '上升转弯.csv'
        # out = open(filename, 'a', newline='')
        # csv_write = csv.writer(out, dialect='excel')
        # C = ['X坐标', 'Y坐标', 'Z坐标', '距离', '角度', '仰角','航向角','速度','雷达频率/GHZ','雷达信号占空比','功率密度/mW每平方米','信号重复频率/KHZ','信号脉冲宽度/us','飞机种类']    
        # csv_write.writerow(C)
        # resultdata = self.dtransf(F)
        # for i in range(len(resultdata)):
        #     for j in range(len(resultdata[i])):
        #         csv_write.writerow(resultdata[i][j] + data.radar.Q[i])
        # out.close()
        self.for_plot(M)
    
    def dtransf(self,data):
        Fdata = []
        for i in range(len(data)):
            datamid = []
            for j in data[i]:
                #print(j)
                data0 = [0, 0, 0, 0, 0,0,0,0]
                data0[0] = j[0] #X坐标
                data0[1] = j[1] #y坐标
                data0[2] = j[2] #z坐标
                data0[3] = np.sqrt(j[0]*j[0]+j[1]*j[1]+j[2]*j[2])##求与原点的距离
                #计算对方相对于原点的运动夹角
                if j[1] > 0:#1、2象限
                    data0[4] = math.pi-math.atan(j[0]/j[1])+j[3]
                else:
                    data0[4] = - math.atan(j[0] / j[1]) + j[3]
                #夹角在0-2π之间
                if data0[4] >= 2 * math.pi:
                    data0[4] = data0[4]  - 2 * math.pi
                elif data0[4] < 0:
                    data0[4] = data0[4] + 2 * math.pi
                if data0[4] > math.pi:#映射到0-π
                    data0[4] = math.pi*2-data0[4]
                data0[5] = math.atan(data0[2]/data0[3])#计算仰角
                data0[6] = j[3] #航向角
                data0[7] = j[5] #速度
                #保留4位小数
                for ii in range (len(data0)):
                    data0[ii]=float('%.4f' % data0[ii])

                datamid.append(data0)
            Fdata.append(datamid)
        return Fdata

    def test_fighter_vertical_rise(self):
        x = 1000
        y = 1000
        z = 2000
        #p0=[x,y,z,Plane.random.uniform(0, math.pi),0, Plane.random.uniform(635, 740),0, 0]
        #r = math.sqrt(x*x + y*y + z*z)
        p0=[x,y,z, 0, 0, Plane.random.uniform(635, 740),0, 0]
        action = []
        t = Plane.random.random() * 10 + 10
        action = []
        data = Fighter(1, p0)
        data.somersault(p0, t)
        M = []
        F = []
        #F.append(data.Q)
        F.append(data.Q)
        M.append(F)
        self.for_plot(M)
    
    def test_formation(self):
        x = 1000
        y = 2000
        z = 2000
        #p0=[x,y,z,Plane.random.uniform(0, math.pi),0, Plane.random.uniform(635, 740),0, 0]
        #r = math.sqrt(x*x + y*y + z*z)
        p0=[x,y,z,0, 0, Plane.random.uniform(735, 1470),0, 0]
        action = []
        data = Fighter(action, p0, 1)
        t = Plane.random.random() * 10 + 10
        aa = 3
        amax = data.plane_attr[1]
        vmax = data.plane_attr[0]
        F = Plane.random.randint(-1, 2)  #生成状态（加速，减速，匀速）
        data.trackline(p0, t, F, amax, aa, vmax)
        form = Formation()
        #plane_data = form.echelonFormation(data.Q, 4, 500)
        #plane_data = form.snakelikeFormation(data.Q, 3, 700,math.pi / 6)
        plane_data = form.diamondFormation(data.Q, 4, 700)
        M = []
        F = []
        transdata =  copy.deepcopy(self.dtransf(plane_data)) #飞机数据转换
        M.append(transdata)
        self.for_plot(M)
    

    #数据转换函数
    def dtransf(self,data):
        Fdata = []
        for i in range(len(data)):
            datamid = []
            print(i)
            for j in data[i]:
                #print(j)
                data0 = [0, 0, 0, 0, 0,0,0,0]
                data0[0] = j[0] #X坐标
                data0[1] = j[1] #y坐标
                data0[2] = j[2] #z坐标
                data0[3] = np.sqrt(j[0]*j[0]+j[1]*j[1]+j[2]*j[2])##求与原点的距离
                #计算对方相对于原点的运动夹角
                if j[1] > 0:#1、2象限
                    data0[4] = math.pi-math.atan(j[0]/j[1])+j[3]
                else:
                    data0[4] = - math.atan(j[0] / j[1]) + j[3]
                #夹角在0-2π之间
                if data0[4] >= 2 * math.pi:
                    data0[4] = data0[4]  - 2 * math.pi
                elif data0[4] < 0:
                    data0[4] = data0[4] + 2 * math.pi
                if data0[4] > math.pi:#映射到0-π
                    data0[4] = math.pi*2-data0[4]
                data0[5] = math.atan(data0[2]/data0[3])#计算仰角
                data0[6] = j[3] #航向角
                data0[7] = j[5] #速度
                #保留4位小数
                for ii in range (len(data0)):
                    data0[ii]=float('%.4f' % data0[ii])

                datamid.append(data0)
            Fdata.append(datamid)
        return Fdata

        

if __name__ == "__main__":
    test = Test()
    #test.for_test()
    #test.test_radar()
    test.test_fighter_turnup()
    #test.test_fighter_vertical_rise()
    #test.test_formation()
    #test.test_round_left_right()