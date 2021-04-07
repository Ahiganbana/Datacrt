from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_dataShow import Ui_Form
from untils import Utils

class Ui_MyDataShow(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        super().setupUi(self)
        self.setupUi(self)

    def setupUi(self, Form):
        self.pushButton.clicked.connect(lambda : self.close())
        self.pushButton_2.clicked.connect(self.slotForSave)
    def changedata(self, data):
        self.data = data
        _translate = QtCore.QCoreApplication.translate
        C = ['X坐标', 'Y坐标', 'Z坐标', '距离', '角度', '仰角','航向角','速度','雷达频率/GHZ','雷达信号占空比','功率密度/mW每平方米','信号重复频率/KHZ','信号脉冲宽度/us']
        num = len(data)
        H = len(C)
        dataList = {}
        radarList = {}
        for i in range(num):
            for j in range(len(data[i].planes)):
                for k in range(len(data[i].planes[j].trackData)):
                    key = str(i) + '-' + str(j) + '-' + str(k)
                    dataList[key] = data[i].planes[j].trackData[k]
                    radarList[key] = data[i].planes[j].radarData[k]
        
        for key in dataList:
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.gridLayout = QtWidgets.QGridLayout(self.tab)
            self.gridLayout.setObjectName("gridLayout")
            self.tableWidget = QtWidgets.QTableWidget(self.tab)
            self.tableWidget.setObjectName("tableWidget")
            #设置表格的行数和列数
            T = len(dataList[key])
            self.tableWidget.setColumnCount(H)
            self.tableWidget.setRowCount(T)
            self.tableWidget.setHorizontalHeaderLabels(C)#设置表头
            # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)#设置不可写
            for i in range(T):#遍历每一行
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(i, item)
                self.tableWidget.verticalHeaderItem(i).setText(_translate("form", str(i)))#标上行数
                self.tableWidget.setRowHeight(i, 30)#设置行高
                for j in range (H):#遍历所有数据维度
                    #self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[t].plane[k].Q[i][j])))
                    plist = dataList[key]
                    if j < len(plist[i]):#写入飞机轨迹数据
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(plist[i][j])))
                    else:#写入飞机雷达数据
                        jj = j-len(plist[i])
                        rlist = radarList[key]
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(rlist[i][jj])))
                QtWidgets.qApp.processEvents()#多线程
                #self.label.setGeometry((self.width() - 300) / 2, (self.height() - 300) / 2, 300, 300)#设置loading图标位置
                self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
                self.tabWidget.addTab(self.tab, "")
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form", key))#设置当前页名
                
    def slotForSave(self):
        saveUtil = Utils()
        saveUtil.saveData(self.data)

class LoadingWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle('Loading')
        self.resize(657, 501)
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.label = QLabel('loading', self)
        #设置位置坐标，尺寸大小
        self.label.setGeometry((self.width() - 300)/2,(self.height() - 300)/2,300,300)
        #加载gif文件
        self.movie = QtGui.QMovie('./image/loading0.gif')

        self.label.setMovie(self.movie)
        self.label.setScaledContents(True)  #自适应大小
        self.label.raise_()
        self.movie.start()
    def resizeEvent(self, e):
        self.label.setGeometry((self.width() - 300)/2,(self.height() - 300)/2,300,300)
    






