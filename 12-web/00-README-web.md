# PyQt5和web的交互技术

同时使用Python和Web开发程序（混合开发）。

使用Python+JavaScript+HTML5+CSS。

由于WebUI的设计的自定义性极高，所以Web可以用来开发PyQt5底层的外观设计。

可能需要单独安装PyQtWebEngine模块

[用Web浏览器控件（QWebEngineView）显示网页](00-WebEngineViewDemo.py)：*QWebEngineView*:显示Web页面

[装载本地Web页面](01-LocalHTMLDemo.py)

[显示嵌入Web页面](02-InnerHTMLDemo.py)：将Web代码硬编码到Python文件中

[PyQt5调用JavaScript代码，并返回值](03-PyQt5CallJSDemo.py)：PyQt5（强行）与JavaScript交互（数据传输）(Python调用JavaScript中函数值等）。

[JavaScript调用PythonAPI计算阶乘](04-PyFactorialDemo.py)：将Python的一个对象映射到JavaScript中。将需要映射的值定义为槽函数（将槽函数映射到JavaScript中）。（js映射的对象来自[factorial](factorial.py)中）