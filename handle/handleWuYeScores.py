#coding=utf-8
from page import wuyesorcesPage,szguPage
from time import sleep

class louyu(wuyesorcesPage.BascinfoPage):
     def __init__(self,driver):
          super(louyu,self).__init__(driver)
     '''
     重新加载url
     '''
     def switch_url(self,url):
          self.switch_default()
          sleep(2)
          self.get(url)
          sleep(2)
          self.switch_fram("iframe")
     '''
     物业资源管理树，搜索当前查询的数据，并点击这个查找的数据。
     '''
     def get_treeSerch(self,value):
          sleep(2)
          self.sendkeys_wuYeTree(value)
          sleep(2)
          self.click_wuYeSerch()
          sleep(2)
          self.click_guanLiQuTree()
          sleep(2)
     '''
     物业资源管理，6个列表中查询数据
     '''
     def get_srechdData(self,num,value):
          sleep(2)
          self.refresh()
          sleep(2)
          self.click_sixTab(num)
          sleep(2)
          self.sendkeys_serch(value)
          sleep(2)
          self.click_serch()
          sleep(2)
     '''
     导出Excel
     '''
     def excport_excle(self,num):
          sleep(2)
          self.click_sixTab(num)
          sleep(2)
          self.click_expotExcle()
          sleep(2)

     '''
     新建分组
     '''
     def add_fenZu(self,name,address,mark):
          sleep(2)
          self.click_xiaJiJigou()
          sleep(2)
          self.click_fenZu()
          sleep(2)
          self.sendkey_fenZuName(name)
          sleep(2)
          self.sendkey_fenZuDiZhi(address)
          sleep(2)
          self.sendkey_fenZuMark(mark)
          sleep(2)
          self.click_divConfirm()
          sleep(2)

     '''
     编辑分组
     '''
     def edit_fenZu(self,fenzu):
          sleep(2)
          self.get_treeSerch(fenzu)
          sleep(2)
          self.click_fenZuEdit()
          sleep(2)
          self.click_divConfirm()
          sleep(2)
     '''
     删除分组
     '''
     def delete_fenZu(self,fenzu):
          sleep(2)
          self.get_treeSerch(fenzu)
          sleep(2)
          self.click_fuZuDelete()
          sleep(2)
          self.click_queRenDelete()

     '''
     新建楼宇
     '''
     def add_louYu(self,name,floor,code,mark):
          sleep(2)
          self.click_xiaJiJigou()
          sleep(2)
          self.click_louYu()
          sleep(2)
          self.sendkey_louYuName(name)
          sleep(2)
          self.sendkey_louYuFloor(floor)
          sleep(2)
          self.sendkey_louYuCode(code)
          sleep(2)
          self.sendkey_louYuMark(mark)
          sleep(2)
          self.click_divConfirm()
          sleep(2)

     '''
     编辑楼宇, @prams  name 楼宇名称
     '''
     def edit_louYu(self,num,name):
          sleep(2)
          self.get_srechdData(num,name)
          sleep(2)
          self.click_louYuEdit()
          sleep(2)
          self.click_divConfirm()
          sleep(2)

     '''
     查看楼宇 name 楼宇名称
     '''
     def look_louYu(self,num,name):
          sleep(2)
          self.get_srechdData(num,name)
          sleep(2)
          self.click_louYuLook()
          sleep(2)
     '''
     删除楼宇 name 楼宇名称
     '''
     def delete_louYu(self,num,name):
          sleep(2)
          self.get_srechdData(num,name)
          sleep(2)
          self.click_louYuDelete()
          sleep(2)
          self.click_queRenDelete()
          sleep(2)
     '''
     添加停车场
     '''
     def add_carParking(self,name,address,mark):
          sleep(2)
          self.click_xiaJiJigou()
          sleep(2)
          self.click_tingCheChang()
          sleep(2)
          self.sendkey_tingCheChangName(name)
          sleep(2)
          self.sendkey_tingCheChangAddress(address)
          sleep(2)
          self.sendkey_tingCheChangMark(mark)
          sleep(2)
          self.click_divConfirm()
          sleep(2)
     '''
     编辑停车场
     '''
     def edit_caiParking(self,num,name):
          sleep(2)
          self.get_srechdData(num,name)
          sleep(2)
          self.click_editTingCheChang()
          sleep(2)
          self.click_divConfirm()
          sleep(2)

     '''
     查看停车场
     '''
     def look_carParking(self,num,name):
          sleep(2)
          self.get_srechdData(num,name)
          sleep(2)
          self.click_lookTingCheChang()
          sleep(2)
     '''
     删除停车场
     '''
     def delete_carParking(self,num,name):
          sleep(2)
          self.get_srechdData(num,name)
          sleep(2)
          self.click_deleteTingCheChang()
          sleep(2)
          self.click_queRenDelete()
          sleep(2)
     '''
     添加房间
     '''



















