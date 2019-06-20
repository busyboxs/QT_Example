import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        title = '按钮测试'
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = 'avatar.png'
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        self.uiComponents()
        self.show()

    def uiComponents(self):
        buttom = QPushButton('Close Application', self)
        buttom.setGeometry(100, 100, 150, 40)
        buttom.setIcon(QtGui.QIcon('avatar.png'))
        buttom.setIconSize(QtCore.QSize(20, 20))
        buttom.setToolTip('This is click buttom')
        buttom.clicked.connect(self.ButtomAction)

    def ButtomAction(self):
        print('Hello World!')
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    sys.exit(app.exec_())