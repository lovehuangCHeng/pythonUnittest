#coding=utf-8
import unittest
from handle import handle
from case import baseCase

class Test_BascinfoCase(baseCase.BaseCase,unittest.TestCase):
     bc = baseCase.BaseCase()
     driver = bc.getDriver()
     lp = handle.louyu(driver)
     #客户管理
     customer_checkbox=bc.readData("customer_check")
     customer_rename=bc.readData("cusomer_renametitle")
     customer_renameclose=bc.readData("customer_renameclose")
     customer_namebox=bc.readData("customer_namebox")
     customer_guanliqubox=bc.readData("customer_guanliqubox")
     #交房登记
     jiaofang_checkbox=bc.readData("jiaofang_checkbox")
     jiaofang_guanliqubox=bc.readData("jiaofang_guanliqubox")
     #接房登记
     jiefang_guanliqubox=bc.readData("jiefang_guanliqubox")
     #入住登记
     ruzhu_guanliqubox=bc.readData("ruzhu_guanliqubox")
     guanliqu="滨湖新城"
     name="沁园春传说"
     @classmethod
     def setUpClass(cls):
          url=cls.bc.readUrl("customerURL")
          cls.lp.get(url)
          cls.lp.setCookie()
          cls.lp.get(url)
          cls.lp.switch_fram("iframe")

     #新建客户档案
     def test_11newcustomer(self):
         try:
             self.lp.del_newData(self.name,self.customer_checkbox)
         except:
             print("还没新建这个用户数据")
         self.lp.newcustomer(self.guanliqu,self.name)
     #编辑客户档案
     def test_12editcustomer(self):
         self.lp.editcustomer(self.customer_checkbox)
     #合并重名客户
     def test_13renamemerge(self):
         self.lp.renameMerge(self.customer_rename,self.customer_renameclose)
     #查询新建客户
     def test_14slectname(self):
         self.lp.select_inputbox(self.name,self.customer_namebox)
     #查询管理区
     def test_15selguanliqu(self):
         self.lp.select_develop(self.customer_guanliqubox,self.guanliqu)
     #删除新建客户数据
     def test_16delnewcustomer(self):
         self.lp.del_newData(self.name,self.customer_checkbox)
     '''
     切换iframe进入到交房登记
     '''
     def test_17switchjiaofang(self):
         url=self.bc.readUrl("jiaofangURL")
         self.lp.switch_url(url)
     #新建交房登记
     def test_21newjiaofang(self):
         self.lp.jiaofangdengji()
     #编辑交房登记
     def test_22editjiaofang(self):
         self.lp.changjiaofang(self.jiaofang_checkbox)
     #查询管理区
     def test_23selguanliqu(self):
         self.lp.select_inputbox(self.guanliqu,self.jiaofang_guanliqubox)
     #高级查询页面
     def test_24seldevelop(self):
         self.lp.select_develop(self.jiaofang_guanliqubox,self.guanliqu)
     '''
     切换iframe，url跳转url到接房页面
     '''
     def test_25switchjiefang(self):
         url=self.readUrl("jiefangURL")
         self.lp.switch_url(url)
     #新建接房登记数据
     def test_31newjiefang(self):
         self.lp.jiefangdengji(3)
     #编辑接房登记数据
     def test_32editjiefang(self):
         self.lp.jiefang_edit(self.jiefang_guanliqubox)
     #查看接房登记
     def test_33chakan(self):
         self.lp.chakan(self.jiefang_guanliqubox)
     #搜索接房登记数据，按管理区
     def test_34selguanliqu(self):
         self.lp.select_inputbox(self.guanliqu,self.jiefang_guanliqubox)
     #高级搜索按钮
     def test_35seldevelop(self):
         self.lp.select_develop(self.jiefang_guanliqubox,self.guanliqu)
     '''
     进入到入住登记页面
     '''
     def test_36switchruzhu(self):
         url=self.bc.readUrl("ruzhuURL")
         self.lp.switch_url(url)
     #编辑入住登记数据
     def test_38editruzhu(self):
         self.lp.ruzhu_edit(self.ruzhu_guanliqubox)
     #查看入住登记
     def test_37ruzhuchakan(self):
         self.lp.chakan(self.ruzhu_guanliqubox)
     #搜索入住登记数据
     def test_39selguanliqu(self):
         self.lp.select_inputbox(self.guanliqu,self.ruzhu_guanliqubox)
     #高级搜索
     def test_40seldevelop(self):
         self.lp.select_develop(self.ruzhu_guanliqubox,self.guanliqu)
     @classmethod
     def tearDownClass(cls):
         cls.lp.quet()
if __name__ == "__main__":
    unittest.main()
