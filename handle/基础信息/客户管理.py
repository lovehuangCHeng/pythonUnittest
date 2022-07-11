from page.基础信息 import 客户档案 as khda
from  time import  sleep
class kuHuHandle(khda.KuHuPage):
    #新建客户
    def kehu_add(self,name,phone):
        self.click_addKeHu()
        sleep(1)
        self.click_add_kehu_region()
        sleep(1)
        self.click_add_kehu_regiondata()
        sleep(1)
        self.sendkeys_add_kehu_name(name)
        sleep(1)
        self.sendkeys_add_kehu_phone(phone)
        sleep(1)
        self.click_addKeHu_save()
        sleep(1)

    # 编辑客户
    def kehu_edit(self,value):
        sleep(1)
        self.kehu_secrch(value)
        sleep(1)
        self.click_editKeHu()
        sleep(1)
        self.click_addKeHu_save()
        sleep(1)

    # 查询客户
    def kehu_secrch(self,value):
        sleep(1)
        self.sendkeys_Kehu_secrch(value)
        sleep(1)
        self.click_KeHu_secrch()
        sleep(1)

    # 合并重名客户
    def kehu_meger(self):
        sleep(1)
        self.click_mergeKeHu()
        sleep(1)
        self.find_element_megertitle()
        sleep(1)
        self.click_megerKeHu_close()
        sleep(1)

    # 高级搜索客户
    def kehu_sennior_secrch(self):
        sleep(1)
        self.click_KeHu_secrh_down()
        sleep(1)
        self.click_KeHu_secrh_senior()
        sleep(1)
        self.click_KeHu_secrh_Reset()
        sleep(1)
        self.click_KeHu_secrh_up()
        sleep(1)

    # 删除客户
    def kehu_delete(self,value):
        self.kehu_secrch(value)
        sleep(1)
        self.click_KeHu_table_input()
        sleep(1)
        self.click_delKeHu()
        sleep(1)
        self.click_delKeHu_confirm()
        sleep(1)
    #断言保存成功
    def assert_kehu_saveSucc(self,excptvalue):
        assert excptvalue in self.find_element_savesucc()
    # 断言删除成功
    def assert_kehu_delSucc(self,excptvalue):
            assert  excptvalue in self.find_element_delsuss()
    # 断言客户存在这个名称
    def assert_kehu_name(self,excptvalue):
            assert excptvalue in self.find_element_kehuname()