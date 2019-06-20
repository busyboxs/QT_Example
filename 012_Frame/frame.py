from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QPushButton
import sys
from PyQt5 import QtGui, QtCore


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Frame'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 200

        self.setWindowIcon(QtGui.QIcon('avatar.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:yellow')

        hbox = QHBoxLayout()
        btn1 = QPushButton('Click Me')
        btn1.setStyleSheet('color:white')
        btn1.setStyleSheet('background-color:green')
        btn1.setFont(QtGui.QFont('Sanserif', 15))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(1.0)
        hbox.addWidget(frame)
        hbox.addWidget(btn1)
        self.setLayout(hbox)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
