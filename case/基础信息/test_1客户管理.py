#coding=utf-8
import  unittest
from handle.基础信息.客户管理 import kuHuHandle as ly
from time import  sleep
class Test_BascinfoCase(unittest.TestCase):
     url=ly.url_kehudangan
     lp=ly()
     @classmethod
     def setUpClass(cls):
          cls.lp.geturl(cls.url)
          cls.lp.setCookie()
          sleep(3)
          cls.lp.geturl(cls.url)
          cls.lp.closetabl()
          cls.lp.geturl(cls.url)

     def test1_add_kehu(self):
          try:
               self.lp.kehu_delete("张胜男")
          except:
               print("删除数据成功")
          self.lp.kehu_add("张胜男",18536524152)

     def test2_secrch_kehu(self):

          self.lp.kehu_secrch("张胜男")
          self.lp.assert_kehu_name("张胜男")


     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()



