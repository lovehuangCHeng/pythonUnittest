#coding=utf-8
from page import BaseDriver
from time import  sleep
class BascinfoPage(BaseDriver.BascPage):
     def __init__(self,driver):
          super(BascinfoPage,self).__init__(driver)
     '''
     #点击div确认按钮,断言div弹窗是否正确
     '''
     def assetdiv(self,strass):
          try :
               assert strass in self.get_divshotinput()
               sleep(2)
               self.click_divshotbtn()
               sleep(2)
          except :
               assert strass in self.get_divlonginput()
               sleep(2)
               self.click_divlongbtn()
               sleep(2)
     '''
     通过模糊搜索，搜索数据的通用方法
     '''
     def selectdata(self,data):
          self.sendkey_select(data)
          sleep(1)
          self.click_sele()
          sleep(1)
     '''
     获取输入框类型，为下拉框的下拉列表中的值
     '''
     def get_click_elements(self,num):
          datalist = []
          datalist = self.driver.find_elements_by_class_name("select2-results__option")
          datalist[num].click()
     '''
     选择客户的方法
     selectCustomerbtn
     //*[@id='HouseId_HouseGrid']/div[2]/table/tbody/tr["+num+"]/td[6]
     '''
     def selectCustomer(self,num):
          self.click("selectCustomerbtn")
          sleep(1)
          str="//*[@id='CustomerId_CustomerGrid']/div[2]/table/tbody/tr[%d]/td[3]" %num
          self.driver.find_element_by_xpath(str).click()
          sleep(1)
          self.click("btnCustomerId")
     '''
     选择房间的方法
     '''
     def selectHouse(self,num):
          self.click("selectHousebtn")
          str="//*[@id='HouseId_HouseGrid']/div[2]/table/tbody/tr[%d]/td[6]" %num
          self.driver.find_element_by_xpath(str).click()
          self.click("btnconfirem")
     '''
     时间操作按钮
     '''
     def click_time(self):
         self.click("clicktime")
         sleep(2)
         element="k-footer"
         self.find_element(element).click()

     #获取新建按钮
     def click_newAdd(self):
          self.click("newbuild")

     #定位管理区，并根据管理区名称，选择管理区
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
     房产档案页面定位信息
     '''
     #改变业主 按钮
     def click_chagecustom(self):
          self.click("changeyezhu")

     #更改业主历史记录 按钮
     def click_changehistroy(self):
          self.click("changehistory")

     #更改状态  按钮
     def click_status(self):
          self.click("changhousestatu")

     #批量生成 按钮
     def click_piliang(self):
          self.click("piliang")

     #导出Excel 按钮
     def get_daoExcel(self):
          element=self.get_element("btnExport").text
          return  element

     #房产档案新建页面，获取楼层输入框
     def send_floor(self,number):
          self.sendkeys("housefloor",number)

     # 房产档案新建页面，获取房间序号输入框
     def send_housexuhao(self,value):
          self.sendkeys("housexuhao",value)

     # 房产档案新建页面，获取房间编号输入框
     def send_houseCode(self,number):
          self.sendkeys("houseCode",number)

     # 房产档案新建页面，获取房间面积输入框
     def send_houseArea(self,area):
          self.sendkeys("houseArea",area)

     # 房产档案新建页面，获取   楼宇
     def click_louyu(self,num):
          self.click("houseLou")
          self.get_click_elements(num)

     # 房产档案新建页面，获取   房间类型
     def click_typehouse(self,num):
          self.click("houseType")
          self.get_click_elements(num)

     #改变业主页面。迁入业主CheckBox
     def clic_moveNewCustomer(self):
          self.click("moveNewCustomer")

     #改变业主页面的【确认】按钮
     def click_btnOkWindow(self):
          self.click("btnOkWindow")

     #改变房间状态的方法
     def select_chagestatus(self,status):
          self.selector("changstatus",status)

     #改变房间状态页面【确认】按钮
     def click_status_comfire(self):
          self.click("ChangeStatusokbut")
     #批量页面取消按钮
     def click_quxioa_pili(self):
         self.click("quxioa_pili")
     '''
     房产状态统计页面，定位信息
     '''
     #房产状态统计按钮
     def click_housetongji(self):
         self.click("housetongji")
     '''
     客户管理
     '''

     #客户档案新建页面，客户类别  现在默认为：个人  暂不填写
     #客户档案新建页面，管理区  sendkey_guanliqu（value）
     #客户档案新建页面，客户名称
     def send_customer_name(self,name):
         self.sendkeys("louyuname",name)
     #客户档案 ， 合并重名客户 按钮
     def click_renameCustomerMerge(self):
         self.click("renameCustomerMerge")
     #交房登页面
     def click_SaveAndBack(self):
         self.click("SaveAndBack")
     #改变交房日期
     def click_chenagedate(self):
         self.click("chagejiaofang")
     #接房登记页面。确认按钮
     def click_jiefang_save(self):
         self.click("PaymentPreview")
     #接房登记新建界面弹窗
     def get_jiefangdivbox(self):
         element=self.find_element("bootbox-body").text
         return element
     #接房登记，查看按钮
     def click_chakan(self):
         self.click("btnLook")
     #接房登记，查看页面，返回按钮
     def click_back(self):
         self.click("fanghui")

     '''
     车库管理
     '''
     #车库档案页面，新建按钮
     def click_btnnew(self):
         self.click("newadd")
     #车库档案新建页面，车库名称
     def send_carcagename(self,Garagename):
         self.sendkeys("CarbarnName",Garagename)
     #选择车库按钮
     def click_carGaragen(self):
         self.click("carkuname")
         sleep(2)
         self.get_click_elements(0)
     #输入车位号
     def send_carnumber(self,carnumber):
         self.sendkeys("carnum",carnumber)
     #车位档案页面，绑定业主按钮
     def click_BindcarCustomer(self):
         self.click("BindcarCustomer")







