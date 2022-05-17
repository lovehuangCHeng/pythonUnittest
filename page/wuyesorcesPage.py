#coding=utf-8
from page import BaseDriver


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

     '''
          楼宇页面的元素
     '''

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

     '''
     停车场页面的元素
     '''
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
     '''
     房间页面的元素
     '''
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
     def click_houseEdit(self):
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
     #点击成员管理
     def click_houseBtnMember(self):
          self.click("成员管理")
     #输入房间楼层
     def sendkey_houseFloor(self,floor):
          self.sendkeys("房间楼层",floor)
     #输入房间序号，正整数
     def sendkey_houseRank(self,rank):
          self.sendkeys("房间序号",rank)
     #输入房间代码
     def sendkey_houseCode(self,code):
          self.sendkeys("房间代码",code)
     #输入房间建筑面积
     def sendkey_houseArea(self,area):
          self.sendkeys("房间建筑面积",area)
     #点击房间类型
     def click_houseType(self):
          self.click("房间类型")
     #选择房间类型为办公
     def click_houseTpyeValue(self):
          self.click("办公")
     #点击房间状态
     def click_houseStatus(self):
          self.click("房间状态")
     #选择房间状态为接访的房间
     def click_houseStatusValue(self):
          self.click("交房")

     '''
     单元的元素
     '''
     #点击添加单元
     def click_unitAdd(self):
          self.click("添加单元")
     #输入单元名称
     def sendkey_unitName(self,name):
          self.sendkeys("单元名称",name)
     #输入单元序号
     def sendkey_unitCode(self,code):
          self.sendkeys("单元序号",code)
     #编辑单元
     def click_unitEdit(self):
          self.click("编辑单元")
     #删除单元
     def click_unitDelete(self):
          self.click("删除单元")

     '''
     车位页面的元素
     '''
     #点击添加车位
     def click_parkingLotAdd(self):
          self.click("添加车位")
     #点击车位查看
     def click_parkingLotLook(self):
          self.click("车位查看")
     #点击车位编辑
     def click_parkingLotEdit(self):
          self.click("车位编辑")
     #点击车位删除
     def click_parkingLotDelete(self):
          self.click("车位删除")
     #点击绑定业主
     def click_parkingLotOwern(self):
          self.click("绑定业主")
     #输入车位号
     def sendkey_parkingLotCode(self,code):
          self.sendkeys("车位号",code)
     #输入车位面积
     def sendkey_parkingLotArea(self,area):
          self.sendkeys("车位面积",area)
     #点击出售日期
     def click_parkingLotTime(self):
          self.click("出售日期")
     #点击今天
     def click_TimeTody(self):
          self.click("今天")
     '''
     广告位页面的元素
     '''
     #点击添加广告位
     def click_adverisingAdd(self):
          self.click("添加广告位")
     #点击编辑广告位
     def click_adverisingEdit(self):
          self.click("编辑广告位")
     #点击删除广告位
     def click_adverisingDelete(self):
          self.click("删除广告位")
     #点击查看广告位
     def click_adverisingLook(self):
          self.click("查看广告位")
     #输入广告位号
     def sendkey_adverisingCode(self,code):
          self.sendkeys("广告位号",code)
     #s输入广告位楼层
     def sendkey_adverisingFloor(self,floor):
          self.sendkeys("广告位楼层",floor)
     #选择广告位，已出租
     def click_adverisingLease(self):
          self.click("已出租")

     # 选择广告位，未出租
     def click_adverisingUnLease(self):
          self.click("未出租")





