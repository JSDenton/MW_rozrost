from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

from main_window import Main_window

def read_colors(filename):
    colors = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line[0]!='#':
                colors.append(line[0:6])
    return colors

def _window():
    #-----initiate the window---------
    app = QApplication(sys.argv)
    window = Main_window()    
    
    #-----display and init save exit---------
    window.show()
    sys.exit(app.exec())


def _main():
    _window()

    return

_main()

#TODO:
#different types of neighbourhood
#different types 