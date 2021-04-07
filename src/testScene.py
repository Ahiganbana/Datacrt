import sys
import Ui_sceneSelect as ui
from ui_myScene import Ui_MyScene
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #show = ui.Ui_Form()
    show = Ui_MyScene()
    show.show()
    sys.exit(app.exec_())