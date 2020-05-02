# lesson 55 2020年5月2日 12:19:24-13:04:55
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ClipBoardDemo(QDialog):
    def __init__(self):
        super(ClipBoardDemo, self).__init__()
        self.setWindowTitle("ClipBoardDemo")
        textCopyButton = QPushButton("复制文本")
        textPasteButton = QPushButton("粘贴文本")
        copyHtmlButto = QPushButton("复制HTML")
        pasteHtmlButton = QPushButton("粘贴HTML")
        copyImageButton = QPushButton("复制图像")
        pasteImageButton = QPushButton("粘贴图像")
        self.textLabel = QLabel("默认文本")
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap(QFileInfo(__file__).absolutePath() + \
            "./images/罗小黑战记 电影原声带.bmp"))
        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(copyHtmlButto, 0, 1)
        layout.addWidget(copyImageButton, 0, 2)
        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(pasteHtmlButton, 1, 1)
        layout.addWidget(pasteImageButton, 1, 2)
        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)
        self.setLayout(layout)
        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        copyHtmlButto.clicked.connect(self.copyHtml)
        pasteHtmlButton.clicked.connect(self.pasteHtml)
        copyImageButton.clicked.connect(self.copyImage)
        pasteImageButton.clicked.connect(self.pasteImage)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("Hello world")
    
    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    # HTML部分没有成功实现，有问题，然而视频课没有测试
    def copyHtml(self):
        # 先创建一个HTML格式的数据
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color = blue>Blue</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap(QFileInfo(__file__).absolutePath() + "./images/罗小黑战记 电影原声带.bmp"))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ClipBoardDemo()
    main.show()
    sys.exit(app.exec_())