# lesson 63 2020年5月23日 17:25:14-17:36:22
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

class PrintDialogDemo(QWidget):
    def __init__(self):
        super(PrintDialogDemo, self).__init__()
        # self.printer相当于打印机
        self.printer = QPrinter()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("PrintDialogDemo")
        self.resize(500, 500)
        self.editor = QTextEdit(self)
        self.editor.setGeometry(20, 20, 300, 270)
        self.openButton = QPushButton("打开文件", self)
        self.openButton.move(350, 20)
        self.openButton.clicked.connect(self.openFile)
        self.settingButton = QPushButton("打印设置", self)
        self.settingButton.move(350, 50)
        self.settingButton.clicked.connect(self.settingDialog)
        self.printButton = QPushButton("打印文档", self)
        self.printButton.move(350, 80)
        self.printButton.clicked.connect(self.printDialog)
    
    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文本文件', '/')
        if fname[0]:
            with open(fname[0], 'r', encoding='utf-8', errors = 'ignore') as f:
                self.editor.setText(f.read())
        
    def settingDialog(self):
        printDialog = QPageSetupDialog(self.printer, self)
        printDialog.exec()
    
    def printDialog(self):
        printdialog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printdialog.exec():
            self.editor.print(self.printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = PrintDialogDemo()
    main.show()
    sys.exit(app.exec_())