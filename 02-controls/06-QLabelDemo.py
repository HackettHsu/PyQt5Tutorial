'''
QLabel最基本使用方式
创建几个QLabel控件并绑定一些常用信号
'''
import sys
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QPushButton, QWidget, QLabel
from PyQt5.QtGui import QPalette,QPixmap # 调色板模块，显示图片模块
from PyQt5.QtCore import Qt, QFileInfo

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color = yellow>这是一个文本标签。</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue) # 设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href = '#'> 欢迎使用Python GUI程序</a.")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap(QFileInfo(__file__).absolutePath() + "./image/罗小黑战记 电影原声带.bmp"))

        label4.setOpenExternalLinks(True)# True，打开网页；False，响应槽设置
        label4.setText("<a href = 'https://item.jd.com/12417265.html'>\
        感谢关注 《Python从菜鸟到高手》</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超链接")

        # VBox：垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel控件演示")

    def linkHovered(self):
        print("当鼠标滑过Label2标签时，触发事件。")
    
    def linkClicked(self):
        print("当鼠标单击Label4标签时，触发事件。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())