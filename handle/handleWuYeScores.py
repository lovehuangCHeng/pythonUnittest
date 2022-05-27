#coding=utf-8
from page import wuyesorcesPage
from time import sleep
from config.elements import  geturl
class louyuHandle(wuyesorcesPage.BascinfoPage):
     khda_url = geturl.客户档案
     wyzy_url = geturl.物业资源管理
     '''
     物业资源管理树，搜索当前查询的数据，并点击这个查找的数据。
     '''
     def get_treeSerch(self,value):
          sleep(1)
          self.sendkeys_wuYeTree(value)
          sleep(1)
          self.click_wuYeSerch()
          sleep(1)
          self.click_guanLiQuTree()
          sleep(1)
     '''
     物业资源管理，6个列表中查询数据
     '''
     def get_srechdData(self,num,value):
          # sleep(1)
          # self.refresh()
          sleep(1)
          self.click_sixTab(num)
          sleep(1)
          self.sendkeys_serch(value)
          sleep(1)
          self.click_serch()
          sleep(1)
     '''
     导出Excel
     '''
     def excport_excle(self,num):
          sleep(1)
          self.click_sixTab(num)
          sleep(1)
          self.click_expotExcle()
          sleep(1)

     '''
     新建分组
     '''
     def add_fenZu(self,name,address,mark):
          sleep(1)
          self.click_xiaJiJigou()
          sleep(1)
          self.click_fenZu()
          sleep(1)
          self.sendkey_fenZuName(name)
          sleep(1)
          self.sendkey_fenZuDiZhi(address)
          sleep(1)
          self.sendkey_fenZuMark(mark)
          sleep(1)
          self.click_divConfirm()
          sleep(1)

     '''
     编辑分组
     '''
     def edit_fenZu(self,fenzu):
          sleep(1)
          self.get_treeSerch(fenzu)
          sleep(1)
          self.click_fenZuEdit()
          sleep(1)
          self.click_divConfirm()
          sleep(1)
     '''
     删除分组
     '''
     def delete_fenZu(self,fenzu):
          sleep(1)
          self.get_treeSerch(fenzu)
          sleep(1)
          self.click_fuZuDelete()
          sleep(1)
          self.click_queRenDelete()

     '''
     新建楼宇
     '''
     def add_louYu(self,name,floor,code,mark):
          sleep(1)
          self.click_xiaJiJigou()
          sleep(1)
          self.click_louYu()
          sleep(1)
          self.sendkey_louYuName(name)
          sleep(1)
          self.sendkey_louYuFloor(floor)
          sleep(1)
          self.sendkey_louYuCode(code)
          sleep(1)
          self.sendkey_louYuMark(mark)
          sleep(1)
          self.click_divConfirm()
          sleep(1)

     '''
     编辑楼宇, @prams  name 楼宇名称
     '''
     def edit_louYu(self,num,name):
          sleep(1)
          self.get_srechdData(num,name)
          sleep(1)
          self.click_louYuEdit()
          sleep(1)
          self.click_divConfirm()
          sleep(1)

     '''
     查看楼宇 name 楼宇名称
     '''
     def look_louYu(self,num,name):
          sleep(1)
          self.get_srechdData(num,name)
          sleep(1)
          self.click_louYuLook()
          sleep(1)
     '''
     删除楼宇 name 楼宇名称
     '''
     def delete_louYu(self,num,name):
          sleep(1)
          self.get_srechdData(num,name)
          sleep(1)
          self.click_louYuDelete()
          sleep(1)
          self.click_queRenDelete()
          sleep(1)
     '''
     添加停车场
     '''
     def add_carParking(self,name,address,mark):
          sleep(1)
          self.click_xiaJiJigou()
          sleep(1)
          self.click_tingCheChang()
          sleep(1)
          self.sendkey_tingCheChangName(name)
          sleep(1)
          self.sendkey_tingCheChangAddress(address)
          sleep(1)
          self.sendkey_tingCheChangMark(mark)
          sleep(1)
          self.click_divConfirm()
          sleep(1)
     '''
     编辑停车场
     '''
     def edit_caiParking(self,num,name):
          sleep(1)
          self.get_srechdData(num,name)
          sleep(1)
          self.click_editTingCheChang()
          sleep(1)
          self.click_divConfirm()
          sleep(1)

     '''
     查看停车场
     '''
     def look_carParking(self,num,name):
          sleep(1)
          self.get_srechdData(num,name)
          sleep(1)
          self.click_lookTingCheChang()
          sleep(1)
     '''
     删除停车场
     '''
     def delete_carParking(self,num,name):
          sleep(1)
          self.get_srechdData(num,name)
          sleep(1)
          self.click_deleteTingCheChang()
          sleep(1)
          self.click_queRenDelete()
          sleep(1)
     '''
     进入添加房间页面,添加房间
     '''
     def add_house(self,lyname,floor,rank,code,area):
          self.look_louYu(2,lyname)
          sleep(1)
          self.click_louYuXiaJi()
          sleep(1)
          self.click_houseAdd()
          sleep(1)
          self.sendkey_houseFloor(floor)
          sleep(1)
          self.sendkey_houseRank(rank)
          sleep(1)
          self.sendkey_houseCode(code)
          sleep(1)
          self.sendkey_houseArea(area)
          sleep(1)
          self.click_houseType()
          sleep(1)
          self.click_houseTpyeValue()
          sleep(1)
          self.click_houseStatus()
          sleep(1)
          self.click_houseStatusValue()
          sleep(1)
          self.click_divConfirm()
          sleep(1)
     '''
     编辑房间
     '''
     def edit_house(self,code):
          sleep(1)
          self.get_srechdData(4,code)
          sleep(1)
          self.click_houseEdit()
          sleep(1)
          self.click_divConfirm()
          sleep(1)
     '''
     查看房间
     '''
     def look_house(self,code):
          sleep(1)
          self.get_srechdData(4, code)
          sleep(1)
          self.click_houseLook()
          sleep(1)

     '''
     查看业主管理
     '''
     def look_houseOwner(self,code):
          self.look_house(code)
          sleep(1)
          self.click_houseOwner()
          sleep(1)
          self.click_divCancel()
          sleep(1)
          self.click_pageDetails()
          sleep(1)
     '''
     查看成员管理
     '''
     def look_houseMember(self,code):
          self.look_house(code)
          sleep(1)
          self.click_houseMember()
          sleep(1)
          self.click_houseBtnMember()
          sleep(1)
          self.click_divCancel()
          sleep(1)
     '''
     删除房间
     '''
     def delete_house(self,code):
          sleep(1)
          self.get_srechdData(4, code)
          sleep(1)
          self.click_houseDelete()
          sleep(1)
          self.click_queRenDelete()
          sleep(1)

     '''
     添加单元
     '''
     def add_unit(self,lyname,unitName,code):
          self.look_louYu(2, lyname)
          sleep(1)
          self.click_louYuXiaJi()
          sleep(1)
          self.click_unitAdd()
          sleep(1)
          self.sendkey_unitName(unitName)
          sleep(1)
          self.sendkey_unitCode(code)
          sleep(1)
          self.click_divConfirm()
          sleep(1)
     '''
     编辑单元,name单元名称
     '''
     def edit_unit(self,name):
          sleep(1)
          self.get_treeSerch(name)
          sleep(1)
          self.click_unitEdit()
          sleep(1)
          self.click_divConfirm()
          sleep(1)
     '''
     删除单元
     '''
     def delete_unit(self,name):
          sleep(1)
          self.get_treeSerch(name)
          sleep(1)
          self.click_unitDelete()
          sleep(1)
          self.click_queRenDelete()
          sleep(1)
     '''
     添加广告位
     '''
     def add_adverising(self,lyname,code,floor):
          self.look_louYu(2, lyname)
          sleep(1)
          self.click_louYuXiaJi()
          sleep(1)
          self.click_adverisingAdd()
          sleep(1)
          self.sendkey_adverisingCode(code)
          sleep(1)
          self.sendkey_adverisingFloor(floor)
          sleep(1)
          self.click_adverisingLease()
          sleep(1)
          self.click_divConfirm()
          sleep(1)
     '''
     编辑广告位
     '''
     def edit_adverising(self,code):
          self.get_srechdData(6,code)
          sleep(1)
          self.click_adverisingEdit()
          sleep(1)
          self.click_divConfirm()
          sleep(1)

     '''
     查看广告位
     '''
     def look_adverising(self,code):
          self.get_srechdData(6, code)
          sleep(1)
          self.click_adverisingLook()
          sleep(1)

     '''
     删除广告位
     '''
     def delete_adverising(self,code):
          self.get_srechdData(6, code)
          sleep(1)
          self.click_adverisingDelete()
          sleep(1)
          self.click_queRenDelete()
          sleep(1)
     '''
     添加车位
     name 停车场的名称，可以为null
     code 车位编号
     area 车位面积
     '''
     def add_parkingLot(self,name,code,area):
          self.look_carParking(3,name)
          sleep(1)
          self.click_parkingLotAdd()
          sleep(1)
          self.sendkey_parkingLotCode(code)
          sleep(1)
          self.sendkey_parkingLotArea(area)
          sleep(1)
          self.click_divConfirm()
          sleep(1)
     '''
     编辑车位
     '''
     def edit_parkingLot(self,code):
          self.get_srechdData(5,code)
          sleep(1)
          self.click_parkingLotEdit()
          sleep(1)
          self.click_divConfirm()
          sleep(1)

     '''
     查看车位
     '''
     def look_parkingLot(self,code):
          self.get_srechdData(5,code)
          sleep(1)
          self.click_parkingLotLook()
          sleep(1)
     '''
     车位绑定业主
     '''
     def binding_parkingLot(self,code):
          self.get_srechdData(5,code)
          sleep(1)
          self.click_parkingLotOwern()
          sleep(1)
          self.click_divCancel()
          sleep(1)

     '''
     删除车位
     '''
     def delete_parkingLot(self,code):
          self.get_srechdData(5, code)
          sleep(1)
          self.click_parkingLotDelete()
          sleep(1)
          self.click_queRenDelete()
          sleep(1)


















