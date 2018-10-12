#coding=utf-8
import unittest
from handle import handle
from case import baseCase

class Test_BascinfoCase(baseCase.BaseCase,unittest.TestCase):
     bc = baseCase.BaseCase()
     driver = bc.getDriver()
     lp = handle.louyu(driver)
     fangchan_check = bc.readData("fangchan_check")#读取楼宇列表中的checkbox
     fangchan_guanlq=bc.readData("fangchan_guanlq")
     fangchan_liecode=bc.readData("fangchan_liecode")
     close = bc.readData("fangchan_close")
     fangchan_code = bc.readData("fangchan_code")
     guanliqu="滨湖新城"
     @classmethod
     def setUpClass(cls):
          url=cls.bc.readUrl("fangchandanganURL")
          cls.lp.get(url)
          cls.lp.setCookie()
          cls.lp.get(url)
          cls.lp.switch_fram("iframe")
     #新建房产档案
     def test_1newfangchan(self):
         try:
             self.lp.del_newData(self.fangchan_code,self.fangchan_check)
         except:
             print("数据还未新建")
         self.lp.newfangchan(self.guanliqu,10,60,self.fangchan_code,120)
     #编辑房产档案
     def test_2editfangchan(self):
         self.lp.edit(self.fangchan_check)
     #改变业主
     def test_3change_Customer(self):
         self.lp.changeCustomer(self.fangchan_check,2)
     #查看改变业主历史记录
     def test_4change_history(self):
         self.lp.changeHistory(self.fangchan_check,self.close)
     #改变房间状态
     def test_5change_status(self):
         self.lp.selectdata("")
         self.lp.changeStatus(self.fangchan_check,'交房')
     #批量生成按钮和导出Excel按钮
     def test_6piliang(self):
         self.lp.piliangshengcheng("导出Excel")
     #查询房间代码含有输入data的房间
     def test_7select_fangchan(self):
         self.lp.select_inputbox(self.fangchan_code,self.fangchan_liecode)
     #按管理区查询管理区数据
     def test_8select_fangchan_guanliqu(self):
         self.lp.select_develop(self.guanliqu,self.fangchan_guanlq)
     #删除新建房产数据
     def test_9delfangchan(self):
         self.lp.del_newData(self.fangchan_code,self.fangchan_check)

     @classmethod
     def tearDownClass(cls):
         cls.lp.quet()
if __name__ == "__main__":
    unittest.main()
