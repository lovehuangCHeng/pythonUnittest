#coding=utf-8
import unittest
from handle import handleWuYeScores
from case import baseCase
import allure
import pytest

@allure.feature('物业资源管理')
class Test_BascinfoCase(baseCase.BaseCase,unittest.TestCase):
     bc = baseCase.BaseCase()
     driver = bc.getDriver()
     lp = handleWuYeScores.louyu(driver)
     guanliqu=bc.reddatasql("guanliqusql",0)[0]
     louyu=bc.reddatasql("louyu",0)[0]
     parking=bc.reddatasql("tingchangc",0)[0]
     fenZuName='长虹道馆'
     louYuName='长虹1栋'
     carParking='长虹停车场'
     @classmethod
     def setUpClass(cls):
          url = cls.bc.readUrl("物业资源管理")
          cls.lp.get(url)
          cls.lp.setCookie()
          cls.lp.get(url)
     ''''''
     #选择管理区
     def test_10guanliqu(self):
          self.lp.get_treeSerch(self.guanliqu)
          self.lp.assertTure('添加下级','添加下级')

     #新建分组
     def test_11addFenZu(self):
          self.lp.add_fenZu(self.fenZuName,'石桥铺','这个是分组数据')
          self.lp.assertTure('添加下级','添加下级')

     #查询分组
     def test_12selectFenZu(self):
          self.lp.get_treeSerch(self.fenZuName)

     #编辑分组
     def test_13editFenZu(self):
          self.lp.edit_fenZu(self.fenZuName)

     #删除分组
     def test_14deleteFenZu(self):
          self.lp.delete_fenZu(self.fenZuName)

     # 选择管理区
     def test_15guanliqu(self):
          self.lp.get_treeSerch(self.guanliqu)
          self.lp.assertTure('添加下级', '添加下级')
     #新建楼宇
     def test_16addLouYu(self):
          self.lp.add_louYu(self.louYuName,'2','5220','楼宇数据')
              
     #搜索楼宇
     def test_17selectLouYu(self):
          self.lp.get_srechdData(2,self.louYuName)
          self.lp.assertTure('楼宇查看',self.louYuName)

     #编辑楼宇
     def test_18editLouYu(self):
          self.lp.edit_louYu(2,self.louYuName)
          self.lp.assertTure('楼宇查看',self.louYuName)

     #查看楼宇
     def test_19lookLouYu(self):
          self.lp.look_louYu(2,self.louYuName)
          self.lp.assertTure("查看页面title","楼宇详情")
     #关闭查看页面
     def test_20closeLouYu(self):
          self.lp.click_pageDetails()
          self.lp.assertTure('楼宇查看', self.louYuName)
     #删除楼宇
     def test_21deleteLouYu(self):
          self.lp.delete_louYu(2,self.louYuName)
          #self.lp.assertTure("","删除成功")
     # 选择管理区
     def test_22guanliqu(self):
          self.lp.get_treeSerch(self.guanliqu)
          self.lp.assertTure('添加下级', '添加下级')
     #新建停车场
     def test_23addCarPark(self):
          self.lp.add_carParking(self.carParking,"重庆新天地","这个是停车场的数据")

     #搜索停车场数据
     def test_24selectCarPark(self):
          self.lp.get_srechdData(3,self.carParking)
          self.lp.assertTure("停车场查看",self.carParking)
     #编辑停车场数据
     def test_25editCarPark(self):
          self.lp.edit_caiParking(3,self.carParking)
          self.lp.assertTure("停车场查看", self.carParking)
     #查看停车场数据
     def test_26lookCarPark(self):
          self.lp.look_carParking(3, self.carParking)
          self.lp.assertTure("查看页面title", "停车场详情")
     #关闭停车场查看页面
     def test_27closeCarPark(self):
          self.lp.click_pageDetails()
          self.lp.assertTure('楼宇查看', self.carParking)
     #删除停车场数据
     def test_28deleteCarPark(self):
          self.lp.delete_carParking(3,self.carParking)
     #资源树上搜索楼宇
     def test_29selectLouYu(self):
          self.lp.get_treeSerch(self.louyu)
     # 新建房间
     # 编辑房间
     # 查看房间
     # 查看房间，业主管理
     # 查看房间，成员管理
     # 编辑房间
     # 删除房间

     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()
if __name__ =="__main__":
     pytest.main(['-s', '-q', '--alluredir', './report/xml'])


