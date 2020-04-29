# 纯代码方法实现退出程序功能
# 用到了QHBoxLayout
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle("退出应用程序")

        # 添加Button
        self.button1 = QPushButton("退出应用程序")
        # 自定义槽的绑定
        self.button1.clicked.connect(self.onClick_Button)
        # 放置这个按钮
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        # 为窗口设置主框架
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        # 把主框架放在窗口中间
        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        # 用sender获取发送信号的对象Button
        sender = self.sender()
        print(sender.text() + " 被按下按钮")
        # 用instance获取实例
        app = QApplication.instance()
        app.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())