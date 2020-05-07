# lesson 131 17:08:06-17:16:28
import sys, os
from PyQt5.QtWidgets import *

os.chdir(sys.path[0])
class LabelButtonBackgroundDemo(QWidget):
    def __init__(self):
        super(LabelButtonBackgroundDemo, self).__init__()
        self.setWindowTitle("LabelButtonBackgroundDemo")
        self.resize(500, 500)
        label1 = QLabel()
        # 鼠标悬停时显示提示
        label1.setToolTip("This is a label.")
        label1.setStyleSheet("QLabel{border-image:url(./images/喵塔利亚.png)}")
        # 设置label1尺寸
        label1.setFixedWidth(300)
        label1.setFixedHeight(300)
        button1 = QPushButton(self)
        button1.setObjectName("Button1")
        button1.setMaximumSize(48, 48)
        button1.setMinimumSize(48, 48)
        # radius：圆角
        style = '''
            #Button1{border-radius:4px; background-image:url("./images/test.ico")}
            #Button1:Pressed{background-image:url("./images/罗小黑战记 电影原声带.bmp")}
        '''
        button1.setStyleSheet(style)
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(button1)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LabelButtonBackgroundDemo()
    main.show()
    sys.exit(app.exec_())