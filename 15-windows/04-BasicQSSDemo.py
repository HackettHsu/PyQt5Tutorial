# lesson 122 14:49:08-14:57:14
import sys 
from PyQt5.QtWidgets import *

class BasicQSSDemo(QWidget):
    def __init__(self):
        super(BasicQSSDemo, self).__init__()
        self.setWindowTitle("BasicQSSDemo")
        self.resize(500, 500)
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = BasicQSSDemo()
    # 设置QSS样式
    # 此方法可以成为选择器，所有是XXX的会设置为{XXX属性}
    qssStyle = 'QPushButton{ background-color : pink}'
    # 使QSS样式（在窗口全局）生效
    main.setStyleSheet(qssStyle)
    main.show()
    sys.exit(app.exec_())