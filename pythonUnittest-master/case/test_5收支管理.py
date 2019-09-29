#coding=utf-8
import unittest
from handle import handleWuYeScores
from case import baseCase

class Test_BascinfoCase(unittest.TestCase):
     bc = baseCase.BaseCase()
     driver = bc.getDriver()
     lp = handleWuYeScores.szgu(driver)
     check_szkm = bc.readData("check_szkm")#读取楼宇列表中的checkbox
     check_queren=bc.readData("querenbtn")
     name=bc.readData("kumumingce")
     newmessage=bc.readData("newsussfull")
     editmessage=bc.readData("editmessage")
     delmessage=bc.readData("delmessage")
     @classmethod
     def setUpClass(cls):
          url=cls.bc.readUrl("homeURL")
          cls.lp.get(url)
          cls.lp.setCookie()
          cls.lp.get(url)
     #进入收支管理页面，收支科目
     def test_1szgu(self):
          self.lp.szgul()
     #新建收支科目，1代表收费，0代表支出
     def test_2bulidszkm(self):
          try:
               self.lp.delnewbulid(self.name,self.delmessage)
          except:
               print("数据不存在")
          self.lp.szkunew(self.name,1,self.newmessage)
     #编辑收支科目
     def test_3editszkm(self):
          self.lp.editszkm(self.check_szkm,self.name,self.editmessage,self.check_queren)
     #删除收支科目
     def test_4delszkm(self):
          self.lp.delnewbulid(self.name,self.delmessage)

     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()
if __name__ =="__main__":
     unittest.main()