from schedClass import MySchedClass
from EmailClass import Email
import os
import time


class mySched(MySchedClass):
    def cmd(self):
        print("mysql备份程序运行中")
        try:
            os.system("mysqldump -u root --password=root jyghc >  D:/jyghc.sql")
            email = Email("254449149@qq.com", "ufmsdjuhkgdxbibh", "smtp.qq.com", 465, "litao080712320@163.com")
            msg = email.createSQLMsg(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"jyghc数据库备份数据成功", "254上的mysql数据库上的jyghc实例备份成功", "d:/jyghc.sql", "jyghc.sql")
            email.sent(msg)
            print(time.strftime('%Y-%m-%d %Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "备份成功,一天后重新备份。请勿关闭运行窗口。")
        except:
            email = Email("254449149@qq.com", "ufmsdjuhkgdxbibh", "smtp.qq.com", 465, "litao080712320@163.com")
            msg = email.createPlainMsg(time.strftime('%Y-%m-%d %Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"jyghc数据库备份失败", "254服务器jyghc数据库备份失败，请查询失败原因！")
            email.sent(msg)
            print(time.strftime('%Y-%m-%d %Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "备份失败，一天后重新备份。问题请联系研发人员！")

ms=mySched()
ms.start(14200)
