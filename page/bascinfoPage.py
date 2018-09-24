#coding=utf-8
from page import BaseDriver
from time import  sleep
class BascinfoPage(BaseDriver.BascPage):
     def __init__(self,driver):
          super(BascinfoPage,self).__init__(driver)
     #点击div确认按钮,断言div弹窗是否正确
     def assetdiv(self,strass):
          try :
               assert strass in  self.get_divshotinput()
               sleep(2)
               self.click_divshotbtn()
               sleep(2)
          except :
               assert strass in self.get_divlonginput()
               sleep(2)
               self.get_divlonginput()
               sleep(2)
     def selectdata(self,data):
          self.sendkey_select(data)
          sleep(1)
          self.click_sele()
          sleep(1)
     #获取新建按钮
     def click_newAdd(self):
          self.click("newbuild")
     #定位管理区，并选着管理区
     def sendkey_guanliqu(self,text):
          self.selector("selectguanliqu",text)
     #楼宇名称
     def sendkey_louyuname(self,louyuname):
          self.sendkeys("louyuname",louyuname)
     #楼宇序号
     def sendkey_louyunum(self,louyucode):
          self.sendkeys("louyucode",louyucode)
     #楼宇档案界面，确定按钮
     def click_save(self):
          self.click("savebutton")
     #楼宇档案界面，取消按钮
     def click_cancel(self):
          self.click("quxiaobutton")
     #编辑按钮
     def click_edit(self):
          self.click("editbutton")
     #删除按钮
     def click_delete(self):
          self.click("delbutton")
     #确认删除按钮
     def click_confirmdel(self):
          self.click("confirmdelbutton")
     #搜索输入框
     def sendkey_select(self,selectvalue):
          self.sendkeys("selinputbox",selectvalue)
     #搜索按钮
     def click_sele(self):
          self.click("selbutton")
     #高级搜索按钮
     def click_seldevelop(self):
          self.click("detiselbutton")
     #重置按钮
     def click_rest(self):
          self.click("restbutton")
     #高级搜索按钮向下按钮
     def click_down(self):
          self.click("fadownbutton")
     #高级搜索按钮向上按钮
     def click_up(self):
          self.click("faupbutton")
     #div弹窗确认按钮 较短的
     def click_divshotbtn(self):
          self.click("divconfirmshot")
     # div弹窗确认按钮 较短的输入框的值
     def get_divshotinput(self):
          element=self.get_element("divinputbox").text
          return element
     # div弹窗确认按钮 较长的
     def click_divlongbtn(self):
          self.click("divconfirlong")
     # div弹窗确认按钮 较长的输入框
     def get_divlonginput(self):
          element = self.get_element("divinputboxlong").text
          return element
     '''
     导出Excel按钮
     '''


