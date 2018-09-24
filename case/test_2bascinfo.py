#coding=utf-8
import unittest
from handle import handle
from case import baseCase

class BascinfoCase(baseCase.BaseCase,unittest.TestCase):
     bc = baseCase.BaseCase()
     driver = bc.getDriver()
     lp = handle.louyu(driver)
     @classmethod
     def setUpClass(cls):
          url=cls.bc.readUrl("louyuURL")
          cls.lp.get(url)
          cls.lp.setCookie()
          cls.lp.get(url)
          cls.lp.switch_fram("iframe")
     def test_1newlouyu(self):
          checkbox = self.bc.readData("checkbox")
          try:
               self.lp.del_newData("大地大时代",checkbox)
          except:
               print("还没有新建这个元素")
          self.lp.newloyu("滨湖新城","大地大时代",5220)
     def test_2edit(self):
          checkbox = self.bc.readData("checkbox")
          self.lp.edit(checkbox)
     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()
if __name__ =="__main__":
     unittest.main()