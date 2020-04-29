import sys
import MainHorizontalLayout # 导入UI模块
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv) # 表示整个主程序
    mainWindow = QMainWindow() # 创建主窗口
    ui = MainHorizontalLayout.Ui_MainWindow()
    ui.setupUi(mainWindow) # 向主窗口上添加控件
    mainWindow.show()
    sys.exit(app.exec_()) # 进入主循环