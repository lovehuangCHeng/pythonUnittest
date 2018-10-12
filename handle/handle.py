#coding=utf-8
from page import bascinfoPage,szguPage
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
     高级搜索，查找管理区是否正确,通用方法
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
     删除新建的数据,通用的方法
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
     def newfangchan(self,guanliqu,num,area,code,xuhao):
          sleep(1)
          self.click_newAdd()
          sleep(1)
          self.sendkey_guanliqu(guanliqu)
          sleep(2)
          self.send_floor(num)
          sleep(2)
          self.send_houseArea(area)
          sleep(2)
          self.send_houseCode(code)
          sleep(1)
          self.send_housexuhao(xuhao)
          sleep(2)
          self.click_louyu(1)
          sleep(2)
          self.click_typehouse(1)
          sleep(2)
          self.click_save()
          sleep(2)
          self.assetdiv("创建房间成功")

     '''
            房产档案编辑数据的方法
     '''
     def editfangchan(self,ckeckbox):
          sleep(1)
          self.find_element(ckeckbox).click()
          sleep(1)
          self.click_edit()
          sleep(1)
          self.click_save()
          sleep(2)
          self.assetdiv("更新房间成功")
     '''
     房产档案页面改变业主的方法
     '''
     def changeCustomer(self,checkbox,num):
          sleep(1)
          self.find_element(checkbox).click()
          sleep(1)
          self.click_chagecustom()
          sleep(1)
          self.clic_moveNewCustomer()
          sleep(1)
          self.selectCustomer(num)
          sleep(1)
          self.click_btnOkWindow()
          sleep(2)
          self.assetdiv("修改房间业主成功")

     '''
     房产档案页面改变业主历史记录的方法
     '''
     def changeHistory(self,checkbox,close):
          sleep(1)
          self.find_element(checkbox).click()
          sleep(1)
          self.click_changehistroy()
          sleep(2)
          self.find_element(close)
     '''
     房产档案页面改变房间状态的方法
     '''
     def changeStatus(self,checkbox,status):
          sleep(2)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_status()
          sleep(2)
          self.select_chagestatus(status)
          sleep(2)
          self.click_status_comfire()
          sleep(2)
          self.assetdiv("修改房间状态成功")
     '''
     房产档案界面批量生成的方法
     '''
     def piliangshengcheng(self,message):
          sleep(2)
          self.click_piliang()
          sleep(2)
          self.click_piliang()
          assert message in self.get_daoExcel()


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
          sleep(1)
          self.send_szkmselectinput(value)
          sleep(1)
          self.click_szkmselectbnt()
          sleep(1)
     #删除新建的收支科目
     def delnewbulid(self,value,message):
          self.selectSZKM(value)
          sleep(1)
          self.click_delszkm()
          sleep(1)
          self.click_delcofnszkm()
          sleep(1)
          assert message in self.get_message()
     #编辑收支科目
     def editszkm(self,checkbox,value,message,checkbox1):
          self.selectSZKM(value)
          sleep(1)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_editszkm()
          sleep(2)
          self.find_element(checkbox1).click()
          sleep(2)
          assert message in self.get_message()

















