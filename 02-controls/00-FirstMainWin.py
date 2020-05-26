import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFileInfo

class FirstMainWin(QMainWindow):
    # 为什么要QMainWindow？
    # 因为这个类是用于编写主窗口，所以需要从QMainWindow中继承相关配置
    def __init__(self):
        # 先调用父类
        # 其实就是自我调用
        super(FirstMainWin, self).__init__()

        # 设置主窗口标题
        self.setWindowTitle("第一个主窗口应用")

        # 设置窗口尺寸
        self.resize(400, 300)

        # 设置状态栏
        self.status = self.statusBar()
        
        self.status.showMessage("只存在5秒的信息", 5000)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 设置窗口图标。
    # Windows下有奇怪的问题，需要写绝对路径否则无效
    # 还不能使用os.getcwd()。为什么？
    # 因为os.getcwd()获得的是命令行所在位置而不是文件所在位置
    # 先获取当前py文件的绝对路径
    root = QFileInfo(__file__).absolutePath()
    # 再与QIcon函数组合
    app.setWindowIcon(QIcon(root + './images/test.ico'))
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())