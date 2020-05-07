# lesson 118 10:01:21-10:12:41
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class WindowStyleDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WindowStyleDemo")
        self.resize(500, 500)
        layout = QHBoxLayout()
        self.styleLabel = QLabel("设置窗口风格")
        self.styleComboBox = QComboBox()
        self.styleComboBox.addItems(QStyleFactory.keys())
        # 获取当前窗口风格
        index = self.styleComboBox.findText(QApplication.style().objectName(), \
            Qt.MatchFixedString)
        self.styleComboBox.setCurrentIndex(index)
        self.styleComboBox.activated[str].connect(self.handleStyleChanged)
        layout.addWidget(self.styleLabel)
        layout.addWidget(self.styleComboBox)
        self.setLayout(layout)

    def handleStyleChanged(self, style):
        QApplication.setStyle(style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowStyleDemo()
    main.show()
    sys.exit(app.exec_())