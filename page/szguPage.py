#coding=utf-8
from util import utils
from time import sleep
class SZGLpage(utils.BascUtils):
    '''
         获取输入框类型，为下拉框的下拉列表中的值
    '''
    def get_click_elements(self, num):
        datalist = []
        datalist = self.driver.find_elements_by_class_name("ant-select-dropdown-menu-item")
        print(datalist)
        datalist[num].click()
    #获取收支管理按钮
    def click_szgl(self):
        self.click("szgu")
    #获取收支科目
    def click_szku(self):
        self.click("szkm")
    # 获取新建按钮
    def click_szkmnew(self):
        self.click("szkmnew")
    #收支科目名称
    def send_szkmname(self,value):
        self.sendkeys("szkmname",value)
    #收支类型
    def click_szkmtype(self,num):
        sleep(1)
        self.click("szkmtype")
        sleep(2)
        self.get_click_elements(num)
    #确认按钮
    def click_szkmcomfire(self):
        self.click("szkmcomfire")
    def click_szkmcomfireedut(self):
        self.click("szkmcomfireedit")
    #获取message信息
    def get_message(self):
        element=self.get_element("szkmmessage").text
        return  element
    #收支科目获取搜索框
    def send_szkmselectinput(self,value):
        self.sendkeys("szkmselectinput",value)
    #收支科目获取搜索按钮
    def click_szkmselectbnt(self):
        self.click("szkmselectbnt")
    #收支科目删除按钮
    def click_delszkm(self):
        self.click("szkmdel")
    #收支科目删除确认按钮
    def click_delcofnszkm(self):
        self.click("szkmdelcomfire")
    #收支科目编辑按钮
    def click_editszkm(self):
        self.click("szkmedit")