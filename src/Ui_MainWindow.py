# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Learning\project\SituationalAwareness\DataCrt-master\datacre-2019.7.17\工程文件\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1094, 895)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_5 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.setting_widget = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_widget.sizePolicy().hasHeightForWidth())
        self.setting_widget.setSizePolicy(sizePolicy)
        self.setting_widget.setObjectName("setting_widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.setting_widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.mode_settings_widget = QtWidgets.QWidget(self.setting_widget)
        self.mode_settings_widget.setObjectName("mode_settings_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mode_settings_widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.modeSelect = QtWidgets.QLabel(self.mode_settings_widget)
        self.modeSelect.setObjectName("modeSelect")
        self.verticalLayout_3.addWidget(self.modeSelect)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DIYMode = QtWidgets.QRadioButton(self.mode_settings_widget)
        self.DIYMode.setObjectName("DIYMode")
        self.mode_buttonGroup = QtWidgets.QButtonGroup(Form)
        self.mode_buttonGroup.setObjectName("mode_buttonGroup")
        self.mode_buttonGroup.addButton(self.DIYMode)
        self.horizontalLayout_4.addWidget(self.DIYMode)
        self.senceMode = QtWidgets.QRadioButton(self.mode_settings_widget)
        self.senceMode.setObjectName("senceMode")
        self.mode_buttonGroup.addButton(self.senceMode)
        self.horizontalLayout_4.addWidget(self.senceMode)
        self.actionMode = QtWidgets.QRadioButton(self.mode_settings_widget)
        self.actionMode.setObjectName("actionMode")
        self.mode_buttonGroup.addButton(self.actionMode)
        self.horizontalLayout_4.addWidget(self.actionMode)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.dimSelect_label = QtWidgets.QLabel(self.mode_settings_widget)
        self.dimSelect_label.setObjectName("dimSelect_label")
        self.verticalLayout_3.addWidget(self.dimSelect_label)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.fiveDim_radioButton = QtWidgets.QRadioButton(self.mode_settings_widget)
        self.fiveDim_radioButton.setObjectName("fiveDim_radioButton")
        self.dim_buttonGroup = QtWidgets.QButtonGroup(Form)
        self.dim_buttonGroup.setObjectName("dim_buttonGroup")
        self.dim_buttonGroup.addButton(self.fiveDim_radioButton)
        self.horizontalLayout_10.addWidget(self.fiveDim_radioButton)
        self.eightDim_radioButton = QtWidgets.QRadioButton(self.mode_settings_widget)
        self.eightDim_radioButton.setObjectName("eightDim_radioButton")
        self.dim_buttonGroup.addButton(self.eightDim_radioButton)
        self.horizontalLayout_10.addWidget(self.eightDim_radioButton)
        self.twelveDim_radioButton = QtWidgets.QRadioButton(self.mode_settings_widget)
        self.twelveDim_radioButton.setObjectName("twelveDim_radioButton")
        self.dim_buttonGroup.addButton(self.twelveDim_radioButton)
        self.horizontalLayout_10.addWidget(self.twelveDim_radioButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sigWidth_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.sigWidth_checkBox.setObjectName("sigWidth_checkBox")
        self.gridLayout.addWidget(self.sigWidth_checkBox, 1, 3, 1, 1)
        self.repeatFre_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.repeatFre_checkBox.setObjectName("repeatFre_checkBox")
        self.gridLayout.addWidget(self.repeatFre_checkBox, 2, 3, 1, 1)
        self.height_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.height_checkBox.setObjectName("height_checkBox")
        self.gridLayout.addWidget(self.height_checkBox, 0, 2, 1, 1)
        self.y_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.y_checkBox.setObjectName("y_checkBox")
        self.gridLayout.addWidget(self.y_checkBox, 0, 1, 1, 1)
        self.x_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.x_checkBox.setObjectName("x_checkBox")
        self.gridLayout.addWidget(self.x_checkBox, 0, 0, 1, 1)
        self.dis_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.dis_checkBox.setObjectName("dis_checkBox")
        self.gridLayout.addWidget(self.dis_checkBox, 1, 2, 1, 1)
        self.powerDen_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.powerDen_checkBox.setObjectName("powerDen_checkBox")
        self.gridLayout.addWidget(self.powerDen_checkBox, 2, 2, 1, 1)
        self.speed_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.speed_checkBox.setObjectName("speed_checkBox")
        self.gridLayout.addWidget(self.speed_checkBox, 0, 3, 1, 1)
        self.direct_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.direct_checkBox.setObjectName("direct_checkBox")
        self.gridLayout.addWidget(self.direct_checkBox, 1, 0, 1, 1)
        self.z_angle_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.z_angle_checkBox.setObjectName("z_angle_checkBox")
        self.gridLayout.addWidget(self.z_angle_checkBox, 1, 1, 1, 1)
        self.dutyCycle_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.dutyCycle_checkBox.setObjectName("dutyCycle_checkBox")
        self.gridLayout.addWidget(self.dutyCycle_checkBox, 2, 1, 1, 1)
        self.radarFre_checkBox = QtWidgets.QCheckBox(self.mode_settings_widget)
        self.radarFre_checkBox.setObjectName("radarFre_checkBox")
        self.gridLayout.addWidget(self.radarFre_checkBox, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_9.addWidget(self.mode_settings_widget)
        self.scene_settings_widget = QtWidgets.QWidget(self.setting_widget)
        self.scene_settings_widget.setObjectName("scene_settings_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scene_settings_widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.scene_settings_widget)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.selectScen_radioButton = QtWidgets.QRadioButton(self.scene_settings_widget)
        self.selectScen_radioButton.setObjectName("selectScen_radioButton")
        self.horizontalLayout_9.addWidget(self.selectScen_radioButton)
        self.makeScen_radioButton = QtWidgets.QRadioButton(self.scene_settings_widget)
        self.makeScen_radioButton.setObjectName("makeScen_radioButton")
        self.horizontalLayout_9.addWidget(self.makeScen_radioButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.addWidget(self.scene_settings_widget)
        self.form_settings = QtWidgets.QLabel(self.setting_widget)
        self.form_settings.setObjectName("form_settings")
        self.verticalLayout_9.addWidget(self.form_settings)
        self.plane_settings_widget = QtWidgets.QWidget(self.setting_widget)
        self.plane_settings_widget.setObjectName("plane_settings_widget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.plane_settings_widget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_2 = QtWidgets.QWidget(self.plane_settings_widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(0, 13, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.overview_textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.overview_textBrowser.setObjectName("overview_textBrowser")
        self.verticalLayout_4.addWidget(self.overview_textBrowser)
        self.horizontalLayout_8.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.plane_settings_widget)
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 13, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.form_num_label = QtWidgets.QLabel(self.widget)
        self.form_num_label.setObjectName("form_num_label")
        self.horizontalLayout_6.addWidget(self.form_num_label)
        self.form_num_spinBox = QtWidgets.QSpinBox(self.widget)
        self.form_num_spinBox.setObjectName("form_num_spinBox")
        self.horizontalLayout_6.addWidget(self.form_num_spinBox)
        self.form_commit_pushButton = QtWidgets.QPushButton(self.widget)
        self.form_commit_pushButton.setObjectName("form_commit_pushButton")
        self.horizontalLayout_6.addWidget(self.form_commit_pushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.form = QtWidgets.QLabel(self.widget)
        self.form.setObjectName("form")
        self.horizontalLayout_2.addWidget(self.form)
        self.setting = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting.sizePolicy().hasHeightForWidth())
        self.setting.setSizePolicy(sizePolicy)
        self.setting.setObjectName("setting")
        self.horizontalLayout_2.addWidget(self.setting)
        self.formnum_label = QtWidgets.QLabel(self.widget)
        self.formnum_label.setObjectName("formnum_label")
        self.horizontalLayout_2.addWidget(self.formnum_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.form_type_label = QtWidgets.QLabel(self.widget)
        self.form_type_label.setObjectName("form_type_label")
        self.horizontalLayout_11.addWidget(self.form_type_label)
        self.form_type_comboBox = QtWidgets.QComboBox(self.widget)
        self.form_type_comboBox.setObjectName("form_type_comboBox")
        self.form_type_comboBox.addItem("")
        self.form_type_comboBox.addItem("")
        self.form_type_comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.form_type_comboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.type_comboBox = QtWidgets.QComboBox(self.widget)
        self.type_comboBox.setStyleSheet("font: 8pt \"Agency FB\";")
        self.type_comboBox.setObjectName("type_comboBox")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.gridLayout_3.addWidget(self.type_comboBox, 0, 1, 1, 1)
        self.type_label = QtWidgets.QLabel(self.widget)
        self.type_label.setObjectName("type_label")
        self.gridLayout_3.addWidget(self.type_label, 0, 0, 1, 1)
        self.num_spinBox = QtWidgets.QSpinBox(self.widget)
        self.num_spinBox.setObjectName("num_spinBox")
        self.gridLayout_3.addWidget(self.num_spinBox, 1, 1, 1, 1)
        self.num_label = QtWidgets.QLabel(self.widget)
        self.num_label.setObjectName("num_label")
        self.gridLayout_3.addWidget(self.num_label, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.base_action_label = QtWidgets.QLabel(self.widget)
        self.base_action_label.setObjectName("base_action_label")
        self.verticalLayout_2.addWidget(self.base_action_label)
        self.base_action_widget = QtWidgets.QWidget(self.widget)
        self.base_action_widget.setObjectName("base_action_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.base_action_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.turn_action_pushButton = QtWidgets.QPushButton(self.base_action_widget)
        self.turn_action_pushButton.setObjectName("turn_action_pushButton")
        self.gridLayout_2.addWidget(self.turn_action_pushButton, 0, 1, 1, 1)
        self.line_action_pushButton = QtWidgets.QPushButton(self.base_action_widget)
        self.line_action_pushButton.setObjectName("line_action_pushButton")
        self.gridLayout_2.addWidget(self.line_action_pushButton, 0, 0, 1, 1)
        self.drive_up_action_pushButton = QtWidgets.QPushButton(self.base_action_widget)
        self.drive_up_action_pushButton.setObjectName("drive_up_action_pushButton")
        self.gridLayout_2.addWidget(self.drive_up_action_pushButton, 1, 1, 1, 1)
        self.drive_down_action_pushButton = QtWidgets.QPushButton(self.base_action_widget)
        self.drive_down_action_pushButton.setObjectName("drive_down_action_pushButton")
        self.gridLayout_2.addWidget(self.drive_down_action_pushButton, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.base_action_widget)
        self.more_action_label = QtWidgets.QLabel(self.widget)
        self.more_action_label.setObjectName("more_action_label")
        self.verticalLayout_2.addWidget(self.more_action_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.s_action_pushButton = QtWidgets.QPushButton(self.widget)
        self.s_action_pushButton.setObjectName("s_action_pushButton")
        self.horizontalLayout.addWidget(self.s_action_pushButton)
        self.o_action_pushButton = QtWidgets.QPushButton(self.widget)
        self.o_action_pushButton.setObjectName("o_action_pushButton")
        self.horizontalLayout.addWidget(self.o_action_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.addPlane_pushButton = QtWidgets.QPushButton(self.widget)
        self.addPlane_pushButton.setObjectName("addPlane_pushButton")
        self.verticalLayout_2.addWidget(self.addPlane_pushButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addWidget(self.widget)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.widget.raise_()
        self.widget_2.raise_()
        self.verticalLayout_9.addWidget(self.plane_settings_widget)
        self.scene_settings_widget.raise_()
        self.plane_settings_widget.raise_()
        self.mode_settings_widget.raise_()
        self.form_settings.raise_()
        self.horizontalLayout_12.addWidget(self.setting_widget)
        self.line_3 = QtWidgets.QFrame(self.widget_5)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_12.addWidget(self.line_3)
        self.dataShow_groupBox = QtWidgets.QGroupBox(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataShow_groupBox.sizePolicy().hasHeightForWidth())
        self.dataShow_groupBox.setSizePolicy(sizePolicy)
        self.dataShow_groupBox.setObjectName("dataShow_groupBox")
        self.horizontalLayout_12.addWidget(self.dataShow_groupBox)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(2, 1)
        self.verticalLayout_7.addWidget(self.widget_5)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.form_commiti_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.form_commiti_pushButton.setObjectName("form_commiti_pushButton")
        self.horizontalLayout_3.addWidget(self.form_commiti_pushButton)
        self.revoke_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.revoke_pushButton.setObjectName("revoke_pushButton")
        self.horizontalLayout_3.addWidget(self.revoke_pushButton)
        self.line = QtWidgets.QFrame(self.widget_3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.sceneSave_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.sceneSave_pushButton.setObjectName("sceneSave_pushButton")
        self.horizontalLayout_3.addWidget(self.sceneSave_pushButton)
        self.data_save_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.data_save_pushButton.setObjectName("data_save_pushButton")
        self.horizontalLayout_3.addWidget(self.data_save_pushButton)
        self.line_2 = QtWidgets.QFrame(self.widget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.dataOverview_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.dataOverview_pushButton.setObjectName("dataOverview_pushButton")
        self.horizontalLayout_3.addWidget(self.dataOverview_pushButton)
        self.clear_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.horizontalLayout_3.addWidget(self.clear_pushButton)
        self.verticalLayout_7.addWidget(self.widget_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.modeSelect.setText(_translate("Form", "                      选择生成模式"))
        self.DIYMode.setText(_translate("Form", "自定义"))
        self.senceMode.setText(_translate("Form", "使用场景生成"))
        self.actionMode.setText(_translate("Form", "使用动作生成"))
        self.dimSelect_label.setText(_translate("Form", "                    选择数据生成的维度"))
        self.fiveDim_radioButton.setText(_translate("Form", "5维"))
        self.eightDim_radioButton.setText(_translate("Form", "8维"))
        self.twelveDim_radioButton.setText(_translate("Form", "12维"))
        self.sigWidth_checkBox.setText(_translate("Form", "脉冲宽度"))
        self.repeatFre_checkBox.setText(_translate("Form", "重复频率"))
        self.height_checkBox.setText(_translate("Form", "高度"))
        self.y_checkBox.setText(_translate("Form", "y坐标"))
        self.x_checkBox.setText(_translate("Form", "x坐标"))
        self.dis_checkBox.setText(_translate("Form", "距离"))
        self.powerDen_checkBox.setText(_translate("Form", "功率密度"))
        self.speed_checkBox.setText(_translate("Form", "速度"))
        self.direct_checkBox.setText(_translate("Form", "航向角"))
        self.z_angle_checkBox.setText(_translate("Form", "俯仰角"))
        self.dutyCycle_checkBox.setText(_translate("Form", "占空比"))
        self.radarFre_checkBox.setText(_translate("Form", "雷达频率"))
        self.label.setText(_translate("Form", "                            场景设置"))
        self.selectScen_radioButton.setText(_translate("Form", "文件导入"))
        self.makeScen_radioButton.setText(_translate("Form", "高级设置"))
        self.form_settings.setText(_translate("Form", "                            编队设置"))
        self.form_num_label.setText(_translate("Form", "编队数量:"))
        self.form_commit_pushButton.setText(_translate("Form", "√"))
        self.form.setText(_translate("Form", "编队"))
        self.formnum_label.setText(_translate("Form", "设置"))
        self.form_type_label.setText(_translate("Form", "编队种类:"))
        self.form_type_comboBox.setItemText(0, _translate("Form", "梯形"))
        self.form_type_comboBox.setItemText(1, _translate("Form", "菱形"))
        self.form_type_comboBox.setItemText(2, _translate("Form", "蛇形"))
        self.type_comboBox.setItemText(0, _translate("Form", "侦察机"))
        self.type_comboBox.setItemText(1, _translate("Form", "战斗机"))
        self.type_comboBox.setItemText(2, _translate("Form", "轰炸机"))
        self.type_comboBox.setItemText(3, _translate("Form", "预警机"))
        self.type_comboBox.setItemText(4, _translate("Form", "直升机"))
        self.type_label.setText(_translate("Form", "飞机种类:"))
        self.num_label.setText(_translate("Form", "飞机数量:"))
        self.base_action_label.setText(_translate("Form", "基本动类型:"))
        self.turn_action_pushButton.setText(_translate("Form", "转弯"))
        self.line_action_pushButton.setText(_translate("Form", "平飞"))
        self.drive_up_action_pushButton.setText(_translate("Form", "上升"))
        self.drive_down_action_pushButton.setText(_translate("Form", "俯冲"))
        self.more_action_label.setText(_translate("Form", "附加机动类型:"))
        self.s_action_pushButton.setText(_translate("Form", "s型"))
        self.o_action_pushButton.setText(_translate("Form", "o型"))
        self.addPlane_pushButton.setText(_translate("Form", "加入编队"))
        self.pushButton_5.setText(_translate("Form", "提交"))
        self.dataShow_groupBox.setTitle(_translate("Form", "数据展示窗口"))
        self.form_commiti_pushButton.setText(_translate("Form", "生成数据"))
        self.revoke_pushButton.setText(_translate("Form", "撤销"))
        self.sceneSave_pushButton.setText(_translate("Form", "保存设置"))
        self.data_save_pushButton.setText(_translate("Form", "保存数据"))
        self.dataOverview_pushButton.setText(_translate("Form", "数据预览"))
        self.clear_pushButton.setText(_translate("Form", "清除"))

