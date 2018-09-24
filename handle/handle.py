#coding=utf-8
from page import bascinfoPage
from time import sleep
class louyu(bascinfoPage.BascinfoPage):
     def __init__(self,driver):
          super(louyu,self).__init__(driver)
     '''
     楼宇管理新建楼宇方法
     '''
     def newloyu(self,guanliqu,louyuname,louyucode):
          sleep(1)
          self.click_newAdd()
          sleep(2)
          self.sendkey_guanliqu(guanliqu)
          sleep(2)
          self.sendkey_louyuname(louyuname)
          sleep(2)
          self.sendkey_louyunum(louyucode)
          sleep(2)
          self.click_save()
          sleep(2)
          self.assetdiv("成功")
     '''
     通用编辑方法，点击编辑按钮，点击保存
     checkbox 定位
     checkbox=//*[@id="gridBuilding"]/div[2]/table/tbody/tr[1]/td[1]/div/span/input
     '''
     def edit(self,checkbox):
          sleep(1)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_edit()
          sleep(2)
          self.click_save()
          sleep(2)
          self.assetdiv("成功")
     '''
     搜索，按楼宇名称搜索
     楼宇名称定位
     louyuname=//*[@id="gridBuilding"]/div[2]/table/tbody/tr[1]/td[4]
     '''
     def select_inputbox(self,selectvalue,key):
          sleep(2)
          self.sendkey_select(selectvalue)
          sleep(2)
          self.click_sele()
          sleep(2)
          self.assertTure(key,selectvalue)
     '''
     高级搜索，查找管理区是否正确
     '''
     def select_develop(self,key,guanliqu):
          sleep(2)
          self.click_down()
          sleep(2)
          self.sendkey_guanliqu(guanliqu)
          sleep(2)
          self.click_up()
          sleep(2)
          self.assertTure(key,guanliqu)
     '''
     删除新建的数据
     '''
     def del_newData(self,data,checkbox):
          self.selectdata(data)
          sleep(1)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_delete()
          sleep(1)
          self.click_confirmdel()
          sleep(2)
          self.assetdiv("删除成功")

     '''
         房产档案新建数据的方法
     '''
     def newfangchan(self):
          pass
     '''
     房产档案页面改变业主的方法
     '''
     def changeCustomer(self):
          pass

     '''
     房产档案页面改变业主历史记录的方法
     '''
     def changeHistory(self):
          pass
     '''
     房产档案页面改变房间状态的方法
     '''
     def changeStatus(self):
          pass
     '''
     房产档案界面批量生成的方法
     '''
     def piliangshengcheng(self):
          pass







