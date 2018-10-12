#coding=utf-8
import unittest
from handle import handle
from case import baseCase

class Test_BascinfoCase(baseCase.BaseCase,unittest.TestCase):
     bc = baseCase.BaseCase()
     driver = bc.getDriver()
     lp = handle.louyu(driver)
     checkbox = bc.readData("checkboxloyu")#读取楼宇列表中的checkbox
     louyuname=bc.readData("louyuname")
     guanliqu=bc.readData("guanliqu_louyu")
     dataguanliqu=bc.reddatasql("guanliqusql",1)
     @classmethod
     def setUpClass(cls):
          url=cls.bc.readUrl("louyuURL")
          cls.lp.get(url)
          cls.lp.setCookie()
          cls.lp.get(url)
          cls.lp.switch_fram("iframe")
     #新建楼宇
     def test_1newlouyu(self):
          try:
               self.lp.del_newData("大地大时代",self.checkbox)
          except:
               print("还没有新建这个元素")
          self.lp.newloyu(self.dataguanliqu,"大地大时代",522000)
     #编辑楼宇
     def test_2edit(self):
          self.lp.edit(self.checkbox)
     #查询新建楼宇
     def test_3select(self):
          self.lp.select_inputbox("大地大时代",self.louyuname)
     #安管理区查询数据
     def test_4seldevelop(self):
          self.lp.select_develop(self.guanliqu,self.dataguanliqu)
     #删除新建楼宇
     def test_5del(self):
          self.lp.del_newData("大地大时代",self.checkbox)
     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()
if __name__ =="__main__":
     unittest.main()


