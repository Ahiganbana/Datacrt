from Ui_settingsImport import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from untils import Utils
from infoWidget import InfoWidget
import os
import json
from formation1 import Formation
import copy
import time

class Ui_MySettingsImport(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        super().setupUi(self)
        self.treeWidget = QTreeWidget(self)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1, )
        self.treeWidget.headerItem().setText(0, "文件选择窗口")
        self.formationInfoList = []
        self.formationList = []
        self.infoWidget = InfoWidget()
        self.setWindowTitle("配置文件导入")
        self.openFile = QFileDialog(self)
        self.setupUi(self)
    def setupUi(self, Form):
        self.addItemsToWidget()
        self.treeWidget.itemClicked.connect(self.slotItemAction)
        self.infoWidget.pushButton.clicked.connect(self.createFormation)
        self.infoWidget.pushButton_2.clicked.connect(self.clearWidget)
    def addItemsToWidget(self):
        self.items = []
        fItem1 = QTreeWidgetItem(self.treeWidget,["配置文件选择"])
        self.items.append(fItem1)
        self.treeWidget.insertTopLevelItems(0, self.items)
        self.fItem1a = QTreeWidgetItem(fItem1,["示例文件"])
        self.fItem1b = QTreeWidgetItem(fItem1,["从本地导入"])
        fItem1.addChild(self.fItem1a)
        fItem1.addChild(self.fItem1b)
    def slotItemAction(self, treeItem, column):
        if(treeItem.text(0) == "示例文件"):
            print("示例文件")
            self.infoWidget.show()
            path = os.getcwd()
            file = open(path + "\sceneFile\场景1.json", 'r')
            line = json.load(file)
            for key in line:
                showInfo = line[key]
                self.formationInfoList.append(showInfo)
                self.infoWidget.textEdit.append(str(showInfo))
            file.close()
            self.detailInfo = self.infoWidget.textEdit.toPlainText()
        if(treeItem.text(0) == "从本地导入"):
            print("从本地导入")
            currPath = os.path.dirname(__file__)
            dirPath = os.path.dirname(currPath)
            dirPath += '\sceneFile'
            filePath = self.openFile.getOpenFileName(self, "打开", dirPath, "json files(*.json)")
            if(len(filePath[0]) == 0):
                QtWidgets.QMessageBox.information(QWidget(), "提示", "未选择导入文件!")
                return
            file = open(filePath[0], 'r')
            line = json.load(file)
            self.infoWidget.show()
            for key in line:
                showInfo = line[key]
                self.formationInfoList.append(showInfo)
                self.infoWidget.textEdit.append(str(showInfo))
            file.close()
            self.detailInfo = self.infoWidget.textEdit.toPlainText()
    def createFormation(self):
        for i in range(len(self.formationInfoList)):
            id = self.formationInfoList[i]["编队编号"]
            mission = self.formationInfoList[i]["任务"]
            ftype = self.formationInfoList[i]["编队类型"]
            info = self.formationInfoList[i]["详细信息"]
            formationi = Formation(id, ftype, mission)
            formationi.info = copy.deepcopy(info)
            self.formationList.append(formationi)
        self.infoWidget.close()
        self.infoWidget.textEdit.clear()
        self.close()
    def clearWidget(self):
        self.infoWidget.textEdit.clear()
        self.formationInfoList.clear()
        self.formationList.clear()
        self.infoWidget.close()
