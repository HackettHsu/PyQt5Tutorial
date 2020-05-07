# lesson 125 视频出错，放的重复视频，所以这里是我自己找的
# 需要pip手动安装qdarkstyle
# 这里的示例代码来自同名GitHub项目
import sys
import qdarkstyle
from PyQt5 import QtWidgets

# create the application and the main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

# setup stylesheet
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
# or in new API
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

# run
window.show()
app.exec_()