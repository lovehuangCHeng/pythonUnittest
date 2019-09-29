#coding=utf-8
from page import BaseDriver
from time import  sleep
class BascinfoPage(BaseDriver.BascPage):
     def __init__(self,driver):
          super(BascinfoPage,self).__init__(driver)
     #获取物业资源树搜索框
     def sendkeys_wuyetree(self,guanliqu):
          self.sendkeys('物业资源搜索框',guanliqu)
     #获取物业资源搜索按钮
     def click_wuyeserch(self):
          self.click("物业资源搜索")
     #获取物业资源树上搜索的管理区
     def click_guanliqutree(self):
          self.click("资源树管理区")
     #点击添加下级
     def click_xiajijigou(self):
          self.click("添加下级")
     #点击取消删除
     def click_quxiaodelete(self):
          self.click("取消删除")
     #点击确认删除
     def click_querendelete(self):
          self.click("确认删除")
     #点击导出Excel
     def click_expotExcle(self):
          self.click("导出Excel")
     #搜索框输入数据
     def sendkeys_serch(self,value):
          self.sendkeys("搜索框",value)










