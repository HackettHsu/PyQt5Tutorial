'''
作为模板存在的文件
每次新建文件时可直接利用模板的代码，替换掉FileName部分即可
节约时间
'''
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FileName(QWidget):
    def __init__(self):
        super(FileName, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("FileName")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = FileName()
    main.show()
    sys.exit(app.exec_())