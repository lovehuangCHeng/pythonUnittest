#coding=utf-8
from page import bascinfoPage,szguPage
from time import sleep

class louyu(bascinfoPage.BascinfoPage):
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
     楼宇管理新建楼宇方法
     '''
     def newloyu(self,guanliqu,louyuname,louyucode):
          sleep(2)
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
          sleep(2)
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
          self.click_seldevelop()
          sleep(2)
          self.click_up()
          sleep(2)
          self.assertTure(key,guanliqu)
     '''
     删除新建的数据,通用的方法
     '''
     def del_newData(self,data,checkbox):
          self.selectdata(data)
          sleep(2)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_delete()
          sleep(2)
          self.click_confirmdel()
          sleep(2)
          self.assetdiv("删除成功")

     '''
         房产档案新建数据的方法
     '''
     def newfangchan(self,guanliqu,num,area,code,xuhao):
          sleep(2)
          self.click_newAdd()
          sleep(2)
          self.sendkey_guanliqu(guanliqu)
          sleep(2)
          self.send_floor(num)
          sleep(2)
          self.send_houseArea(area)
          sleep(2)
          self.send_houseCode(code)
          sleep(2)
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
          sleep(2)
          self.find_element(ckeckbox).click()
          sleep(2)
          self.click_edit()
          sleep(2)
          self.click_save()
          sleep(2)
          self.assetdiv("成功")
     '''
     房产档案页面改变业主的方法
     '''
     def changeCustomer(self,checkbox,num):
          sleep(2)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_chagecustom()
          sleep(3)
          self.clic_moveNewCustomer()
          sleep(2)
          self.selectCustomer(num)
          sleep(2)
          self.click_btnOkWindow()
          sleep(2)
          self.assetdiv("修改房间业主成功")

     '''
     房产档案页面改变业主历史记录的方法
     '''
     def changeHistory(self,checkbox,close):
          sleep(2)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_changehistroy()
          sleep(2)
          self.find_element(close).click()
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
          self.click_quxioa_pili()
          sleep(2)
          assert message in self.get_daoExcel()
     '''
     房产统计页面进入的方法
     '''
     def housesummry(self):
          mesage="导出EXCEL"
          sleep(2)
          self.switch_fram("iframe")
          sleep(2)
          assert  mesage in self.get_daoExcel()
     '''
     客户管理
     '''
     #新建客户档案
     def newcustomer(self,guanliqu,name):
          sleep(2)
          self.click_newAdd()
          sleep(2)
          self.sendkey_guanliqu(guanliqu)
          sleep(2)
          self.send_customer_name(name)
          sleep(2)
          self.click_save()
          sleep(2)
          self.assetdiv("创建客户成功")
     #编辑客户档案
     def editcustomer(self,checkbox):
          self.editfangchan(checkbox)
     #合并重名客户的方法
     def renameMerge(self,messagekey,close):
          sleep(2)
          self.click_renameCustomerMerge()
          sleep(3)
          message="合并同名客户"
          assert message in self.find_element(messagekey).text
          sleep(2)
          self.find_element(close).click()
          sleep(2)
          assert "导出EXCEL" in self.get_daoExcel()
     '''
     交房登记，新建交房登记
     '''
     def jiaofangdengji(self):
          sleep(2)
          self.click_newAdd()
          sleep(2)
          self.selectHouse(2)
          sleep(2)
          self.selectCustomer(3)
          sleep(2)
          self.click_SaveAndBack()
          sleep(2)
          self.assetdiv("交房登记成功")
     '''
     更改交房日期
     '''
     def changjiaofang(self,checkbox):
          sleep(2)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_chenagedate()
          sleep(2)
          self.click_btnOkWindow()
          sleep(2)
          self.assetdiv("修改房间交房时间成功")
     '''
     新建接房登记数据
     '''
     def jiefangdengji(self,number):
          sleep(2)
          self.click_newAdd()
          sleep(2)
          self.selectHouse(number)
          sleep(2)
          self.click_jiefang_save()
          sleep(2)
          assert "接房成功" in self.get_jiefangdivbox()
          sleep(2)
          self.driver.find_element_by_css_selector(".modal-content > div:nth-child(2) > button:nth-child(1)").click()
          sleep(2)
     #接房登记，编辑
     def jiefang_edit(self,checkbox):
          sleep(2)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_edit()
          sleep(2)
          self.click_time()
          sleep(2)
          self.click_save()
          sleep(2)
          self.assetdiv("修改接房记录房成功")
     '''
     查看接房登记，查看方法
     '''
     def chakan(self,checkbox):
          sleep(2)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_chakan()
          sleep(2)
          self.click_back()
          sleep(2)
     '''
     入住登记，编辑  assert 更新入住登记成功
     '''
     def ruzhu_edit(self,checkbox):
          self.editfangchan(checkbox)
     '''
     新建车库档案
     '''
     def newGarage(self,Garagename,guanliqu):
          sleep(2)
          self.click_btnnew()
          sleep(2)
          self.send_carcagename(Garagename)
          sleep(2)
          self.sendkey_guanliqu(guanliqu)
          sleep(2)
          self.click_save()
          self.assetdiv("新建车库成功")
     #编辑车库数据
     def editGaragen(self,checkbox):
          sleep(2)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_edit()
          sleep(2)
          self.click_save()
          sleep(2)
          self.assetdiv("成功")
     #新建车位档案
     def newcarparking(self,guanliqu,carnumber):
          sleep(2)
          self.click_btnnew()
          sleep(2)
          self.sendkey_guanliqu(guanliqu)
          sleep(2)
          self.click_carGaragen()
          sleep(2)
          self.send_carnumber(carnumber)
          sleep(2)
          self.click_save()
          sleep(2)
          self.assetdiv("创建车位成功")
     #绑定车位业主
     def BindcarCustomer(self,checkbox):
          sleep(2)
          self.find_element(checkbox).click()
          sleep(2)
          self.click_BindcarCustomer()
          sleep(2)
          self.selectCustomer(5)
          sleep(2)
          self.click_btnOkWindow()
          sleep(2)
          self.assetdiv("绑定业主成功")


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
          self.find_element(checkbox).click()
          sleep(2)
          self.click_editszkm()
          sleep(2)
          self.find_element(checkbox1).click()
          sleep(2)
          assert message in self.get_message()

















