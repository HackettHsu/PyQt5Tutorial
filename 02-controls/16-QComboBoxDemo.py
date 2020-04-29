# lesson 40
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件演示")
        self.resize(300, 100)
        layout = QVBoxLayout()

        self.label = QLabel("请选择编程语言")
        self.comboBox = QComboBox()
        self.comboBox.addItem("C++")
        self.comboBox.addItem("Python")
        self.comboBox.addItems(['Java', 'C#', 'Ruby'])
        # 若当前所选发生改变就发送信号
        # 这种信号默认传两个参数，第二个参数为可选项个数index
        self.comboBox.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.label)
        layout.addWidget(self.comboBox)
        self.setLayout(layout)

    def selectionChange(self, i):
        # 获得当前选择的文本
        self.label.setText(self.comboBox.currentText())
        # 自适应下拉项尺寸
        self.label.adjustSize()
        # 显示所有项目的状态
        for count in range(self.comboBox.count()):
            # item 项目count = 项目count内容
            print(f"item {str(count)} = {self.comboBox.itemText(count)}")
            # current index 当前选择项目的序号（索引） selection changed 当前选择项目的名称
            print(f"current index {i} selection changed {self.comboBox.currentText()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())