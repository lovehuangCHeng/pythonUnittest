import util.odbcBasc
class SqlData(util.odbcBasc.odbc):
    def selectSql(self,key,num):
        '''
        根据查询的结果获取元素，取第几个元素就输入几-1
        :param num:
        :param sql: 配置文件中的key值
        :return:
        '''
        self.connect()
        tt=self.select(key)
        self.close()
        return tt[num]

    def openmodels(self):
        '''
        需要在数据库中先执行存储过程，有这个名称后才能进行调用,
        参考confluence上：脚本需要用到的存储过程
        '''
        self.connect()
        self.execPROC('Nova.Pms.WeChat')
        self.close()






