#coding=utf-8
import  unittest
from handle.基础信息.客户管理 import kuHuHandle as ly
from time import  sleep
class Test_BascinfoCase(unittest.TestCase):
     url=ly.url_kehudangan
     lp=ly()
     customerName="张胜男"
     @classmethod
     def setUpClass(cls):
          cls.lp.geturl(cls.url)
          cls.lp.setCookie()
          sleep(3)
          cls.lp.geturl(cls.url)
          cls.lp.closetabl()
          cls.lp.geturl(cls.url)
     #新建
     def test1_add_kehu(self):
          try:
               self.lp.kehu_delete(self.customerName)
          except:
               print("删除数据成功")
          self.lp.kehu_add(self.customerName,18536524152)

     # 查询
     def test2_secrch_kehu(self):
          self.lp.kehu_secrch(self.customerName)
          self.lp.assert_kehu_name(self.customerName)

     # 编辑
     def test3_edit_kehu(self):
          self.lp.kehu_edit()
          self.lp.assert_kehu_saveSucc("保存成功")
         #保存成功！


     # 删除
     def test4_del_kehu(self):
          self.lp.kehu_delete(self.customerName)
          self.lp.assert_kehu_delSucc("删除成功")
     #高级搜索
     def test5_ineer_kehu(self):
          self.lp.kehu_sennior_secrch()

     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()



