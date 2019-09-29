#coding=utf-8
import unittest
from handle import handleWuYeScores
from case import baseCase

class Test_BascinfoCase(baseCase.BaseCase,unittest.TestCase):
     bc = baseCase.BaseCase()
     driver = bc.getDriver()
     lp = handleWuYeScores.louyu(driver)
     guanliqu=bc.reddatasql(0)[0]
     @classmethod
     def setUpClass(cls):
          url = cls.bc.readUrl("物业资源管理")
          cls.lp.get(url)
          cls.lp.setCookie()
          cls.lp.get(url)
     #新建楼宇
     def test_1guanliqu(self):
          try:
               self.lp.get_guanliqu(self.guanliqu)
          except:
               print("获取元素失败！！！")

     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()
if __name__ =="__main__":
     unittest.main()


