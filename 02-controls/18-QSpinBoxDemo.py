# lesson 42
'''
作为模板存在的文件
每次新建文件时可直接利用模板的代码，替换掉QSpinBoxDemo部分即可
节约时间
'''
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QSpinBox演示")
        self.resize(300, 100)
        layout = QVBoxLayout()
        self.label = QLabel("当前值")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.spinBox = QSpinBox()
        self.spinBox.valueChanged.connect(self.valueChange)
        layout.addWidget(self.spinBox)
        self.setLayout(layout)

    def valueChange(self):
        self.label.setText("当前值：" + str(self.spinBox.value()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())