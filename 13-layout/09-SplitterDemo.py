# lesson 104 22:34:31-22:50:05
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SplitterDemo(QWidget):
    def __init__(self):
        super(SplitterDemo, self).__init__()
        self.setWindowTitle("SplitterDemo")
        self.resize(500, 500)
        # 创建两个面板并设置外观
        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        # 创建横向拖动条
        splitter1 = QSplitter(Qt.Horizontal)
        textEdit = QTextEdit()
        # 添加控件到拖动条
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textEdit)
        # 改变默认尺寸
        splitter1.setSizes([100, 200])
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        layout = QHBoxLayout()
        layout.addWidget(splitter2)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = SplitterDemo()
    main.show()
    sys.exit(app.exec_())