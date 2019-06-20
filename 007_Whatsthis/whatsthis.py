from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QWhatsThis
from PyQt5 import QtGui
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'What is this'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 200
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('avatar.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()
        label = QLabel('Focus And Press SHIFT + F1')
        hbox.addWidget(label)

        button = QPushButton('Click Me', self)
        button.setWhatsThis('可以按的按钮')
        hbox.addWidget(button)
        self.setLayout(hbox)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())