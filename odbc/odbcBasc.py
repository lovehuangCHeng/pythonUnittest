import  pyodbc
import configparser
class odbc():
    def connect(self,conn_info):
        self.cnxn = pyodbc.connect(conn_info)
        self.cursor=self.cnxn.cursor()
    def select(self,sql,num):
        '''
        查询数据
        select Name from OrganizationItem where Discriminator='管理区'
        :param sql:
        :return:
        '''
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        print(row[num].Name)
        return row[num].Name

    def close(self):
        self.cursor.close()
        self.cnxn.close()

    def redconfig(self,key):
        conf = configparser.ConfigParser()
        conf.read("sql.ini",encoding="utf-8-sig")
        value = conf.get("SQL", key)
        return value

    def writeConfig(self):
        conf = configparser.ConfigParser()
        conf.set("group_b", "b_key3", "new3")  # 指定section和option则更新value
        conf.set("group_b", "b_key5", "value5")  # 指定section，则增加option和value
        # 写回配置文件
        conf.write(open("sql.ini", "wb"))
