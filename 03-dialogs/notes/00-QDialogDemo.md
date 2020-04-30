## [*QDialog*](../00-QDialogDemo.py)：对话框

没有菜单栏的窗口。（与*QWidget*、*QMainWindow*平级）

*setWindowModality(Qt.ApplicationMode)*：设置对话框模式为应用模式（在对话框关闭之前，主窗口所有控件都不可用）

*exec()*：显示对话框

五类子类对话框

1. [*QMessageBox*](../01-QMessageBoxDemo.py)：显示消息


    类型：*QMessageBox.type(self, MessageBoxName, MessageBoxTitle)*

    1. *QMessageBox.about()* 关于对话框

    2. *QMessageBox.critical()* 错误对话框

    3. *QMessageBox.warning()* 警告对话框

    4. *QMessageBox.question()* 提问对话框

    5. *QMessageBOx.information()* 消息对话框

    差异：

    1. 弹出对话框的图标不同

    2. 对话框显示按钮不同

2. [*QColorDialog*](../05-QColorDialogDemo.py)：显示颜色

3. [*QFileDialog*](../06-QFileDialogDemo.py)：文件控制

    分支非常多，最常用就是打开和保存文件。

    打开文件：

    1. *getOpenFileName(self, "窗口名称", "初始路径", "打开文件类型（\*.格式1 \*.格式2)")方法*：打开单个文件

        返回两个值 fname文件名, quit是否取消了 （ quit也可以用_来不接受返回值）

    2. *QFileDialog()方法*：直接使用了QFileDialog，具体及一些控制如下：

        ```python
        openFile = QFileDialog()
        # 显示所有文件
        openFile.setFileMode(QFileDialog.AnyFile)
        # 选择（过滤）文件
        openFile.setFilter(QDir.Files)
        ```

4. [*QFontDialog*](../04-QFontDialogDemo.py)：设置字体 显示字体列表和字号并设置

5. [*QInputDialog*](../02-QInputDialogDemo.py)：获取用户输入
