from Ui_MainWindow import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from formation1 import Formation
from paintTrack import PaintTrack
from ui_mysceneMake import Ui_MySceneMake
from ui_MySettingsImport import Ui_MySettingsImport
from ui_MyDataShow import Ui_MyDataShow
from ui_MyDataShow import LoadingWidget
import matplot
from untils import Utils
from planeGroup import PlaneGroup
import copy
import sip
import numpy as np
import json
import time
import os

class WorkThread(QThread):
    trigger = pyqtSignal()
    def __init__(self):
        super(WorkThread, self).__init__()
        print("线程创建成功")
    def getWidget(self,widget):
        self.widget = widget
    def run(self):
        print("线程运行中")
        self.loading = LoadingWidget(self.widget)
        self.loading.show()

class Ui_MyMainWindow(Ui_Form,QtWidgets.QWidget):
    form_list = []
    action_list = []
    formNum = 0
    contents = []
    clickTime = 0
    dimSize = 12
    dimList = []
    planeGroupInfo = {}
    formationInfoList = []
    def __init__(self, parent=None):
        super().__init__()
        super().setupUi(self)
        self.setupUi(self)
        self.planeGroups = []
        self.form_data = []
        self.data = []
    
    def setupUi(self, Form):
        self.setCheckBoxId()
        self.sceneMk = Ui_MySceneMake(parent=Ui_MyMainWindow)
        self.settingsImport = Ui_MySettingsImport(parent=Ui_MyMainWindow)
        self.pushButton_5.setEnabled(False)
        self.form_commit_pushButton.clicked.connect(self.slotForMainwindow)
        self.pushButton_5.clicked.connect(self.soltForFormicommit)
        self.line_action_pushButton.clicked.connect(self.slotBaseActionBut1)
        self.turn_action_pushButton.clicked.connect(self.slotBaseActionBut2)
        self.drive_down_action_pushButton.clicked.connect(self.slotBaseActionBut3)
        self.drive_up_action_pushButton.clicked.connect(self.slotBaseActionBut4)
        self.type_comboBox.currentIndexChanged.connect(self.slotPlaneTypeSel)
        self.form_type_comboBox.currentIndexChanged.connect(self.slotFormTypeSel)
        self.s_action_pushButton.clicked.connect(self.slotAddiActionBut1)
        self.o_action_pushButton.clicked.connect(self.slotAddiActionBut2)
        self.form_commiti_pushButton.clicked.connect(self.slotForShow)
        self.form_commiti_pushButton.clicked.connect(self.slotCollectColumns)
        self.dataOverview_pushButton.clicked.connect(self.slotForOverview)
        self.data_save_pushButton.clicked.connect(self.slotForSave)
        self.num_spinBox.setValue(1)
        self.scene_settings_widget.setEnabled(False)
        self.plane_settings_widget.setEnabled(False)
        self.senceMode.toggled.connect(self.slotOpenSceneMode)
        self.actionMode.toggled.connect(self.slotOpenActionMode)
        self.DIYMode.toggled.connect(self.slotOpenDIYMode)
        self.columns_buttonGroup.setExclusive(False)
        self.horizontalLayout_10.setEnabled(False)
        self.gridLayout.setEnabled(False)
        self.fiveDim_radioButton.clicked.connect(self.soltSelect5Dim)
        self.eightDim_radioButton.clicked.connect(self.soltSelect8Dim)
        self.twelveDim_radioButton.clicked.connect(self.defaultCheckBox)
        self.selectScen_radioButton.clicked.connect(self.soltSelectScene)
        self.makeScen_radioButton.clicked.connect(self.slotMakeScene)
        self.textEdit_2.textChanged.connect(self.slotJudgeEmpty)
        self.clear_pushButton.clicked.connect(self.delt)
        self.clear_pushButton.clicked.connect(self.slotRevokAction)
        self.revoke_pushButton.clicked.connect(self.slotRevokAction)
        self.overview_textBrowser.textChanged.connect(self.slotTextBrowser)
        self.addPlane_pushButton.clicked.connect(self.slotCreatePlaneGroup)
        self.sceneSave_pushButton.clicked.connect(self.slotSettingsSave)
        self.sceneMk.yes_pushButton.clicked.connect(self.slotShowSceneInfo)
        self.settingsImport.infoWidget.pushButton.clicked.connect(self.slotShowSettingInfo)
        self.columns_buttonGroup.buttonClicked.connect(self.soltCountDimsize)
        self.form_commiti_pushButton.setEnabled(False)
        self.setting.setReadOnly(True)
        self.DIYMode.setChecked(True)
        self.textEdit.setReadOnly(True)
        self.overview_textBrowser.setReadOnly(True)
        self.paintCanvas = PaintTrack()

    def slotForMainwindow(self):
        self.formNum =  self.form_num_spinBox.value()
        if(self.formNum == 0):
            QtWidgets.QMessageBox.information(QWidget(), "提示", "编队数量至少为1")
            return;
        self.setNthFormation()
        self.form_num_spinBox.setEnabled(False)
        self.form_commit_pushButton.setEnabled(False)
    
    def setNthFormation(self):
        self.setting.setText(str(len(self.form_list) + 1))
        
    def slotBaseActionBut1(self):
        self.pushButton_5.setEnabled(True)
        self.textEdit.append(self.line_action_pushButton.text())
        self.action_list.append(self.line_action_pushButton.text())
    def slotBaseActionBut2(self):
        self.pushButton_5.setEnabled(True)
        self.textEdit.append(self.turn_action_pushButton.text())
        self.action_list.append(self.turn_action_pushButton.text())
    def slotBaseActionBut3(self):
        self.pushButton_5.setEnabled(True)
        self.textEdit.append(self.drive_down_action_pushButton.text())
        self.action_list.append(self.drive_down_action_pushButton.text())
    def slotBaseActionBut4(self):
        self.pushButton_5.setEnabled(True)
        self.textEdit.append(self.drive_up_action_pushButton.text())
        self.action_list.append(self.drive_up_action_pushButton.text())
    def slotAddiActionBut1(self):
        self.pushButton_5.setEnabled(True)
        self.textEdit.append(self.s_action_pushButton.text())
        self.action_list.append(self.s_action_pushButton.text())
    def slotAddiActionBut2(self):
        self.pushButton_5.setEnabled(True)
        self.textEdit.append(self.o_action_pushButton.text())
        self.action_list.append(self.o_action_pushButton.text())

    def slotPlaneTypeSel(self):
        self.pushButton_5.setEnabled(True)
        if(not self.textEdit.document().isEmpty()):
            self.textEdit.clear()
        index = self.type_comboBox.currentIndex()
        if(index == 1):
            self.s_action_pushButton.setText("筋斗")
            self.o_action_pushButton.setText("上升转弯")
        if(index == 2 or index == 4):
            self.s_action_pushButton.setText("左迂回")
            self.o_action_pushButton.setText("右迂回")
        if(index == 0 or index == 3):
            self.s_action_pushButton.setText("s型")
            self.o_action_pushButton.setText("o型")

    def slotFormTypeSel(self):
        self.pushButton_5.setEnabled(True)
        index = self.form_type_comboBox.currentIndex()

    def slotForShow(self):
        for i in range(len(self.form_list)):
            print(self.form_list[i])
        self.clickTime += 1
        self.helper = LoadingWidget(self.dataShow_groupBox)
        self.helper.show()
        (self.data, self.form_data) = self.paintCanvas.createData(self.form_list)
        if(self.clickTime == 1):
            #第一次点击生成数据
            self.gridlayout = QtWidgets.QGridLayout(self.dataShow_groupBox)  # 继承容器groupBox
        else:
            #不是第一次点击生成数据
            self.gridlayout.removeWidget(self.paintCanvas)
            sip.delete(self.paintCanvas)
            self.paintCanvas = PaintTrack()
        self.paintCanvas.drawTrack(self.data)
        self.gridlayout.addWidget(self.paintCanvas,0,1)
        self.helper.deleteLater()

    def soltForFormicommit(self):
        if(len(self.setting.text()) == 0):
            QtWidgets.QMessageBox.information(QWidget(), "提示", "请先确定编队数量!")
            if(not self.textEdit.document().isEmpty()):
                self.textEdit.clear()
            return
        num = int(self.setting.text())
        content = "第" + str(num) + "个编队 :"
        #self.overview_textBrowser.append()
        self.overview_textBrowser.append(content + self.textEdit_2.toPlainText())
        self.contents.append(content + self.textEdit_2.toPlainText())
        self.createForm()
        if(num < self.formNum):
            num += 1
            #self.setting.setText(str(num))
            self.setNthFormation()
        else:
            self.widget.setEnabled(False)
        self.textEdit_2.clear()
        self.textEdit.clear()
        self.action_list = []

    def createForm(self):
        form_id = int(self.setting.text())
        form_type = self.form_type_comboBox.currentText()
        form = Formation(form_id, form_type)
        form.planes = copy.deepcopy(self.planeGroups)
        form.info = copy.deepcopy(self.formationInfoList)
        self.formationInfoList.clear()
        self.planeGroups.clear()
        self.form_list.append(form)
        self.commitOrNot()

    def slotForOverview(self):
        #self.tools = LoadingWidget()
        self.tools = Ui_MyDataShow()
        self.loading = LoadingWidget(self.tools)
        self.loading.show()
        self.tools.changedata(self.form_data)
        self.tools.show()
        self.tools.setWindowTitle("数据展示")
        self.loading.deleteLater()

    def slotOpenSceneMode(self):
        self.twelveDim_radioButton.setChecked(True)
        if(self.senceMode.isChecked()):
            self.scene_settings_widget.setEnabled(True)
            self.widget.setEnabled(False)
        else:
            self.scene_settings_widget.setEnabled(False)
            self.widget.setEnabled(True)
        self.horizontalLayout_10.setEnabled(True)
        self.gridLayout.setEnabled(True)
        self.defaultCheckBox()
    def slotOpenActionMode(self):
        self.twelveDim_radioButton.setChecked(True)
        if(self.actionMode.isChecked()):
            self.plane_settings_widget.setEnabled(True)
        else:
            self.plane_settings_widget.setEnabled(False)
        self.horizontalLayout_10.setEnabled(True)
        self.gridLayout.setEnabled(True)
        self.defaultCheckBox()
    def slotOpenDIYMode(self):
        self.twelveDim_radioButton.setChecked(True)
        if(self.DIYMode.isChecked()):
            self.plane_settings_widget.setEnabled(True)
            self.scene_settings_widget.setEnabled(True)
        else:
            self.plane_settings_widget.setEnabled(False)
            self.scene_settings_widget.setEnabled(False)
        self.defaultCheckBox()
        self.horizontalLayout_10.setEnabled(True)
        self.gridLayout.setEnabled(True)
    def soltSelect5Dim(self):
        self.dimSize = 5
        if(self.fiveDim_radioButton.isChecked()):
            listOfCheckBox = self.columns_buttonGroup.buttons()
            columns = len(listOfCheckBox)
            for i in range(5, columns):
                if(listOfCheckBox[i].isChecked()):
                    listOfCheckBox[i].setChecked(False)
                    listOfCheckBox[i].setEnabled(False)

    def soltCountDimsize(self):
        count = 0
        listOfCheckBox = self.columns_buttonGroup.buttons()
        length = len(listOfCheckBox)
        for i in range(length):
            if(listOfCheckBox[i].isChecked()):
                count += 1
        if (count == self.dimSize):
            for i in range(length):
                if(not listOfCheckBox[i].isChecked()):
                    listOfCheckBox[i].setEnabled(False)
        else:
            for i in range(length):
                listOfCheckBox[i].setEnabled(True)
        print(count)

    def setCheckBoxId(self):
        self.columns_buttonGroup = QButtonGroup(self.setting_widget)
        self.columns_buttonGroup.addButton(self.x_checkBox, 0)
        self.columns_buttonGroup.addButton(self.y_checkBox, 1)
        self.columns_buttonGroup.addButton(self.height_checkBox, 2)
        self.columns_buttonGroup.addButton(self.speed_checkBox, 3)
        self.columns_buttonGroup.addButton(self.direct_checkBox, 4)
        self.columns_buttonGroup.addButton(self.z_angle_checkBox, 5)
        self.columns_buttonGroup.addButton(self.dis_checkBox, 6)
        self.columns_buttonGroup.addButton(self.sigWidth_checkBox, 7)
        self.columns_buttonGroup.addButton(self.radarFre_checkBox, 8)
        self.columns_buttonGroup.addButton(self.dutyCycle_checkBox, 9)
        self.columns_buttonGroup.addButton(self.powerDen_checkBox, 10)
        self.columns_buttonGroup.addButton(self.repeatFre_checkBox, 11)

    def soltSelect8Dim(self):
        self.dimSize = 8
        if(self.eightDim_radioButton.isChecked()):
            listOfCheckBox = self.columns_buttonGroup.buttons()
            for i in range(8):
                listOfCheckBox[i].setEnabled(True)
                if(not listOfCheckBox[i].isChecked()):
                    listOfCheckBox[i].setChecked(True)
            for i in range(8, len(listOfCheckBox)):
                if(listOfCheckBox[i].isChecked()):
                    listOfCheckBox[i].setChecked(False)
                    listOfCheckBox[i].setEnabled(False)
        
    def soltSelectScene(self):
        self.settingsImport.show()
    
    def slotMakeScene(self):
        self.sceneMk.show()
    
    def slotSettingsSave(self):
        if(len(self.form_list) == 0):
            QtWidgets.QMessageBox.information(QWidget(), "提示", "请先完成设置!")
            return
        saveStr = ""
        fdict = {}
        for i in range(len(self.form_list)):
            sdict = {}
            sdict["编队编号"] = self.form_list[i].form_id
            sdict["任务"] = self.form_list[i].mission
            sdict["编队类型"] = self.form_list[i].ftype
            sdict["详细信息"] = self.form_list[i].info
            fdict["config" + str(i)] = sdict
        #fstr = json.dumps(fdict, ensure_ascii=False)
        currPath = os.path.dirname(__file__)
        dirPath = os.path.dirname(currPath)
        dirPath += '\sceneFile'
        print(dirPath)
        filePath = QFileDialog.getSaveFileName(self, "保存场景", dirPath, "json files(*.json)")
        filename = filePath[0]
        if(not len(filename) == 0):
            with open(filename, 'w') as fileObj:
                json.dump(fdict, fileObj,ensure_ascii=False)

    def slotForSave(self):
        #飞机数据保存函数
        if(not self.form_data):
            QtWidgets.QMessageBox.information(QWidget(), "提示", "请先生成数据!")
            return
        save = Utils()
        save.saveData(self.form_data, self.dimList)


    def defaultCheckBox(self):
        self.dimSize = 12
        listOfCheckBox = self.columns_buttonGroup.buttons()
        if(self.twelveDim_radioButton.isChecked()):
            for i in range(len(listOfCheckBox)):
                # print(i)
                # print('----')
                # print(listOfCheckBox[i].text())
                listOfCheckBox[i].setEnabled(True)
                listOfCheckBox[i].setChecked(True)
    def slotJudgeEmpty(self):
        if(self.textEdit_2.document().isEmpty()):
            self.pushButton_5.setEnabled(False)
        else:
            self.pushButton_5.setEnabled(True)

    def delt(self):
        formNum = self.formNum
        if self.form_list:
            formNum = formNum - 1
        if self.data:
            #del self.data[len(self.data) - 1]
            self.data.pop()
        else:
            QtWidgets.QMessageBox.information(QWidget(), "提示", "请先生成数据!")
            return
        #更新图像
        self.gridlayout.removeWidget(self.paintCanvas)
        sip.delete(self.paintCanvas)
        self.paintCanvas = PaintTrack()
        print(len(self.data))
        self.paintCanvas.drawTrack(self.data)
        self.gridlayout.addWidget(self.paintCanvas, 0, 1)
    def slotRevokAction(self):
        if(self.contents):
            self.contents.pop()
        s = len(self.contents)
        #self.overview_textBrowser.clear()
        show = ""
        for i in range(s):
           show += self.contents[i] + "\n"
        self.overview_textBrowser.setText(show)
        if(len(self.form_list) > 0):
            self.form_list.pop()
        sl = len(self.form_list)
        if(sl < self.formNum):
            self.form_commiti_pushButton.setEnabled(False)
        elif(sl == self.formNum):
            self.form_commiti_pushButton.setEnabled(True)
        if(len(self.setting.text()) > 0):
            self.setNthFormation()
            self.widget.setEnabled(True)
    
    def slotTextBrowser(self):
        if(self.overview_textBrowser.document().isEmpty()):
            self.revoke_pushButton.setEnabled(False)
        else:
            self.revoke_pushButton.setEnabled(True)
    
    def slotCollectColumns(self):
        listc = self.columns_buttonGroup.buttons()
        for i in range(len(listc)):
            if(listc[i].isChecked()):                                       
                self.dimList.append(listc[i].text())
    
    def slotCreatePlaneGroup(self):
        """
        创建飞机组
        """
        if(not self.textEdit.document().isEmpty()):
            self.textEdit.clear()
        if(len(self.action_list) == 0):
            QtWidgets.QMessageBox.information(QWidget(), "提示", "请为飞机选择机动类型!")
            return
        actionList = copy.deepcopy(self.action_list)
        ptype = self.type_comboBox.currentText()
        num = self.num_spinBox.value()
        ftype = self.form_type_comboBox.currentText()
        self.planeGroupInfo[ptype] = num
        self.planeGroupInfo["动作"] = copy.deepcopy(actionList)
        #formationInfo = json.dumps(self.planeGroupInfo, ensure_ascii=False)
        formationInfo = copy.deepcopy(self.planeGroupInfo)
        showInfo = ptype + ":" + str(num) + "\n动作:" + ','.join(actionList)
        self.formationInfoList.append(formationInfo)
        #self.contents.append(showInfo)
        self.textEdit_2.append(showInfo)
        planeGroup = PlaneGroup(ptype, ftype, num, actionList)
        self.planeGroupInfo.clear()
        self.planeGroups.append(planeGroup)
        self.action_list.clear()
    
    def slotShowSceneInfo(self):
        if(self.sceneMk.formationi):
            self.setNthFormation()
            content = "第" + str(len(self.form_list) + 1) + "个编队 :"
            self.sceneMk.formationi.form_id = 1+ len(self.form_list)
            self.overview_textBrowser.append(content)
            missionExpress = "编队任务:" + self.sceneMk.formationi.mission
            self.overview_textBrowser.append(missionExpress)
            for i in range(len(self.sceneMk.formationi.planes)):
                showInfo = self.sceneMk.formationi.planes[i].ptype + \
                    ":" + str(self.sceneMk.formationi.planes[i].num) + \
                    "\n动作:" + ','.join(self.sceneMk.formationi.planes[i].actionList)
                self.overview_textBrowser.append(showInfo)
            self.contents.append(content + self.overview_textBrowser.toPlainText())
            self.form_list.append(self.sceneMk.formationi)
        self.commitOrNot()
        self.setNthFormation()
        self.form_num_spinBox.setValue(1 + len(self.form_list))
    def slotShowSettingInfo(self):
        infoLength = len(self.settingsImport.formationList)
        if(not infoLength == 0):
            #self.overview_textBrowser.append(self.settingsImport.detailInfo)
            #根据每一个编队生成飞机组
            startt = time.time()
            for i in range(infoLength):
                formationi = self.settingsImport.formationList[i]
                groups = formationi.info
                planeGroups = []
                formationi_id =  len(self.form_list) + 1
                showInfo = "第" + str(formationi_id)  + "个编队\n"
                ftype = formationi.ftype
                formationi.form_id = formationi_id
                for j in range(len(groups)):
                    for key in groups[j]:
                        if(key == "动作"):
                            actionList = groups[j][key]
                            showInfo += key + ":" + ",".join(actionList) + "\t"
                        else:
                            ptype = key
                            num = groups[j][key]
                            showInfo += ptype + ":" + str(num) + "\t"
                    planeGroupi = PlaneGroup(ptype, ftype, num, actionList)
                    formationi.planes.append(planeGroupi)
                self.form_list.append(formationi)
                self.overview_textBrowser.append(showInfo)
                self.contents.append(showInfo)
            
            endt = time.time()
            print("解析信息花费的时间:",endt - startt)
            self.settingsImport.formationList.clear()
            self.settingsImport.formationInfoList.clear()
            self.setNthFormation()
            self.form_num_spinBox.setValue(len(self.form_list) + 1)
            self.commitOrNot()
    
    def commitOrNot(self):
        if(not self.form_list):
            self.form_commiti_pushButton.setEnabled(False)
        else:
            self.form_commiti_pushButton.setEnabled(True)
        



        


