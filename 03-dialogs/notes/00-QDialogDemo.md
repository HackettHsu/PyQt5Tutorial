## *QDialog*：[对话框](../00-QDialogDemo.py)

没有菜单栏的窗口。（与*QWidget*、*QMainWindow*平级）

*setWindowModality(Qt.ApplicationMode)*：设置对话框模式为应用模式（在对话框关闭之前，主窗口所有控件都不可用）

*exec()*：显示对话框

五类子类对话框

1. *QMessageBox*：[显示消息](../01-QMessageBoxDemo.py)


    类型：

    1. 关于对话框

    2. 错误对话框

    3. 警告对话框

    4. 提问对话框

    5. 消息对话框

    差异：

    1. 弹出对话框的图标不同

    2. 对话框显示按钮不同

2. *QColorDialog*：显示颜色

3. *QFileDialog*：显示文件保存状况

4. *QFontDialog*：设置字体

5. *QInputDialog*：获取用户输入
