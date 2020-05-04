# *layout*：布局

0. [绝对布局](../00-AbsoluteLayoutDemo.py)：通过坐标（x,y)来控制控件的位置。用*move(x,y)*来设置位置。

1. [水平盒布局](../01-HBoxLayoutDemo.py)

2. [控件对齐方式（以水平盒布局为例）](../02-HBoxLayoutAlignDemo.py)：*addWidget(self, 控件名, 拉伸（所占空间）（可以理解为此控件与下一控件距离相较于其他距离的比例）（int） , 对齐方式（Qt.alignment）)*

3. [垂直盒布局](../03-VBoxLayoutDemo.py)

4. [设置伸缩量](../04-StretchDemo.py)：除*2*所述方法外，还可以用*addStretch*方法。

5. [让按钮固定在窗口左下角](../05-RightButtomButtonDemo.py)：如确定取消按钮。实现方法：组成水平布局