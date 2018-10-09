#coding=utf-8
import configparser
import odbc.odbcHandl
from selenium import  webdriver
class BaseCase(object):
     def getDriver(self):
          '''
          获取webdriver
          :return:
          '''
          driver = webdriver.Chrome()
          return driver
     '''
     读取填写的数据文件
     '''
     def readData(self,key):
          conf = configparser.ConfigParser()
          conf.read("../config/testData.ini",encoding="utf-8-sig")
          value=conf.get("DATA",key)
          return value
     '''
     读取url文件
     '''
     def readUrl(self,key):
          conf = configparser.ConfigParser()
          conf.read("../config/url.ini",encoding="utf-8-sig")
          url = conf.get("TESTURL", key)
          return  url

     def reddatasql(self,sqlkey,num):
          '''
          读取数据库中的数据
          :param sqlkey:
          :param num:
          :return:
          '''
          od=odbc.odbcHandl.SqlData()
          val=od.guanliqu(sqlkey,num)
          return val

