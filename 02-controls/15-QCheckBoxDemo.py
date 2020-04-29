import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("复选框控件演示")
        layout = QHBoxLayout()
        self.checkBox1 = QCheckBox("复选框控件1")
        # setChecked：设置默认勾选状态
        self.checkBox1.setChecked(True)
        layout.self.ch
    
    def checkboxState(self, cb):
        check1State = self.checkBox1.text() + ', isChecked = ' + str(self.checkBox1.isChecked()) \
            + ', checkState = ' + self.checkBox1..checkState() + '\n' # 上一行斜杠是代码跨行
        check2State = self.checkBox2.text() + ', isChecked = ' + str(self.checkBox2.isChecked()) \
            + ', checkState = ' + self.checkBox2.checkState() + '\n'
        check3State = self.checkBox3.text() + ', isChecked = ' + str(self.checkBox2.isChecked()) \
            + ', checkState = ' + self.checkBox3.checkState() + '\n'
        print(check1State + check2State + check3State)

if __name__ == "__main__":
    app = QApplication()
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())