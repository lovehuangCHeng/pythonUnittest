from page.基础信息 import 仪表管理 as ybgl
from time import sleep


class YiBiaoTypeHandle(ybgl.YiBiaoPage):
    # 新建仪表类型
    def YiBiaoType_add(self, name, unit):
        self.click_addYiBiaoType()
        sleep(1)
        self.sendkeys_add_YiBiaoType_name(name)
        sleep(1)
        self.sendkeys_add_YiBiaoType_unit(unit)
        sleep(1)
        self.click_YiBiaoType_save()
        sleep(1)

    # 编辑仪表
    def YiBiaoType_edit(self, value):
        sleep(1)
        self.sendkeys_YiBiaoType_secrch(value)
        sleep(1)
        self.click_editYiBiaoType()
        sleep(1)
        self.click_YiBiaoType_save()
        sleep(1)

    # 查询仪表
    def YiBiaoType_secrch(self, value):
        sleep(1)
        self.sendkeys_YiBiaoType_secrch(value)
        sleep(1)
        self.click_YiBiaoType_secrch()
        sleep(1)

    # 高级搜索仪表
    def YiBiaoType_sennior_secrch(self, value):
        sleep(1)
        self.click_YiBiaoType_secrh_down()
        sleep(1)
        self.click_YiBiaoType_secrh_Reset()
        sleep(1)
        self.sendkeys_YiBiaoType_secrch_senior(value)
        sleep(1)
        self.click_YiBiaoType_secrh_senior()
        sleep(1)


    # 删除仪表
    def YiBiaoType_delete(self, value):
        self.YiBiaoType_secrch(value)
        sleep(1)
        # self.click_KeHu_table_input()
        # sleep(1)
        self.click_delYiBiaoType()
        sleep(1)
        self.click_confirmDelYiBiaoType()
        sleep(1)

    # 断言保存成功
    def assert_YiBiaoType_saveSucc(self, excptvalue):
        assert excptvalue in self.find_element_savesucc()

    # 断言新增成功
    def assert_YiBiaoType_newSucc(self, excptvalue):
        assert excptvalue in self.find_element_newsucc()


    # 断言删除成功
    def assert_YiBiaoType_delSucc(self, excptvalue):
        assert excptvalue in self.find_element_delsuss()

    # 断言客户存在这个名称
    def assert_YiBiaoType_name(self, excptvalue):
        assert excptvalue in self.find_element_YiBiaoTypename()
