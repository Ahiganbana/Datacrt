import sys
import Ui_MainWindow as ui
from ui_MyMainWindow import Ui_MyMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #show = ui.Ui_Form()
    show = Ui_MyMainWindow()
    show.show()
    sys.exit(app.exec_())