# lesson 124 15:06:19-15:41:49
import sys, os
from PyQt5.QtWidgets import *

# 解决Windows环境下VsCode设置相对路径失败的方法
os.chdir(sys.path[0])
class QSSSubControlDemo(QWidget):
    def __init__(self):
        super(QSSSubControlDemo, self).__init__()
        self.setWindowTitle("QSSSubControlDemo")
        combo = QComboBox(self)
        combo.setObjectName("myComboBox")
        combo.addItems(["Windows", "Linux", "Mac OS X"])
        combo.move(50, 50)
        self.setGeometry(250, 200, 320, 150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QSSSubControlDemo()
    qssStyle = '''
        QComboBox#myComboBox::drop-down{
            image:url(images/dropdown.png)
        }
    '''
    main.setStyleSheet(qssStyle)
    main.show()
    sys.exit(app.exec_())