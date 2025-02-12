# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conveyor_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets,QtSerialPort
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSerialPort import *
from PyQt5 import QtSerialPort
from PyQt5.QtCore import *
from PyQt5.QtSerialPort import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import time

##ser = serial.Serial('COM6', 9800, timeout=1)
class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__()

        self.port_com_port = QtSerialPort.QSerialPort()
        self.port_com_port.setPortName("COM6")
        self.port_com_port.setBaudRate(QSerialPort.BaudRate.Baud9600)
        
        self.port_com_port.setStopBits(QSerialPort.StopBits.OneStop)

        self.port_com_port.open(QIODevice.ReadWrite)
        self.port_com_port.readyRead.connect(self.count)
        self.count_r=0
        self.count_g=0
        self.count_b=0
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1001, 751))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(80, 30, 191, 201))
        self.frame_2.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(390, 30, 191, 201))
        self.frame_3.setStyleSheet("background-color:rgb(0, 255, 0)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(700, 30, 191, 201))
        self.frame_4.setStyleSheet("background-color:rgb(0, 0, 255)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.redCount = QtWidgets.QLabel(self.frame_5)
        self.redCount.setGeometry(QtCore.QRect(160, 40, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.redCount.setFont(font)
        self.redCount.setObjectName("redCount")
        self.greenCounr = QtWidgets.QLabel(self.frame_5)
        self.greenCounr.setGeometry(QtCore.QRect(460, 40, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.greenCounr.setFont(font)
        self.greenCounr.setObjectName("greenCounr")
        self.blueCount = QtWidgets.QLabel(self.frame_5)
        self.blueCount.setGeometry(QtCore.QRect(770, 40, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.blueCount.setFont(font)
        self.blueCount.setObjectName("blueCount")
        
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Object Sorting Software"))
        self.redCount.setText(_translate("MainWindow", "0"))
        self.greenCounr.setText(_translate("MainWindow", "0"))
        self.blueCount.setText(_translate("MainWindow", "0"))
        ##self.timer = QtCore.QTimer(self)

        
    def count(self):
  
     
        data = self.port_com_port.readAll()
        print(data)
        forBlue = [b"B",b"BB",b"lue",b"ue",b"Blue",b"e"]
        forGreen = [b"Gree",b"n",b"Gr","een",b"GG",b"en",b"Green",b"reen",b"G"]
        forRed = [b"RR",b"Re",b"Red",b"ed",b"d",b"R"]
        if data in forBlue:
            
            self.count_b=self.count_b+1
            print("colour is blue",self.count_b)
            self.blueCount.setText(str(self.count_b))
       
        if data in forGreen:
            
            self.count_g=self.count_g+1
            print("colour is Green",self.count_g)
            self.greenCounr.setText(str(self.count_g))
            
        if data in forRed:
            
            self.count_r=self.count_r+1
            print("colour is Red",self.count_b)
            self.redCount.setText(str(self.count_r))
            time.sleep(2)
        
        
        
        
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


