#coding=utf-8

from case import baseCase
import  unittest

class Test_BascinfoCase(baseCase.BaseCase, unittest.TestCase):
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
     #导出楼宇数据
     def test_21expotExecl(self):
          self.lp.excport_excle(2)
          self.lp.assertTure("导出Excel","导出Excel")
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
     #导出停车场数据
     def test_29expotExecl(self):
          self.lp.excport_excle(3)
          self.lp.assertTure("导出Excel","导出Excel")
     #资源树上搜索楼宇
     #def test_29selectLouYu(self):
          #self.lp.get_treeSerch(self.louyu)
     # 新建房间
     def test_30addHouse(self):
          self.lp.add_house("",2,2,self.houseCode,60)
     # 编辑房间
     def test_31editHouse(self):
          self.lp.edit_house(self.houseCode)
     # 查看房间，业主管理
     def test_32ownerHouse(self):
          self.lp.look_houseOwner(self.houseCode)
          self.lp.assertTure("查看页面title","房间详情")

     # 查看房间，成员管理
     def test_33memberHouse(self):
          self.lp.look_houseMember(self.houseCode)
          self.lp.assertTure("查看页面title","房间详情")
     # 查看房间
     def test_34lookHouse(self):
          self.lp.look_house(self.houseCode)
          self.lp.assertTure("查看页面title", "房间详情")
          self.lp.click_pageDetails()
     # 删除房间
     def test_35deleteHouse(self):
          self.lp.delete_house(self.houseCode)
     # 导出房间数据
     def test_36expotExecl(self):
          self.lp.excport_excle(4)
          self.lp.assertTure("导出Excel", "导出Excel")
     #添加单元
     def test_37addUnit(self):
          self.lp.add_unit("",self.unitName,50)
     #编辑单元
     def test_38edit(self):
          self.lp.edit_unit(self.unitName)
     #删除单元
     def test_39deleteUnit(self):
          self.lp.delete_unit(self.unitName)
     #添加车位
     def test_40addParkingLot(self):
          self.lp.add_parkingLot("",self.carCode,25)
     #编辑车位
     def test_41editParkingLot(self):
          self.lp.edit_parkingLot(self.carCode)
     #绑定车位业主
     def test_42binbingParkingLot(self):
          self.lp.binding_parkingLot(self.carCode)
     #查看车位
     def test_43lookParkingLot(self):
          self.lp.look_parkingLot(self.carCode)
     #删除车位
     def test_44deleteParkingLot(self):
          self.lp.delete_parkingLot(self.carCode)
     #d导出车位数据
     def test_45expotExecl(self):
          self.lp.excport_excle(5)
          self.lp.assertTure("导出Excel", "导出Excel")
     #添加广告为
     def test_46addAdverising(self):
          self.lp.add_adverising("",self.adverCode,2)
     #编辑广告位
     def test_47editAdverising(self):
          self.lp.edit_adverising(self.adverCode)
     #查看广告位
     def test_47lookAdverising(self):
          self.lp.look_adverising(self.adverCode)
     #删除广告位
     def test_48deleteAdverising(self):
          self.lp.delete_adverising(self.adverCode)
     # d导出车位数据
     def test_49expotExecl(self):
          self.lp.excport_excle(6)
          self.lp.assertTure("导出Excel", "导出Excel")
     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()



