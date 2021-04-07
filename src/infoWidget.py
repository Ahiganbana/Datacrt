from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_infoWidget import Ui_Form

class InfoWidget(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.setupUi(self)
    def setupUi(self, Form):
        self.textEdit.setReadOnly(True)
        self.setWindowTitle("配置预览")