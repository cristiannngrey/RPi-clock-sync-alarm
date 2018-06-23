# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project-clock_v2.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import sys
from datetime import datetime
import calendar
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.hour = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Serif Blk")
        font.setPointSize(150)
        font.setBold(True)
        font.setWeight(75)
        self.hour.setFont(font)
        self.hour.setAlignment(QtCore.Qt.AlignCenter)
        self.hour.setObjectName("hour")
        self.gridLayout.addWidget(self.hour, 1, 1, 1, 1)
        self.date = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(55)
        self.date.setFont(font)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hour.setText(_translate("MainWindow", ""))
        self.date.setText(_translate("MainWindow", ""))

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.showFullScreen()
    MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def update_time():
        TIME = datetime.now()
        year = str(TIME.year)
        month = TIME.month
        date = "%02d" % TIME.day
        hr = "%02d" % TIME.hour
        mn = "%02d" % TIME.minute
        sec = "%02d" % TIME.second
        day = calendar.weekday(TIME.year, TIME.month, TIME.day) 
        Day = ''

        if day == 0:
            Day = "Monday"
        elif day == 1:
            Day = "Tuesday"
        elif day == 2:
            Day = "Wednesday"
        elif day == 3:
            Day = "Thursday"
        elif day == 4:
            Day = "Friday"
        elif day == 5:
            Day = "Saturday"
        elif day == 6:
            Day = "Sunday"            

        if month == 1:
            Month = "January"
        elif month == 2:
            Month = "February"
        elif month == 3:
            Month = "March"
        elif month == 4:
            Month = "April"
        elif month == 5:
            Month = "May"
        elif month == 6:
            Month = "June"
        elif month == 7:
            Month = "July"
        elif month == 8:
            Month = "August"
        elif month == 9:
            Month = "September"
        elif month == 10:
            Month = "October"
        elif month == 11:
            Month = "November"
        elif month == 12:
            Month = "December"
        

        ui.hour.setText(hr+":"+mn+":"+sec)
        ui.date.setText(Day+","+Month+" "+date+" "+year)

        
        
    timer = QtCore.QTimer()
    timer.timeout.connect(update_time)
    timer.start(1000)

    sys.exit(app.exec())