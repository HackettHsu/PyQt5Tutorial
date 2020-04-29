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
        # checkBox1是已选中状态，checkState应该输出2
        self.checkBox1 = QCheckBox("复选框控件1")
        # setChecked：设置默认勾选状态
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda : self.checkboxState(self.checkBox1))
        layout.addWidget(self.checkBox1)

        # checkBox2是未选中状态，输出0
        self.checkBox2 = QCheckBox("复选框控件2")
        self.checkBox2.stateChanged.connect(lambda : self.checkboxState(self.checkBox2))
        layout.addWidget(self.checkBox2)

        # checkBox3是半选中状态，应该输出1
        self.checkBox3 = QCheckBox("复选框控件3：半选中状态")
        self.checkBox3.stateChanged.connect(lambda : self.checkboxState(self.checkBox3))
        # 半选中要设置以下两个属性
        # 属性1:Tristate 三态。是否允许半选中
        self.checkBox3.setTristate(True)
        # 属性2：setCheckState中的Qt.PartiallyChecked，表示正处于半选中状态
        # 注意：Qt.PartiallyChecked不要加括号
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)
    
    def checkboxState(self, cb):
        check1State = self.checkBox1.text() + ', isChecked = ' + str(self.checkBox1.isChecked()) \
            + ', checkState = ' + str(self.checkBox1.checkState()) + '\n' # 上一行结尾斜杠是代码跨行
        check2State = self.checkBox2.text() + ', isChecked = ' + str(self.checkBox2.isChecked()) \
            + ', checkState = ' + str(self.checkBox2.checkState()) + '\n'
        check3State = self.checkBox3.text() + ', isChecked = ' + str(self.checkBox2.isChecked()) \
            + ', checkState = ' + str(self.checkBox3.checkState()) + '\n'
        print(check1State + check2State + check3State)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())