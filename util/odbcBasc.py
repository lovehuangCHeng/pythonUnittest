import pymssql
import configparser
class odbc():
    def __init__(self):
        self.server=self.readDataSql("server")
        self.user=self.readDataSql("user")
        self.password=self.readDataSql("password")
        self.database=self.readDataSql("database")
    #读取数据配置文件。
    def readDataSql(self, key):
        conf = configparser.ConfigParser()
        conf.read("../config/dataconfig/sqlconfig.ini", encoding="utf-8-sig")
        # conf.read("D:/GitHub/pythonUnittest-master/config/testData.ini", encoding="utf-8-sig")
        value = conf.get("sql", key)
        return value

    def connect(self):
         self.cnxn = pymssql.connect(self.server, self.user, self.password, self.database)
         self.cursor=self.cnxn.cursor() # 获取光标
    def selectData(self,sql):
        '''
        查询数
        'select Name from OrganizationItem where Discriminator=%s','管理区'
        :param sql:
        '''
        print(self.redsqlconfig(sql))
        self.cursor.execute(self.redsqlconfig(sql))
        row = self.cursor.fetchall()
        return row

    def InsertData(self,sql):
        print(self.redsqlconfig(sql))
        self.cursor.execute(self.redsqlconfig(sql))
        # 如果没有指定autocommit属性为True的话就需要调用commit()方法
        self.cnxn.commit()
    #执行存储过程的，目前只支持一个变量。
    def execPROC(self,str):
        self.cursor.execute(f"EXEC USP_demo @saas_id='%s'"%(str))
        self.cnxn.commit()
    # 删除操作
    def DeleteData(self,sql):
        self.cursor.execute(self.redsqlconfig(sql))

    # 修改操作
    def UpdateData(self,sql):
        print(self.redsqlconfig(sql))
        self.cursor.execute(self.redsqlconfig(sql))
        self.cnxn.commit()

    def close(self):
        '''
        关闭数据库连接
        '''
        self.cursor.close()
        self.cnxn.close()

    '''
         读取数据库执行脚本
    '''
    def redsqlconfig(self, key):
        conf = configparser.ConfigParser()
        conf.read("../config/dataconfig/sql.ini", encoding="utf-8-sig")
        value = conf.get("SQL", key)
        return value
    def writeConfig(self):
        conf = configparser.ConfigParser()
        conf.set("group_b", "b_key3", "new3")  # 指定section和option则更新value
        conf.set("group_b", "b_key5", "value5")  # 指定section，则增加option和value
        # 写回配置文件
        conf.write(open("sql.ini", "wb"))
#redconfig =odbc()
