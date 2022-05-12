from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #-----display and init save exit---------
    


def _main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
    return

_main()

#TODO:
#different types of neighbourhood
#different types 