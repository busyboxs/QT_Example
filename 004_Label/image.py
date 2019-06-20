from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Label Image'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 200
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon('avatar.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        # labelImage.setFixedSize(400, 200)
        pixmap = QPixmap('test.jpg')
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
