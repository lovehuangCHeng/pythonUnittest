#coding=utf-8
from page import wuyesorcesPage,szguPage
from time import sleep

class louyu(wuyesorcesPage.BascinfoPage):
     def __init__(self,driver):
          super(louyu,self).__init__(driver)
     '''
     重新加载url
     '''
     def switch_url(self,url):
          self.switch_default()
          sleep(2)
          self.get(url)
          sleep(2)
          self.switch_fram("iframe")
     '''
     物业资源管理，搜索当前的管理区，并查询这个管理区。
     '''
     def get_guanliqu(self,guanliqu):
          self.sendkeys_wuyetree(guanliqu)
          sleep(2)
          self.click_wuyeserch()
          sleep(2)
          self.click_guanliqutree()


class szgu(szguPage.SZGLpage):
     def __init__(self,driver):
          super(szgu,self).__init__(driver)
     def szgul(self):
          self.click_szgl()
          sleep(2)
          self.click_szku()
          sleep(2)
     #新建收支科目
     def szkunew(self,name,num,message):
          self.click_szkmnew()
          sleep(2)
          self.send_szkmname(name)
          sleep(2)
          self.click_szkmtype(num)
          sleep(2)
          self.click_szkmcomfire()
          sleep(2)
          assert message in self.get_message()
     #查询收支科目
     def selectSZKM(self,value):
          sleep(2)
          self.send_szkmselectinput(value)
          sleep(2)
          self.click_szkmselectbnt()
          sleep(2)
     #删除新建的收支科目
     def delnewbulid(self,value,message):
          self.selectSZKM(value)
          sleep(2)
          self.click_delszkm()
          sleep(2)
          self.click_delcofnszkm()
          sleep(2)
          assert message in self.get_message()
     #编辑收支科目
     def editszkm(self,checkbox,value,message,checkbox1):
          self.selectSZKM(value)
          sleep(2)
          self.get_element(checkbox).click()
          sleep(2)
          self.click_editszkm()
          sleep(2)
          self.get_element(checkbox1).click()
          sleep(2)
          assert message in self.get_message()

















