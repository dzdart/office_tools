# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tanchuang.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(479, 327)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.QL_GIF = QtWidgets.QLabel(self.centralwidget)
        self.QL_GIF.setGeometry(QtCore.QRect(10, 10, 199, 149))
        self.QL_GIF.setStyleSheet("")
        self.QL_GIF.setText("")
        self.QL_GIF.setObjectName("QL_GIF")
        self.QB_Button = QtWidgets.QPushButton(self.centralwidget)
        self.QB_Button.setGeometry(QtCore.QRect(60, 30, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QB_Button.sizePolicy().hasHeightForWidth())
        self.QB_Button.setSizePolicy(sizePolicy)
        self.QB_Button.setMinimumSize(QtCore.QSize(100, 100))
        self.QB_Button.setMaximumSize(QtCore.QSize(100, 100))
        self.QB_Button.setText("")
        self.QB_Button.setObjectName("QB_Button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
