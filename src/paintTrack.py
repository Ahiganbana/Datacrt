import matplotlib.pyplot as plt
import copy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
import numpy as np
import math
import random
matplotlib.use("Qt5Agg")  # 声明使用QT5

class PaintTrack(FigureCanvas):
    def __init__(self, flag = 0):
        self.Q = []
        self.P = []
        self.rat = 0#放大比例
        #编队颜色
        self.color = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
        #飞机颜色
        self.colora = ['g', 'b', 'c', 'k', 'm']
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(20, 20), dpi=60)
        #第二步：在父类中激活Figure窗口
        super(PaintTrack, self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        #self.axes=Axes3D(self.fig)
        if(flag == 0):    
            self.axes = self.fig.add_subplot(111, projection='3d')
        else:
            self.axes = self.fig.add_subplot(111)
        #self.ax = plt.axes(projection='3d')

        self.x = [0, 0]
        self.y = [0, 0]
        self.z = [0, 0]

    def drawTrack(self, Q):
        xmin = xmax = 0
        ymin = ymax = 0
        #画飞机轨迹
        for ij in range(len(Q)):
            #len(Q):编队中飞机组的数量 
            self.Q = Q[ij]
            #self.Q : 每个飞机组的数据
            for i in range(len(self.Q)):
                #飞机组中的每架飞机
                for k in range(len(self.Q[i])):
                    #获取位置坐标
                    X = [j[0] for j in self.Q[i][k]]
                    Y = [j[1] for j in self.Q[i][k]]
                    Z = [j[2] for j in self.Q[i][k]]
                    self.axes.scatter(X[0:1], Y[0:1], Z[0:1], c="k", marker="x") #起始位置
                    self.axes.plot(X[:], Y[:], Z[:], c=self.color[ij%7]) #分配不同颜色
                    self.axes.scatter(X[len(X)-2:len(X)-1], Y[len(X)-2:len(X)-1], Z[len(X)-2:len(X)-1], c="k", marker="^")#终点
                    #获得坐标的最大范围
                    xmin = min(min(X[:]), xmin)
                    xmax = max(max(X[:]), xmax)
                    ymin = min(min(Y[:]), ymin)
                    ymax = max(max(Y[:]), ymax)
                    self.x = [xmin, xmax]
                    QtWidgets.qApp.processEvents()
        self.y = [ymin, ymax]
        self.z = [200,15000]
        xx,yy = np.meshgrid(self.x, self.y)#设置坐标范围
        zz = xx*0
        #self.axes.plot_surface(xx, yy, zz, cmap = plt.cm.YlGnBu_r, alpha=0.2)#画海平面
        self.axes.set_zlabel('Z')  # 坐标轴
        self.axes.set_ylabel('Y')
        self.axes.set_xlabel('X')
        #self.axes.set_xlim(100, 5000)
        #self.axes.set_ylim(100, 5000)
        self.axes.set_zlim(200, 15000)
        self.Xlen = xmax-xmin
        self.Ylen = ymax-ymin
        self.Zlen = 15000

    #数据转换函数
    def dtransf(self,data):
        Fdata = []
        #输入为飞机组的轨迹数据
        for i in range(len(data)):
            datamid = []
            for j in range(len(data[i])):
                # #print(j)
                data0 = [0, 0, 0, 0, 0, 0, 0, 0]
                data0[0] = data[i][j][0] #X坐标
                data0[1] = data[i][j][1] #y坐标
                data0[2] = data[i][j][2] #z坐标
                data0[3] = data[i][j][4]##求与原点的距离
                #计算对方相对于原点的运动夹角
                if data[i][j][1] > 0:#1、2象限
                    data0[4] = math.pi-math.atan(data[i][j][0]/data[i][j][1])+data[i][j][3]
                else:
                    data0[4] = - math.atan(data[i][j][0] / data[i][j][1]) + data[i][j][3]
                #夹角在0-2π之间
                if data0[4] >= 2 * math.pi:
                    data0[4] = data0[4]  - 2 * math.pi
                elif data0[4] < 0:
                    data0[4] = data0[4] + 2 * math.pi
                if data0[4] > math.pi:#映射到0-π
                    data0[4] = math.pi*2-data0[4]
                data0[5] = math.atan(data0[2]/data0[3])#计算仰角
                data0[6] = data[i][j][3] #航向角
                data0[7] = abs(data[i][j][5]) #速度
                #保留4位小数
                for ii in range (len(data0)):
                    data0[ii]=float('%.4f' % data0[ii])

                datamid.append(data0)
            Fdata.append(datamid)
        return Fdata
    
    def createData(self, form_list):
        finalData = []
        form_num = len(form_list)
        #遍历每一个编队
        for i in range(form_num):
            transdata = []
            #遍历编队中的每一个飞机组
            for j in range(len(form_list[i].planes)):
                form_list[i].planes[j].createTrackData()
                #print(form_list[i].planes[j].trackData)
                #计算距离
                self.distanceCount(form_list[i].planes[j].trackData)
                radarData = []
                for k in range(len(form_list[i].planes[j].trackData)):
                    distance = [x[4] for x in form_list[i].planes[j].trackData[k]]
                    #print("in trackdata",len(pro[k]))
                    radarData.append(form_list[i].planes[j].createRadarData(distance))
                    QtWidgets.qApp.processEvents()
                form_list[i].planes[j].radarData = copy.deepcopy(radarData)
                #transdata中存放的是飞机组的数据
                form_list[i].planes[j].trackData = self.dtransf(form_list[i].planes[j].trackData)
                #form_list[i].planes[j].trackData = pro
                transdata.append(copy.deepcopy(form_list[i].planes[j].trackData)) #飞机组数据转换
            finalData.append(transdata)
        return finalData, form_list

    def distanceCount(self, datai):
        fdata = []
        for j in range(len(datai)):
            #取出飞机组中的每个飞机的数据
            #print("in distanceCount",len(data))
            data = datai[j]
            for i in range(len(data)):
                datai[j][i][4] = np.sqrt(datai[j][i][0]*datai[j][i][0] + \
                    datai[j][i][1]*datai[j][i][1] + datai[j][i][2]*datai[j][i][2])
                    

