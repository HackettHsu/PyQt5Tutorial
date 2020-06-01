# 最后的内容（杂项内容）

0. 使用Pyinstaller打包PyQt5应用：

    0. 使用pip安装

    1. 基本使用方法及命令解释：

        0. 基本使用：`pyinstaller XXX.py`，产生的产品要先出现终端再打开窗口；

        1. `pyinstaller -Fw XXX.py`： *-w* 不显示终端(?)；*-Fw*将所有的库打包成一个文件。

[操作SQLite数据库](00-MyDBDemo.py)：使用*QtSql*模块。但受到PyQt5版本影响，新版本可能不自带该模块需要另行安装（像*QtWebEngine*模块一样）。处理方法：
1. 安装旧版PyQt5`pip install pyqt5==5.10.1`
2. 单独安装缺少的模块：
   1. `pip install PyQtWebEngine`和`pip install PyQtSql`
   2. 适用于Linux的：`apt install python3-pyqt5.qtwebengine python3-pyqt5.qtsql`。

[使用可视化的方式对SQLite数据库进行增、删、改、查操作](01-DataGridDemo.py)

[分页显示数据](02-DataGrid2Demo.py)：视频课内容过多，从网上下载已经写好的代码。

[使用PyQtGraph进行数据可视化](03-GraphDemo.py)：也是下载的代码。另外，PyQtGraph是第三方模块，需要另行下载。下载的代码还使用numpy模块产生了一些正态分布等统计学数据。这两个模块Kali自带。还有，下载的代码是先使用Designer绘制UI再添加相关内容的方法制作的。