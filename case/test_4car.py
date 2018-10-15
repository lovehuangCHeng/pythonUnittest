#coding=utf-8
import unittest
from handle import handle
from case import baseCase

class Test_BascinfoCase(baseCase.BaseCase,unittest.TestCase):
     bc = baseCase.BaseCase()
     driver = bc.getDriver()
     lp = handle.louyu(driver)
     #车库档案
     Garage_checkbox=bc.readData("Garage_checkbox")
     Garage_parkname=bc.readData("Garage_parkname")
     Garage_guanliqubox=bc.readData("Garage_guanliqubox")
     Garagename="滨湖世纪停车场"
     #车位档案
     park_checkbox=bc.readData("park_checkbox")
     park_Garagename=bc.readData("park_Garagename")
     park_guanliqubox=bc.readData("park_guanliqubox")
     park_numberbox=bc.readData("park_numberbox")
     carnumber="XCKU1568"
     guanliqu="滨湖新城"
     @classmethod
     def setUpClass(cls):
         url = cls.bc.readUrl("carkuURL")
         cls.lp.get(url)
         cls.lp.setCookie()
         cls.lp.get(url)
         cls.lp.switch_fram("iframe")
     #新建车库档案
     def test_11newGaragen(self):
         try:
             self.lp.del_newData(self.Garagename, self.Garage_checkbox)
         except:
             print("还未新建这个车库")
         self.lp.newGarage(self.Garagename,self.guanliqu)
     #编辑车位档案
     def test_12deitGaragen(self):
         self.lp.editGaragen(self.Garage_checkbox)
     #查询新建车库
     def test_13selnewGaragen(self):
         self.lp.select_inputbox(self.Garagename,self.Garage_parkname)
     #查询管理区
     def test_14seldevelop(self):
         self.lp.select_develop(self.Garage_guanliqubox,self.guanliqu)
     #删除新建车位数据
     def test_15delnewGaragen(self):
         self.lp.del_newData(self.Garagename,self.Garage_checkbox)
     '''
     切换地址到车位档案页面
     '''
     def test_16switchcarparking(self):
         url=self.bc.readUrl("carweiURL")
         self.lp.switch_url(url)
     #新建车位档案数据
     def test_17newcarparking(self):
         try:
             self.lp.del_newData(self.carnumber, self.park_checkbox)
         except :
             print("没有这个车位存在")
         self.lp.newcarparking(self.guanliqu,self.carnumber)
     #编辑车位数据
     def test_18editcarparking(self):
         self.lp.editGaragen(self.park_checkbox)
     #车位绑定业主
     def test_19bandcustomer(self):
         self.lp.BindcarCustomer(self.park_checkbox)
     #查询新建的车位
     def test_20selnewcarparknum(self):
         self.lp.select_inputbox(self.carnumber,self.park_numberbox)
     #查询管理区数据
     def test_21seldevelop(self):
         self.lp.select_develop(self.park_guanliqubox,self.guanliqu)
     #删除新建车位数据
     def test_22delnewparking(self):
         self.lp.del_newData(self.carnumber,self.park_checkbox)
     @classmethod
     def tearDownClass(cls):
         cls.lp.quet()

if __name__ == "__main__":
    unittest.main()

