from PyQt5.QtWidgets import QApplication, QDialog, QRadioButton, QHBoxLayout, QGroupBox, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Radio Buttom'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 200
        self.iconName = 'avatar.png'
        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.label = QLabel('你选择了牛奶', self)
        self.label.setFont(QtGui.QFont('Sanserif', 15))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox("请选择一个。。。")
        self.groupBox.setFont(QtGui.QFont('Sanserif', 13))

        hboxLayout = QHBoxLayout()

        self.radiobutton1 = QRadioButton('牛奶')
        self.radiobutton1.setChecked(True)
        self.radiobutton1.setIcon(QtGui.QIcon('avatar.png'))
        self.radiobutton1.setIconSize(QtCore.QSize(25, 25))
        self.radiobutton1.setFont(QtGui.QFont('Sanserif', 13))
        self.radiobutton1.toggled.connect(self.onRadioBtn)
        hboxLayout.addWidget(self.radiobutton1)

        self.radiobtn2 = QRadioButton("蛋糕")
        self.radiobtn2.setIcon(QtGui.QIcon("avatar.png"))
        self.radiobtn2.setIconSize(QtCore.QSize(25, 25))
        self.radiobtn2.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn2.toggled.connect(self.onRadioBtn)
        hboxLayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton("奶茶")
        self.radiobtn3.setIcon(QtGui.QIcon("avatar.png"))
        self.radiobtn3.setIconSize(QtCore.QSize(25, 25))
        self.radiobtn3.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn3.toggled.connect(self.onRadioBtn)
        hboxLayout.addWidget(self.radiobtn3)
        self.groupBox.setLayout(hboxLayout)

    def onRadioBtn(self):
        randioBtn = self.sender()
        if randioBtn.isChecked():
            self.label.setText('你选择了' + randioBtn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
