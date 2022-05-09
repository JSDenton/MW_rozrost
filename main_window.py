import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from main import read_colors

colors = read_colors("colors.txt")

class Main_window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("main_window.ui", self)
        self.spinBox_width.maximum = self.canvas.width
        self.spinBox_height.maximum = self.canvas.height
        self.spinBox_nucleon_count.maximum = len(colors)
