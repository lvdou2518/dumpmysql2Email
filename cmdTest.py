import os

# 系统运行cmd命令
# os.system("mysqldump -h localhost -P 3306 -u root -p root jyghc > d:/jyghc.sql")
os.system("mysqldump -u root --password=root jyghc >  D:/jyghc.sql")