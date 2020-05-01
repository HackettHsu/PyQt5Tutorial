# lesson 54 2020年5月1日 21:26:03-21:51:17
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyComboxBox(QComboBox): # combox:组合框
    def __init__(self):
        super(MyComboxBox, self).__init__()
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        print(event)
        # mimeData：PyQt5自创用于存储数据的容器，具体之后会解释
        if event.mimeData().hasText():
            # 存在数据则接受
            event.accept()

    def dropEvent(self, event):
        self.addItem(event.mimeData().text())

class DragDorpDemo(QWidget):
    def __init__(self):
        super(DragDorpDemo, self).__init__()
        self.setWindowTitle("DragDropDemo")
        layout = QFormLayout()
        layout.addRow(QLabel("请将左边的文本拖拽到右边的下拉列表中"))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)
        combo = MyComboxBox()
        layout.addRow(lineEdit, combo)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DragDorpDemo()
    main.show()
    sys.exit(app.exec_())