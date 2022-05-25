# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1093, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas = QtWidgets.QGraphicsView(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(40, 50, 820, 740))
        self.canvas.setInteractive(True)
        self.canvas.setObjectName("canvas")
        self.comboBox_neighourhood = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_neighourhood.setGeometry(QtCore.QRect(890, 70, 141, 22))
        self.comboBox_neighourhood.setObjectName("comboBox_neighourhood")
        self.comboBox_neighourhood.addItem("")
        self.comboBox_neighourhood.addItem("")
        self.comboBox_neighourhood.addItem("")
        self.comboBox_neighourhood.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(890, 50, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 120, 151, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_distribution = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_distribution.setGeometry(QtCore.QRect(890, 140, 141, 22))
        self.comboBox_distribution.setObjectName("comboBox_distribution")
        self.comboBox_distribution.addItem("")
        self.comboBox_distribution.addItem("")
        self.comboBox_distribution.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(890, 190, 151, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_boundaries = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_boundaries.setGeometry(QtCore.QRect(890, 210, 141, 22))
        self.comboBox_boundaries.setObjectName("comboBox_boundaries")
        self.comboBox_boundaries.addItem("")
        self.comboBox_boundaries.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(890, 260, 55, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox_width = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_width.setGeometry(QtCore.QRect(890, 280, 61, 22))
        self.spinBox_width.setMaximum(820)
        self.spinBox_width.setProperty("value", 820)
        self.spinBox_width.setObjectName("spinBox_width")
        self.spinBox_height = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_height.setGeometry(QtCore.QRect(970, 280, 61, 22))
        self.spinBox_height.setMaximum(740)
        self.spinBox_height.setProperty("value", 740)
        self.spinBox_height.setObjectName("spinBox_height")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(890, 360, 131, 16))
        self.label_5.setObjectName("label_5")
        self.spinBox_nucleon_count = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_nucleon_count.setGeometry(QtCore.QRect(890, 380, 61, 22))
        self.spinBox_nucleon_count.setMaximum(100)
        self.spinBox_nucleon_count.setProperty("value", 30)
        self.spinBox_nucleon_count.setObjectName("spinBox_nucleon_count")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 310, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(890, 430, 141, 28))
        self.pushButton_start.setObjectName("pushButton_start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_picture_as = QtGui.QAction(MainWindow)
        self.actionSave_picture_as.setObjectName("actionSave_picture_as")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave_picture_as)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_neighourhood.setItemText(0, _translate("MainWindow", "von Neumann"))
        self.comboBox_neighourhood.setItemText(1, _translate("MainWindow", "Moore"))
        self.comboBox_neighourhood.setItemText(2, _translate("MainWindow", "Pentagonal"))
        self.comboBox_neighourhood.setItemText(3, _translate("MainWindow", "Hexagonal"))
        self.label.setText(_translate("MainWindow", "Neighbourhood type"))
        self.label_2.setText(_translate("MainWindow", "Nucleon distribution type"))
        self.comboBox_distribution.setItemText(0, _translate("MainWindow", "Random"))
        self.comboBox_distribution.setItemText(1, _translate("MainWindow", "Custom"))
        self.comboBox_distribution.setItemText(2, _translate("MainWindow", "Regular"))
        self.label_3.setText(_translate("MainWindow", "Boundary condition type"))
        self.comboBox_boundaries.setItemText(0, _translate("MainWindow", "Absolute"))
        self.comboBox_boundaries.setItemText(1, _translate("MainWindow", "Periodic"))
        self.label_4.setText(_translate("MainWindow", "Size"))
        self.label_5.setText(_translate("MainWindow", "Nucleon count"))
        self.pushButton.setText(_translate("MainWindow", "Generate space"))
        self.pushButton_start.setText(_translate("MainWindow", "Start simulation"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_picture_as.setText(_translate("MainWindow", "Save picture as"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
