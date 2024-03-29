from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'First Window'
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon('avatar.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    sys.exit(app.exec_())