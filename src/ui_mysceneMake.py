from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_sceneMake import Ui_Dialog
from ui_MynumSelect import Ui_MynumSelect
from formation1 import Formation
from paintTrack import PaintTrack
from untils import Utils
from ui_MySceneShow import Ui_MySceneShow
from planeGroup import PlaneGroup
import copy

class Ui_MySceneMake(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__()
        super().setupUi(self)
        self.numSelectWin = Ui_MynumSelect()
        self.setupUi(self)
        self.setWindowTitle("高级设置")
        self.planeGroups = []
        self.formationInfoList = []
        self.clickTimes = 0
        self.formationi = None

    def setupUi(self, Dialog):
        self.setRadioBoxId()
        self.initView()
        self.missionGroup.buttonClicked.connect(self.clickDetect)
        self.formationGroup.buttonClicked.connect(self.formationDetect)
        self.yes_pushButton.clicked.connect(self.createFormation)
        self.no_pushButton.clicked.connect(lambda : self.close())
        self.radioButton_6.setChecked(True)
        self.formationType = "梯形"
        self.listWidget.setCurrentRow(0)
        self.radioButton.setChecked(True)
    def setRadioBoxId(self):
        self.missionGroup = QButtonGroup(self.verticalLayout)
        self.missionGroup.addButton(self.radioButton, 0)
        self.missionGroup.addButton(self.radioButton_2, 1)
        self.missionGroup.addButton(self.radioButton_3, 2)
        self.missionGroup.addButton(self.radioButton_4, 3)
        self.missionGroup.addButton(self.radioButton_5, 4)
        self.missionGroup.addButton(self.radioButton_9, 5)
        self.formationGroup = QButtonGroup(self.horizontalLayout_3)
        self.formationGroup.addButton(self.radioButton_6, 0)
        self.formationGroup.addButton(self.radioButton_7, 1)
        self.formationGroup.addButton(self.radioButton_8, 2)
    def clickDetect(self):
        checkId = self.missionGroup.checkedId()
        if(checkId == 3 or checkId == 4 or checkId == 5):
            self.listWidget.item(1).setFlags(Qt.ItemFlags(not Qt.ItemIsEnabled))
            self.listWidget.item(4).setFlags(Qt.ItemFlags(not Qt.ItemIsEnabled))
        else:
            self.listWidget.item(0).setFlags(Qt.ItemFlags(53))
            self.listWidget.item(1).setFlags(Qt.ItemFlags(53))
            self.listWidget.item(2).setFlags(Qt.ItemFlags(53))
            self.listWidget.item(3).setFlags(Qt.ItemFlags(53))
            self.listWidget.item(4).setFlags(Qt.ItemFlags(53))

    def initView(self):
        self.listWidget.addItems(["侦察机", "战斗机", "电子战机", "直升机", "轰炸机"])
        self.listWidget.itemClicked.connect(self.soltItem)
    def soltItem(self, item):
        flag = int(item.flags())
        name = item.text()
        print(flag)
        if(not flag == 0):
            self.numSelectWin.show()
            self.numSelectWin.lineEdit.setText(name)
    def formationDetect(self, item):
        self.formationType = item.text()

    def createFormation(self):
        self.clickTimes += 1
        self.planeInfo = copy.deepcopy(self.numSelectWin.planeInfo)
        if(not self.planeInfo):
            QtWidgets.QMessageBox.information(QWidget(), "提示", "请选择执行任务的飞机类型和数量!")
            return
        actionList = self.createActionList()
        actions = []
        self.formList = []
        #key为飞机的类型 planeInfo[key]为飞机的数量
        for key in self.planeInfo:
            planeGroupInfo = {}
            actions = actionList[key]
            planeGroupInfo[key] = self.planeInfo[key]
            planeGroupInfo["动作"] = actions
            planeGroupi = PlaneGroup(key, self.formationType, self.planeInfo[key], actions)
            self.formationInfoList.append(planeGroupInfo)
            self.planeGroups.append(planeGroupi)
        self.formationi = Formation(self.clickTimes, self.formationType)
        self.formationi.planes = copy.deepcopy(self.planeGroups)
        self.formationi.mission = self.missionGroup.checkedButton().text()
        self.formationi.info = copy.deepcopy(self.formationInfoList)
        self.numSelectWin.planeInfo.clear()
        self.planeInfo.clear()
        self.planeGroups.clear()
        self.formationInfoList.clear()
    def createAndShowData(self):
        self.paintCanvas = PaintTrack()
        (data, formData) = self.paintCanvas.createData(self.formList)
        self.paintCanvas.drawTrack(data)
        self.showWin = Ui_MySceneShow()
        self.showWin.getData(formData)
        self.gridlayout = QtWidgets.QGridLayout(self.showWin.widget)  # 继承容器groupBox
        self.gridlayout.addWidget(self.paintCanvas,0,1)
        self.showWin.show()
    def createActionList(self):
        missionId = self.missionGroup.checkedId()
        actions = []
        #攻击
        attackDict = {"战斗机":["筋斗", "转弯"], "直升机":["左迂回"], "轰炸机":["左迂回", "转弯"], "侦察机":["爬升", "s型"], "预警机":["o型"]}
        #攻击区域/方向
        breakDict = {"战斗机":["上升转弯","转弯"], "直升机":["转弯"], "轰炸机":["左迂回"], "侦察机":["转弯"], "预警机":["o型"]}
        #巡逻
        patrolDict = {"战斗机":["转弯"], "直升机":["平飞"], "轰炸机":["右迂回"], "侦察机":["s型"], "预警机":["o型"]}
        #电子干扰
        elecinterDict = {"侦察机":["s型"], "预警机":["转弯"], "直升机":["左迂回"]}
        #指挥
        commondDict = {"预警机":["o型"], "侦察机": ["平飞"], "直升机":["左迂回"]}
        #侦察监视
        reconnaissanceDict = {"侦察机":["s型"], "预警机":["平飞"], "直升机":["左迂回"]}
        if(missionId == 0):
            actions = attackDict
        elif(missionId == 1):
            actions = breakDict
        elif(missionId == 2):
            actions = patrolDict
        elif(missionId == 3):
            actions = commondDict
        elif(missionId == 4):
            actions = reconnaissanceDict
        elif(missionId == 5):
            actions = elecinterDict
        return actions 

        


            