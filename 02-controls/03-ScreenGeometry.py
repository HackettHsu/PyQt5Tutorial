'''
屏幕坐标系
PyQt5在进行界面设计时默认存在X-Y坐标系，以（屏幕和程序）左上角为零点
工作区：程序中不包括标题栏的区域
到底哪些含有标题栏？
'''
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget

# 单击按钮输出坐标信息
def onClick_Button():
    print("Method 1:")
    print(f"widget.x() = {widget.x()}")# 窗口坐标。含标题栏
    print(f"widget.y() = {widget.y()}") 
    print(f"widget.width() = {widget.width()}")# 工作区坐标。不含标题栏
    print(f"widget.height() = {widget.height()}")

    print("Method 2:")
    print(f"widget.geometry().x() = {widget.geometry().x()}")# 工作区坐标。不含标题栏
    print(f"widget.geometry().y() = {widget.geometry().y()}")
    print(f"widget.geometry().width() = {widget.geometry().width()}")
    print(f"widget.geometry().height() = {widget.geometry().height()}")

    print("Method 3:")
    print(f"widget.frameGeometry().x() = {widget.frameGeometry().x()}")# 窗口坐标。含标题栏
    print(f"widget.frameGeometry().y() = {widget.frameGeometry().y()}")
    print(f"widget.frameGeometry().width() = {widget.frameGeometry().width()}")# 窗口坐标。含有标题栏
    print(f"widget.frameGeometry().height() = {widget.frameGeometry().height()}")

app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_Button)

btn.move(24, 52)

widget.resize(300, 240)# 设置工作区的高度

widget.move(250, 200)

widget.setWindowTitle("屏幕坐标")

widget.show()

sys.exit(app.exec_())