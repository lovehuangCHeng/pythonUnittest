#coding=utf-8
import configparser
import util.odbcHandl
from selenium import  webdriver
class BaseCase(object):
     def getDriver(self):
          '''
          获取webdriver
          D:/GitHub/pythonUnittest-master
          '''
          driver = webdriver.Chrome()
          return driver
     '''
     读取数据配置文件。
     '''
     def readData(self,key):
          conf = configparser.ConfigParser()
          #conf.read("./config/testData.ini",encoding="utf-8-sig")
          conf.read("D:/GitHub/pythonUnittest-master/config/testData.ini", encoding="utf-8-sig")
          value=conf.get("DATA",key)
          return value
     '''
     读取url文件
     '''
     def readUrl(self,key):
          conf = configparser.ConfigParser()
          conf.read("D:/GitHub/pythonUnittest-master/config/url.ini",encoding="utf-8-sig")
          urlc = conf.get('TESTURL', key)
          urlbase = conf.get('TESTURL', 'basicurl')
          url = urlbase + urlc
          return  url

     def reddatasql(self,key,num):
          '''
          读取数据库中的数据,管理区
          :param num:
          '''
          od= util.odbcHandl.SqlData()
          val=od.selectSql(key,num)
          return val
#BaseCase=BaseCase()
# # print(BaseCase.reddatasql(0))
#print(BaseCase.readUrl('首页'))



