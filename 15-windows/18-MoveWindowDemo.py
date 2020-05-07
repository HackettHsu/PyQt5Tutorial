# lesson 136 21:11:47-21:21:53

import sys 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
window1 = QMainWindow()
window1.setWindowTitle("1")
window1.show()
window2 = QMainWindow()
window2.setWindowTitle("2")
window2.show()
animation1 = QPropertyAnimation(window1, b'geometry')
animation2 = QPropertyAnimation(window2, b'geometry')
# 创建一个并行的组(两个动画同时运行)
# 串行：QSequentialAnimationGroup
group = QParallelAnimationGroup()
group.addAnimation(animation1)
group.addAnimation(animation2)
animation1.setDuration(3000)
# QRect(零点x, 零点y, 长, 高)
animation1.setStartValue(QRect(0, 1000, 100, 300))
animation1.setEndValue(QRect(250, 250, 100, 30))
# 增加一个动画特效(QEasingCurve有很多不同动画特效的子类)
animation1.setEasingCurve(QEasingCurve.OutBounce)
animation2.setDuration
animation2.setStartValue(QRect(250, 150, 100, 30))
animation2.setEndValue(QRect(850, 250, 100, 30))
animation2.setEasingCurve(QEasingCurve.OutExpo)
group.start()
sys.exit(app.exec_())