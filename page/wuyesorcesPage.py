#coding=utf-8
from page import BaseDriver
from time import  sleep
class BascinfoPage(BaseDriver.BascPage):
     def __init__(self,driver):
          super(BascinfoPage,self).__init__(driver)
     #获取物业资源树搜索框
     def sendkeys_wuYeTree(self,guanliqu):
          self.sendkeys('物业资源搜索框',guanliqu)
     #获取物业资源搜索按钮
     def click_wuYeSerch(self):
          self.click("物业资源搜索")
     #获取物业资源树上搜索的管理区
     def click_guanLiQuTree(self):
          self.click("资源树管理区")
     #点击添加下级
     def click_xiaJiJigou(self):
          self.click("添加下级")
     #点击添加分组
     def click_fenZu(self):
          self.click("添加分组")
     #输入分组名称
     def sendkey_fenZuName(self,name):
          self.sendkeys("分组名称",name)
     #输入分组地址
     def sendkey_fenZuDiZhi(self,address):
          self.sendkeys("分组地址",address)
     #分组说明
     def sendkey_fenZuMark(self,mark):
          self.sendkeys("分组说明",mark)
     #分组编辑
     def click_fenZuEdit(self):
          self.click("分组编辑")
     #分组删除
     def click_fuZuDelete(self):
          self.click("分组删除")
     '''
     点击弹窗确定按钮，物业资源管理：分组、楼宇、单元、房间、停车场、车位、广告位
     '''
     def click_divConfirm(self):
          self.click("分组确定")

     '''
          点击弹窗确定按钮,物业资源管理：分组、楼宇、单元、房间、停车场、车位、广告位
     '''
     def click_divCancel(self):
          self.click("分组取消")


     #点击添加楼宇
     def click_louYu(self):
          self.click("添加楼栋")
     #楼宇名称
     def sendkey_louYuName(self,name):
          self.sendkeys("楼宇名称",name)
     #楼宇序号
     def sendkey_louYuCode(self,code):
          self.sendkeys("楼宇序号",code)
     #楼宇层数
     def sendkey_louYuFloor(self,floor):
          self.sendkeys("楼宇层数",floor)
     #楼宇备注
     def sendkey_louYuMark(self,mark):
          self.sendkeys("楼宇备注",mark)
     #楼宇编辑
     def click_louYuEdit(self):
          self.click("楼宇编辑")
     #楼宇删除
     def click_louYuDelete(self):
          self.click("楼宇删除")
     #楼宇查看
     def click_louYuLook(self):
          self.click("楼宇查看")

     #关闭查看页面
     def click_pageDetails(self):
          self.click("查看页面关闭按钮")

     #点击添加停车场
     def click_tingCheChang(self):
          self.click("添加停车场")

     #停车场名称
     def sendkey_tingCheChangName(self,name):
          self.sendkeys("停车场名称",name)
     #停车场地址
     def sendkey_tingCheChangAddress(self,address):
          self.sendkeys("停车场地址",address)

     #停车场说明
     def sendkey_tingCheChangMark(self,mark):
          self.sendkeys("停车场说明",mark)
     #编辑停车场
     def click_editTingCheChang(self):
          self.click("停车场编辑")
     #删除停车场
     def click_deleteTingCheChang(self):
          self.click("停车场删除")
     #查看停车场
     def click_lookTingCheChang(self):
          self.click("停车场查看")
     #点击取消删除
     def click_quXiaoDelete(self):
          self.click("取消删除")
     #点击确认删除
     def click_queRenDelete(self):
          self.click("确认删除")
     #点击导出Excel
     def click_expotExcle(self):
          self.click("导出Excel")
     #搜索框输入数据
     def sendkeys_serch(self,value):
          self.sendkeys("搜索框",value)
     #搜索框点击按钮
     def click_serch(self):
          self.click("搜索按钮")
     #获取物业资源管理总公司下6个tab页面
     def get_sixSources(self):
          return self.get_element("6个tab页面")
     #点击管理区、楼宇、停车场、房间、车位、广告位中的一个标签。
     def click_sixTab(self,num):
          self.driver.find_element_by_xpath\
               ("//div[@class='ant-tabs-nav-scroll']/div/div/div[%d]"%(num)).click()
     #点击楼宇列表中第一个checkbox
     def click_wuyeCheckbox(self):
          self.click("4个页面checkbox")
     #点击房间列表中第一个checkbox
     def click_fangJianCheckbox(self):
          self.click("房间CheckBox")
     #添加下级，添加房间
     def click_louYuXiaJi(self):
          self.click("楼宇添加下级")
     #点击添加房间
     def click_houseAdd(self):
          self.click("添加房间")
     # 点击编辑房间
     def click_houesEdit(self):
          self.click("房间编辑")
     #点击房间删除
     def click_houseDelete(self):
          self.click("房间删除")
     #点击房间查看
     def click_houseLook(self):
          self.click("房间查看")
     #点击业主管理
     def click_houseOwner(self):
          self.click("业主管理")
     #点击当前居住成员
     def click_houseMember(self):
          self.click("当前居住成员")
     #









