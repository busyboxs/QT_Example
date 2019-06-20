from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QGridLayout, QGroupBox, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QRect


class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Grid Layout'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 200
        self.iconName = 'avatar.png'
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox('grid layout test')

        gridLayout = QGridLayout()

        self.button = QPushButton('第一个', self)
        self.button.setIcon(QtGui.QIcon(self.iconName))
        self.button.setIconSize(QtCore.QSize(25, 25))
        self.button.setMinimumHeight(25)
        gridLayout.addWidget(self.button, 0, 0)

        self.button2 = QPushButton('第二个', self)
        self.button2.setIcon(QtGui.QIcon(self.iconName))
        self.button2.setIconSize(QtCore.QSize(25, 25))
        self.button2.setMinimumHeight(25)
        gridLayout.addWidget(self.button2, 0, 1)

        self.button3 = QPushButton('第三个', self)
        self.button3.setIcon(QtGui.QIcon(self.iconName))
        self.button3.setIconSize(QtCore.QSize(25, 25))
        self.button3.setMinimumHeight(25)
        gridLayout.addWidget(self.button3, 1, 0)

        self.button4 = QPushButton('第四个', self)
        self.button4.setIcon(QtGui.QIcon(self.iconName))
        self.button4.setIconSize(QtCore.QSize(25, 25))
        self.button4.setMinimumHeight(25)
        gridLayout.addWidget(self.button4, 1, 1)

        self.groupBox.setLayout(gridLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
