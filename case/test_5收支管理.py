#coding=utf-8
import unittest
from handle import handle
from case import baseCase

class Test_BascinfoCase(baseCase.BaseCase,unittest.TestCase):
     bc = baseCase.BaseCase()
     driver = bc.getDriver()
     lp = handle.szgu(driver)
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
     def test_1szgu(self):
          self.lp.szgul()
     def test_2bulidszkm(self):
          try:
               self.lp.delnewbulid(self.name,self.delmessage)
          except:
               print("数据不存在")
          self.lp.szkunew(self.name,1,self.newmessage)
     def test_3editszkm(self):
          self.lp.editszkm(self.check_szkm,self.name,self.editmessage,self.check_queren)
     def test_4delszkm(self):
          self.lp.delnewbulid(self.name,self.delmessage)
     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()
if __name__ =="__main__":
     unittest.main()