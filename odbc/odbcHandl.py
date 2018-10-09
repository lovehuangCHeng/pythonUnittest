import odbc.odbcBasc
class SqlData(odbc.odbcBasc.odbc):
    def guanliqu(self,sqlkey,num):
        '''
        根据查询的结果获取元素，取第几个元素就输入几
        :param num:
        :param sql: 配置文件中的key值
        :return:
        '''
        df = odbc.odbcBasc.odbc()
        conn_info=df.redconfig('conn_info')
        guanliqusql = df.redconfig(sqlkey)
        self.connect(conn_info)
        tt=self.select(guanliqusql,num-1)
        self.close()
        return tt







