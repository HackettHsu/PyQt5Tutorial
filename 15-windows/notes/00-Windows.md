# 窗口、绘图和特效

0. [设置窗口风格](../00-WindowStyleDemo.py)：*QApplication.setStyle()*。设置窗口中控件的风格。

1. [设置窗口样式](../01-WindowPatternDemo.py)：*setWindowFlags(很多种样式，用 “|”实现多样式共存)*。主要是窗口边框、标题栏和窗口本身的特性。

2. [用代码设置窗口的最大化和最小化](../02-WindowMaxMinDemo.py)

3. [项目实战：实现绘图应用](../03-DrawingDemo.py)：

    需要解决三个核心内容：

    1. 如何绘图：通过调用*update()*方法触发*paintEvent*在*paintEvent*方法中绘图。

    2. 在哪里绘图：在*QPixmap*中绘图，并可以提前用*fill()*填充画布背景色。

    3. 如何通过移动鼠标实现绘图：记录鼠标按下、移动和抬起三个事件。

4. [QSS基础](../04-BasicQSSDemo.py)：*QSS：Qt Style Sheets*，Qt样式表，用于设置控件风格、样式，类似CSS。

5. [使用QSS选择器设置控件样式](../05-QSSSelectorDemo.py)：比如只设置个别控件样式。

6. [QSS子控件选择器](../06-QSSSubControlDemo.py)：有些控件是多个其他控件组合起来的，子控件能单独之控制一部分。

7. [QDarkStyle样式](../07-QDardStyleDemo.py)

8. 三种方式设置背景色和背景图：视频出错，自己找的。

    1. 使用QSS：[背景色](../08-BackgroundColorDemo1.py)；[背景图](../08-BackgroundImageDemo1.py)，这里图片是拉伸覆盖。

    2. 使用QPalteet（调色板）[背景色](../08-BackgroundColorDemo2.py)；[背景图](../08-BackgroundImageDemo2.py)，从坐标原点开始平铺并重复覆盖。

    3. 使用paintEvent：[背景色](../08-BackgroundColorDemo3.py)；[背景图](../08-BackgroundImageDemo3.py),拉伸覆盖。

9. [实现不规则窗口（异形窗口）](../09-AbnormityWindowDemo.py)：方法之一。通过*mask*实现，需要一张透明的 *\.png*的图，抠出空白后即可形成异形。

10. 移动和关闭不规则窗口：上一课程都出错了，直接跳过。

11. 不规则窗体动画实现：跳过

12. [装载Gif动画文件](../12-gifFileDemo.py)：使用*QMovie*。

13. [使用QSS为标签和按钮添加背景图](../13-LabelButtonBackgroundDemo.py)：可以以此类推到其他控件上。

14. [缩放图片](../14-ScaleImageDemo.py)：*QImage.Scaled*

15. [创建透明和半透明窗口](../15-OpacityWindowDemo.py)：*setWindowOpacity()* [0, 1]。1表示不透明。

16. [装载QSS文件](../16-LoadQSSFIleDemo.py)

17. [用动画效果改变窗口尺寸](../17-AnimWindowDemo.py)