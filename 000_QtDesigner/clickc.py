# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Pycharm_Project\image_recognize\clickc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 170, 93, 28))
        self.pushButton.setObjectName("pushButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        self.pushButton.clicked.connect(self.on_clicked)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Qt测试"))
        self.pushButton.setText(_translate("mainWindow", "PushButton"))
        self.menu.setTitle(_translate("mainWindow", "菜单"))

    def on_clicked(self):
        QtWidgets.QMessageBox.information(self.pushButton, '标题', '测试斤斤计较')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    mainwindows = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainwindows)
    mainwindows.show()
    sys.exit(app.exec_())

