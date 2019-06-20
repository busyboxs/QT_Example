from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout
import sys
from PyQt5 import QtGui


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Line Edit'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 200
        self.setWindowIcon(QtGui.QIcon('avatar.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont('Sanserif', 13))
        self.lineedit.returnPressed.connect(self.onPressed)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont('Sanserif', 13))
        hbox.addWidget(self.label)
        hbox.addWidget(self.lineedit)
        self.setLayout(hbox)
        self.show()

    def onPressed(self):
        self.label.setText(self.lineedit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
