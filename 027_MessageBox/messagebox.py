from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFontDialog, QColorDialog, QFileDialog, QMessageBox
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.Qt import QFileInfo


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'MessagrBox'
        self.top = 200
        self.left = 400
        self.width = 680
        self.height = 480

        self.setWindowIcon(QIcon('avatar.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateEditor()
        self.CreateMenu()
        self.show()

    def CreateEditor(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')

        printAction = QAction(QIcon('print.png'), 'Print', self)
        printAction.triggered.connect(self.printDialog)

        fileMenu.addAction(printAction)

        printPreviewAction = QAction(QIcon('printprev.png'), 'Print Preview', self)
        printPreviewAction.triggered.connect(self.printpreviewDialog)
        fileMenu.addAction(printPreviewAction)

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

        copyAction = QAction(QIcon('copy.png'), 'Copy', self)
        copyAction.setShortcut('Ctrl+C')
        editMenu.addAction(copyAction)

        saveAction = QAction(QIcon('save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        editMenu.addAction(saveAction)

        pasteAction = QAction(QIcon('paste.png'), 'Paste', self)
        pasteAction.setShortcut('Ctrl+P')
        editMenu.addAction(pasteAction)

        fontAction = QAction(QIcon('font.png'), 'Font', self)
        fontAction.setShortcut('Ctrl+F')
        fontAction.triggered.connect(self.fontDialog)
        viewMenu.addAction(fontAction)

        colorAction = QAction(QIcon('color.png'), 'Color', self)
        colorAction.triggered.connect(self.colorDialog)
        viewMenu.addAction(colorAction)

        helpAction = QAction(QIcon('about.png'), 'About Application', self)
        helpAction.triggered.connect(self.AboutmessageBox)
        helpMenu.addAction(helpAction)

        choiceAction = QAction(QIcon('new.png'), 'Choice Message', self)
        choiceAction.triggered.connect(self.choiceMessageBox)
        helpMenu.addAction(choiceAction)

        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(fontAction)
        self.toolbar.addAction(colorAction)
        self.toolbar.addAction(printAction)
        self.toolbar.addAction(printPreviewAction)
        self.toolbar.addAction(helpAction)

    def exitWindow(self):
        self.close()

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def printpreviewDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()

    def printPreview(self, printer):
        self.textEdit.print_(printer)

    def AboutmessageBox(self):
        QMessageBox.about(self, 'About Application', 'This is a simple texteditor application')

    def choiceMessageBox(self):
        message = QMessageBox.question(self, 'Choise Message', 'Do You Like PyQt5?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if message == QMessageBox.Yes:
            print('Yes, I like PyQt5')
        else:
            print('No, I do not like PyQt5')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

