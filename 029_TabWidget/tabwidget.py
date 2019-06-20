import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QComboBox, QCheckBox, QGroupBox
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QDialogButtonBox
from PyQt5 import QtGui
from PyQt5 import QtCore


class Tab(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('TabWidget')
        self.setWindowIcon(QtGui.QIcon('avatar.png'))

        vbox = QVBoxLayout()
        tabWidget = QTabWidget()
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        tabWidget.setFont(QtGui.QFont('Sanserif', 12))
        tabWidget.addTab(TabContact(), 'Contact Details')
        tabWidget.addTab(TabPersonalDetails(), 'Personal Details')

        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)


class TabContact(QWidget):
    def __init__(self):
        super().__init__()
        nameLabel = QLabel('Name: ')
        nameEdit = QLineEdit()

        phoneLabel = QLabel('Phone: ')
        phoneEdit = QLineEdit()

        addressLabel = QLabel('Address: ')
        addressEdit = QLineEdit()

        emailLabel = QLabel('Email: ')
        emailEdit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(nameLabel)
        vbox.addWidget(nameEdit)
        vbox.addWidget(phoneLabel)
        vbox.addWidget(phoneEdit)
        vbox.addWidget(addressLabel)
        vbox.addWidget(addressEdit)
        vbox.addWidget(emailLabel)
        vbox.addWidget(emailEdit)
        self.setLayout(vbox)


class TabPersonalDetails(QWidget):

    def __init__(self):
        super().__init__()
        groupBox = QGroupBox('Select Your Gender')
        list = ['Male', 'Female']
        combo = QComboBox()
        combo.addItems(list)
        vbox = QVBoxLayout()
        vbox.addWidget(combo)
        groupBox.setLayout(vbox)

        groupBox2 = QGroupBox('Select Your Facorite Programming Language')

        python = QCheckBox('Python')
        cpp = QCheckBox('C++')
        java = QCheckBox('Java')
        csharp = QCheckBox('C#')

        vboxp = QVBoxLayout()
        vboxp.addWidget(python)
        vboxp.addWidget(cpp)
        vboxp.addWidget(java)
        vboxp.addWidget(csharp)
        groupBox2.setLayout(vboxp)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(groupBox2)
        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tabdialog = Tab()
    tabdialog.show()
    sys.exit(app.exec_())
