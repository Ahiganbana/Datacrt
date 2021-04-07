from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_numSelect import Ui_Form


class Ui_MynumSelect(Ui_Form, QtWidgets.QWidget):
    planeInfo = {}
    def __init__(self, parent=None):
        super().__init__()
        super().setupUi(self)
        self.setupUi(self)
        self.setWindowTitle("选择飞机数量")
        self.lineEdit.setReadOnly(True)

    def setupUi(self, Form):
        self.pushButton.clicked.connect(self.slotCommitPlaneNum)
        self.pushButton_2.clicked.connect(lambda : self.close())
        self.spinBox.setValue(1)
    def slotCommitPlaneNum(self):
        planeType = self.lineEdit.displayText()
        planeNum = self.spinBox.value()
        if(planeNum > 0):
            self.planeInfo[planeType] = planeNum
        self.close()