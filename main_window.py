import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic


class Main_window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("main_window.ui", self)
        self.spinBox_width.maximum = self.canvas.Width
        self.spinBox_height.maximum = self.canvas.Height
