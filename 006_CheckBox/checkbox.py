from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox, QLabel
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Check Box'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 200
        self.iconName = 'avatar.png'
        self.initWindow()
        self.baseStr = 'You have select: '

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('avatar.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont('Sanserif', 13))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox('请选择（多选）。。。')
        self.groupBox.setFont(QtGui.QFont('Sanserif', 13))
        hboxLayout = QHBoxLayout()

        self.checkbox1 = QCheckBox('Python')
        self.checkbox1.setIcon(QtGui.QIcon('avatar.png'))
        self.checkbox1.setIconSize(QtCore.QSize(15, 15))
        self.checkbox1.setFont(QtGui.QFont('Sanserif', 13))
        self.checkbox1.toggled.connect(self.onCheckbox_toggled)
        hboxLayout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox('Java')
        self.checkbox2.setIcon(QtGui.QIcon('avatar.png'))
        self.checkbox2.setIconSize(QtCore.QSize(15, 15))
        self.checkbox2.setFont(QtGui.QFont('Sanserif', 13))
        self.checkbox2.toggled.connect(self.onCheckbox_toggled)
        hboxLayout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox('C++')
        self.checkbox3.setIcon(QtGui.QIcon('avatar.png'))
        self.checkbox3.setIconSize(QtCore.QSize(15, 15))
        self.checkbox3.setFont(QtGui.QFont('Sanserif', 13))
        self.checkbox3.toggled.connect(self.onCheckbox_toggled)
        hboxLayout.addWidget(self.checkbox3)

        self.groupBox.setLayout(hboxLayout)

    def onCheckbox_toggled(self):
        strlist = []

        if self.checkbox1.isChecked():
            strlist.append(self.checkbox1.text())
        if self.checkbox2.isChecked():
            strlist.append(self.checkbox2.text())
        if self.checkbox3.isChecked():
            strlist.append(self.checkbox3.text())
        self.label.setText(self.baseStr + ', '.join(strlist))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

