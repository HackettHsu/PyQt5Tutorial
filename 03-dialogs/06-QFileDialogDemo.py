# lesson48 2020年4月30日 20:28:07-20:55:57
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QFileDialogDemo")
        self.resize(500, 500)
        layout = QVBoxLayout()
        self.button1 = QPushButton("加载图片")
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)
        self.imageLabel1 = QLabel()
        layout.addWidget(self.imageLabel1)

        self.button2 = QPushButton("加载文件")
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)
        self.content1 = QTextEdit()
        layout.addWidget(self.content1)
        self.setLayout(layout)

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, "打开文件", ".", "图像文件(*.jpg *.png)")
        self.imageLabel1.setPixmap(QPixmap(fname))

    def loadText(self):
        # 打开文件方法2：直接使用QFileDialog
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        # 显示对话框
        if dialog.exec():
            # 如果打开成功
            fname = dialog.selectedFiles()
            f = open(fname[0], "r", encoding="UTF-8")
            # 读取文件。这是基本的Python API
            # with方法打开文件：之前学过的。处理完后自动关闭文件。
            with f:
                data = f.read()
                # 用content1控件显示文件内容
                self.content1.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())