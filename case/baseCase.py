#coding=utf-8
import configparser
import os
from selenium import  webdriver
class BaseCase(object):
     def getDriver(self):
          chromedriver = "D:\python\python\chromedriver.exe"
          os.environ["webdriver.chrome.driver"] = chromedriver
          driver = webdriver.Chrome(chromedriver)
          return driver
     '''
     读取填写的数据文件
     '''
     def readData(self,key):
          conf = configparser.ConfigParser()
          conf.read("../dataconfig/testData.ini")
          value=conf.get("DATA",key)
          return value
     '''
     读取url文件
     '''
     def readUrl(self,key):
          conf = configparser.ConfigParser()
          conf.read("../dataconfig/url.ini")
          url = conf.get("ZIP", key)
          return  url

