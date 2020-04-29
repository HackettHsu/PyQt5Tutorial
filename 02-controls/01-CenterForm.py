'''
窗口初始居中
PyQt5本身不带有居中的功能
需要自己计算窗口左边到屏幕左边的距离 = 窗口右边到屏幕右边的距离并设置
QDesktopWidget 含有获取屏幕尺寸的函数
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

class CenterForm(QMainWindow):
    def __init__(self):
        # 先调用父类
        super(CenterForm, self).__init__()

        # 设置主窗口标题
        self.setWindowTitle("让窗口居中")

        # 设置窗口尺寸
        self.resize(400, 300)

    def center(self):
        # 计算屏幕尺寸并获取居中坐标
        # 获取窗口坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2

        # 用move方法移动窗口
        self.move(newLeft, newTop)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()

    sys.exit(app.exec_())