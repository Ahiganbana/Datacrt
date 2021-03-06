#@作者：张厚源 e-mail：885063529@qq.com
#@时间：2019.7.8
#-*- coding: utf-8 -*-
__author__ = 'zhy'
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from childUI import UiForm  #引用界面文件
from newUI import Ui_MainWindow
# #加载动画设计
# class LoadingGifWin(QWidget):
#     def __init__(self,parent=None):
#         super(LoadingGifWin, self).__init__(parent)
#         #实例化标签到窗口中
#         self.label=QLabel('loading',self)
#         #设置标签的宽度与高度
#         self.setFixedSize(100,100)
#         #设置无边框
#         self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint)
#         #加载gif文件
#         self.movie=QtGui.QMovie('./image/loading0.gif')
#         # 播放速度
#         # self.movie.setSpeed(100)
#         self.label.setMovie(self.movie)
#         self.movie.start()
#子窗口类
class ChildWindow(UiForm):
    """
    展示窗口(生成数据过程中的等待图标)
    """
    def __init__(self):
        super(ChildWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Loading')
        # 实例化标签到窗口中
        self.label = QLabel('loading', self)
        #设置位置坐标，尺寸大小
        self.label.setGeometry((self.width() - 300)/2,(self.height() - 300)/2,300,300)
        #加载gif文件
        self.movie = QtGui.QMovie('./image/loading0.gif')

        self.label.setMovie(self.movie)
        self.label.setScaledContents(True)  #自适应大小
        self.label.raise_()
        self.movie.start()
        self.pushButton.clicked.connect(self.btnClick)  # 按钮事件绑定

    def btnClick(self):  # 子窗体自定义事件
        self.close()
#主窗口类
class MyWindow(Ui_MainWindow):
    """
    主窗口展示
    """
    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        self.setupUi(self)
    def disp(self):
        """
        数据展示
        """
        self.child = ChildWindow()  #实例化子窗口作为成员
        self.child.show()           #显示
        self.child.label.show()
        # 数据载入子窗口
        self.child.changedata(self.planedata, self.raddata)
        self.child.changedata2(self.shipdata)
        self.child.setWindowTitle('数据显示')
        self.child.label.deleteLater()   #删除label

if __name__ == "__main__":  # 主程序
    APP = QApplication(sys.argv)
    MAINDOW = QMainWindow()  # 声明窗口
    MYAPP = MyWindow()
    BTN = MYAPP.display  # 主窗体按钮事件绑定
    BTN.clicked.connect(MYAPP.disp)
    MYAPP.show()
    sys.exit(APP.exec_())  # 当点击窗口的x时，退出程序
    