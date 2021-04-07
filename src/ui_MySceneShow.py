from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_sceneShow import Ui_Form 
from ui_MyDataShow import Ui_MyDataShow

class Ui_MySceneShow(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        super().setupUi(self)
        self.setupUi(self)
        self.setWindowTitle("场景展示")
    def getData(self, sdata):
        self.data = sdata

    def setupUi(self, Form):
        self.pushButton.clicked.connect(self.slotShowDataInTable)
        self.pushButton_3.clicked.connect(lambda : self.close())
    def slotShowDataInTable(self):
        self.showData = Ui_MyDataShow()
        self.showData.changedata(self.data)
        self.showData.show()
    def slotSaveScene(self):
        pass
    