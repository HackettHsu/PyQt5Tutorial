# PyQt5 Tutorial

这是我在学习*PyQt5*基本运用时的练习项目文件夹。

课程来源：从网易云课堂上传到B站的 [PyQt5教程](https://www.bilibili.com/video/BV154411n79)， 讲师：李宁

PyCharm相关、Python基本以及一些简单的知识不计入笔记，自行搜索查询。

详细笔记见项目中的Markdown笔记文件，以及程序代码中的注释。

注意：

1. *.pylintrc*文件：VsCode使用*pylint*进行Python语法判断，然而这个插件不能自动检索PyQt5（PyQt脱胎于用**C语言**编写的Qt，所以pylint支持不佳）。在项目根目录创建*.pylintrc*文件并录入`extension-pkg-whitelist=PyQt5`就能避免纠错功能不停关于PyQt模块的报错。但这样也屏蔽了其他的正常使用，所以当真正需要时去掉这个文件就行了。