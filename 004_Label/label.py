from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Label Test'
        self.top = 200
        self.left = 200
        self.width = 400
        self.height = 200
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon('avatar.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        label = QLabel('This is Labels')
        vbox.addWidget(label)
        label2 = QLabel('Label style to show')
        label2.setFont(QtGui.QFont('Sanserif', 20))
        label2.setStyleSheet('color:green')
        vbox.addWidget(label2)
        self.setLayout(vbox)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
