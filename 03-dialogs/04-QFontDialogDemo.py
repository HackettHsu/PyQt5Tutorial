# lesson 45 2020年4月30日 17:12:36-17:17:28
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("FontDialog 示例")
        layout = QVBoxLayout()
        self.fontButton = QPushButton("选择字体")
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)
        self.fontLabel = QLabel("Hello, 字体效果测试")
        layout.addWidget(self.fontLabel)
        self.setLayout(layout)

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())