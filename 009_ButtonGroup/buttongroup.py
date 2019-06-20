from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QButtonGroup, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Button Group'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 200
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('avatar.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.label = QLabel('This is label', self)
        self.label.setFont(QtGui.QFont('Sanserif', 13))
        vbox.addWidget(self.label)

        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        button = QPushButton('Python')
        self.buttongroup.addButton(button, 1)
        self.buttongroup.addButton(button, 1)
        button.setFont(QtGui.QFont("Sanserif", 13))
        button.setIcon(QtGui.QIcon("avatar.png"))
        button.setIconSize(QtCore.QSize(15, 15))
        hbox.addWidget(button)

        button = QPushButton("Java")
        self.buttongroup.addButton(button, 2)
        button.setFont(QtGui.QFont("Sanserif", 13))
        button.setIcon(QtGui.QIcon("avatar.png"))
        button.setIconSize(QtCore.QSize(15, 15))
        hbox.addWidget(button)

        button = QPushButton("C++")
        self.buttongroup.addButton(button, 3)
        button.setFont(QtGui.QFont("Sanserif", 13))
        button.setIcon(QtGui.QIcon("avatar.png"))
        button.setIconSize(QtCore.QSize(15, 15))
        hbox.addWidget(button)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.show()

    def on_button_clicked(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text() + ' Was Clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
