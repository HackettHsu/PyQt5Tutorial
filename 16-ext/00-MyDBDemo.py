# lesson 138
import sys, os
# Query:操作数据库
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

os.chdir(sys.path[0])
def createDB():
    # 设置读取数据库类型
    db = QSqlDatabase.addDatabase('QSQLITE')
    # SQLite 是以文件为形式存储的，要指定文件名
    db.setDatabaseName('./db/database.db')
    if not db.open():
        print("Can't connect to database.")
        return False
    query = QSqlQuery()
    # 执行SQLite的相关语句
    query.exec('create table people(id int primary key, name varchar(10), address varchar(50))')
    query.exec("insert into people values(1, 'HackettHsu', 'Zhuzhou')")
    query.exec("insert into people values(2, 'Optimus Prime', 'Cybertron')")
    db.close()
    return True

if __name__ == "__main__":
    createDB()