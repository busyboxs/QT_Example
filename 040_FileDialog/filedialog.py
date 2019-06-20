from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Open File'
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.initWindow()

    def initWindow(self):

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('avatar.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()


        self.btn1 = QPushButton('选择图像')
        self.btn1.clicked.connect(self.getImage)
        vbox.addWidget(self.btn1)

        # self.btn2 = QPushButton('图像检测')
        # self.btn2.clicked.connect(self.detectImage)
        # vbox.addWidget(self.btn2)

        self.label = QLabel(self)
        self.label.setFixedSize(500, 400)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.show()

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:/', 'Image file (*.jpg *.gif)')
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        pixmapscared = pixmap.scaledToHeight(300)
        self.label.setPixmap(pixmapscared)
        # self.label.setFixedHeight(500)
        # self.label.heightForWidth(self.label.width())
        self.label.setScaledContents(True)
        print(pixmap.width())
        print(pixmap.height())
        print(self.label.width())
        print(self.label.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
