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
     guanliqu_louyu=bc.readData("guanliqu_louyu")
     #dataguanliqu=bc.reddatasql("guanliqusql",1)
     fangchan_check = bc.readData("fangchan_check")  # 读取楼宇列表中的checkbox
     fangchan_guanlq = bc.readData("fangchan_guanlq")
     fangchan_liecode = bc.readData("fangchan_liecode")
     close = bc.readData("fangchan_close")
     fangchan_code = bc.readData("fangchan_code")
     houseSummary_guanli = bc.readData("houseSummary_guanli")
     url_1 = bc.readUrl("fangchantongjiURL")
     guanliqu = "滨湖新城"
     @classmethod
     def setUpClass(cls):
          url=cls.bc.readUrl("louyuURL")
          cls.lp.get(url)
          cls.lp.setCookie()
          cls.lp.get(url)
          cls.lp.switch_fram("iframe")
     #新建楼宇
     def test_11newlouyu(self):
          try:
               self.lp.del_newData("大地大时代",self.checkbox)
          except:
               print("还没有新建这个元素")
          self.lp.newloyu(self.guanliqu,"大地大时代",522000)
     #编辑楼宇
     def test_12edit(self):
          self.lp.edit(self.checkbox)
     #查询新建楼宇
     def test_13select(self):
          self.lp.select_inputbox("大地大时代",self.louyuname)
     #安管理区查询数据
     def test_14seldevelop(self):
          self.lp.select_develop(self.guanliqu_louyu,self.guanliqu)
     #删除新建楼宇
     def test_15del(self):
          self.lp.del_newData("大地大时代",self.checkbox)
     '''
     切换iframe标签，进入房产档案页面
     '''
     def test_16switch_fangchandangan(self):
          url=self.bc.readUrl("fangchandanganURL")
          self.lp.switch_url(url)
     # 批量生成按钮和导出Excel按钮
     def test_21piliang(self):
          self.lp.piliangshengcheng("导出EXCEL")

     # 新建房产档案
     def test_22newfangchan(self):
          try:
               self.lp.del_newData(self.fangchan_code, self.fangchan_check)
          except:
               print("数据还未新建")
          self.lp.newfangchan(self.guanliqu, 10, 60, self.fangchan_code, 120)

     # 编辑房产档案
     def test_23editfangchan(self):
          self.lp.edit(self.fangchan_check)

     # 改变业主
     def test_24change_Customer(self):
          self.lp.changeCustomer(self.fangchan_check, 2)

     # 查看改变业主历史记录
     def test_25change_history(self):
          self.lp.changeHistory(self.fangchan_check, self.close)

     # 改变房间状态
     def test_26change_status(self):
          self.lp.selectdata("")
          self.lp.changeStatus(self.fangchan_check, '交房')

     # 查询房间代码含有输入data的房间
     def test_27select_fangchan(self):
          self.lp.select_inputbox(self.fangchan_code, self.fangchan_liecode)

     # 按管理区查询管理区数据
     def test_28select_fangchan_guanliqu(self):
          self.lp.select_develop(self.fangchan_guanlq, self.guanliqu)

     # 删除新建房产数据
     def test_29delfangchan(self):
          self.lp.del_newData(self.fangchan_code, self.fangchan_check)
     '''
     进入房产统计页面
     '''
     def test_31runtongji(self):
          self.lp.switch_default()
          self.lp.get(self.url_1)
          self.lp.housesummry()
     # 搜索普通搜索
     def test_32summerysel(self):
          self.lp.select_inputbox(self.guanliqu, self.houseSummary_guanli)

     # 房产统计高级搜索
     def test_33summertsel_develop(self):
          self.lp.select_develop(self.houseSummary_guanli, self.guanliqu)
     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()
if __name__ =="__main__":
     unittest.main()


