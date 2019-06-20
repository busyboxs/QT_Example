from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QHBoxLayout, QGroupBox, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Windows(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'HBox Layout'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = 'avatar.png'

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle((self.title))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox('测试一下这是什么？')
        hboxLayout = QHBoxLayout()

        self.button = QPushButton('第一个', self)
        self.button.setIcon(QtGui.QIcon('avatar.png'))
        self.button.setIconSize(QtCore.QSize(25, 25))
        self.button.setMinimumHeight(25)
        hboxLayout.addWidget(self.button)

        self.button2 = QPushButton('第二个', self)
        self.button2.setIcon(QtGui.QIcon('avatar.png'))
        self.button2.setIconSize(QtCore.QSize(25, 25))
        self.button2.setMinimumHeight(25)
        hboxLayout.addWidget(self.button2)

        self.button3 = QPushButton('第三个', self)
        self.button3.setIcon(QtGui.QIcon('avatar.png'))
        self.button3.setIconSize(QtCore.QSize(25, 25))
        self.button3.setMinimumHeight(25)
        hboxLayout.addWidget(self.button3)

        self.groupBox.setLayout(hboxLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Windows()
    sys.exit(app.exec_())