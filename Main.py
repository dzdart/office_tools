from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, uic
from ui import Ui_MainWindow as mainui
import threading
import time

import sys


class Main_wind(QtWidgets.QMainWindow, mainui):
    def __init__(self, parent=None):
        super(Main_wind, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet('background-image: url(:/icon/Sourse/MainBG.png);')
        self.sub = QD()
        self.But_Mail.clicked.connect(self.showMsg)
        self.But_Msg.clicked.connect(self.sub.ui.show)

    def showMsg(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.resize(200, 150)
        self.dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        # 获取桌面大小，并移动做右下角
        desktop = QtWidgets.QApplication.desktop()
        desktop_size = [desktop.width(), desktop.height()]
        positionA = [int(desktop_size[0] - 200), int(desktop_size[1] - 150)]
        self.dialog.move(positionA[0], positionA[1] - 45)

        gif = QtGui.QMovie('./Sourse/1mail.gif')
        QL_Gif = QtWidgets.QLabel(self.dialog)
        QL_Gif.setStyleSheet('background-color: rgba(1, 0, 0, 0)')
        QL_Gif.setMovie(gif)
        gif.start()
        self.dialog.setStyleSheet('background-color: rgba(1, 0, 0, 0)')
        QB_Push = QtWidgets.QPushButton(self.dialog)
        QB_Push.resize(200, 150)
        QB_Push.setStyleSheet('background-color: rgba(1, 0, 0, 0)')
        QB_Push.clicked.connect(self.dialog.close)
        threading.Thread(target=self.sleep_clos, args=([self.dialog, 5])).start()  # 定时关闭弹窗
        self.dialog.exec_()

    def sleep_clos(self, w: QtWidgets, s=5):
        """
        1、要关闭的widget
        2、延迟适建
        """
        time.sleep(s)
        w.close()


class QD:
    def __init__(self):
        super(QD, self).__init__()
        self.ui = uic.loadUi("./MailTaskList.ui")
        self.ui.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        print(123)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    UI = Main_wind()
    # UI.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    UI.show()
    sys.exit(app.exec_())
