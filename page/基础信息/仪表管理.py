from util import utils
from config.elements.基础信息 import 仪表管理 as ybgl
from config.elements import geturl


class YiBiaoPage(utils.BascUtils):
    url_YiBiaoType = geturl.仪表类型

    #    获取仪表类型-新增按钮，并点击
    def click_addYiBiaoType(self):
        self.click(ybgl.仪表类型新增)

    #    获取仪表类型-编辑按钮，并点击
    def click_editYiBiaoType(self):
        self.click(ybgl.仪表类型编辑)

    #    获取仪表类型-删除按钮，并点击
    def click_delYiBiaoType(self):
        self.click(ybgl.仪表类型删除)

    #    获取仪表类型-确认删除按钮，并点击
    def click_confirmDelYiBiaoType(self):
        self.click(ybgl.仪表类型确认删除)

    #     获取搜索输入框，并输入数据
    def sendkeys_YiBiaoType_secrch(self, text):
        self.sendkeys(ybgl.仪表类型搜索框, text)

    #    获取仪表类型-搜索按钮，并点击
    def click_YiBiaoType_secrch(self):
        self.click(ybgl.仪表类型搜索按钮)

    #     获取仪表类型-高级搜索-向下展开按钮，并点击
    def click_YiBiaoType_secrh_down(self):
        self.click(ybgl.仪表类型高级搜索)

    #     获取搜索输入框，并输入数据
    def sendkeys_YiBiaoType_secrch_senior(self, text):
        self.sendkeys(ybgl.仪表类型高级搜索框, text)

    #     获取仪表类型-高级搜索按钮，并点击
    def click_YiBiaoType_secrh_senior(self):
        self.click(ybgl.仪表类型高级搜索按钮)

    #     获取仪表类型-高级搜索-重置，并点击
    def click_YiBiaoType_secrh_Reset(self):
        self.click(ybgl.仪表类型高级重置)

    #     获取仪表类型-名称，并输入数据
    def sendkeys_add_YiBiaoType_name(self, text):
        self.sendkeys(ybgl.仪表类型名称, text)

    #     获取仪表类型-计量单位，并输入数据
    def sendkeys_add_YiBiaoType_unit(self, text):
        self.sendkeys(ybgl.计量单位, text)

    #     获取仪表类型-新增保存按钮，并点击
    def click_YiBiaoType_save(self):
        self.click(ybgl.仪表类型保存)

    '''
     断言
     '''

    # 获取仪表类型-更新仪表成功，并返回element
    def find_element_savesucc(self):
        return self.find_element(ybgl.更新仪表成功).text

    #     获取仪表类型-创建仪表成功，并返回element
    def find_element_newsucc(self):
        return self.find_element(ybgl.创建仪表成功).text

    #     获取仪表类型-删除仪表类型成功，并返回element
    def find_element_delsuss(self):
        return self.find_element(ybgl.删除仪表类型).text

    #     获取仪表类型-仪表类型名称断言，并返回element
    def find_element_YiBiaoTypename(self):
        return self.find_element(ybgl.仪表类型名称断言).text
