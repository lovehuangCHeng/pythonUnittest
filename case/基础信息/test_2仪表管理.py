# coding=utf-8
import unittest
from handle.基础信息.仪表管理 import YiBiaoTypeHandle as ly
from time import sleep

class Test_BascinfoCase(unittest.TestCase):
    url = ly.url_YiBiaoType
    lp = ly()
    meterTypeName = '测试水表勿动'
    @classmethod
    def setUpClass(cls):
        cls.lp.login_By_Cookies(cls.url)


    # 新增仪表类型
    def test1_add_YiBiaoType(self):
        try:
            self.lp.YiBiaoType_delete(self.meterTypeName)
        except:
            print("删除数据成功")
        self.lp.YiBiaoType_add(self.meterTypeName, "吨")
        sleep(1)
        self.lp.assert_YiBiaoType_newSucc("创建仪表类型成功！")


    # 查询仪表类型
    def test2_secrch_YiBiaoType(self):
        self.lp.YiBiaoType_secrch(self.meterTypeName)
        self.lp.assert_YiBiaoType_name(self.meterTypeName)

    # 高级查询仪表类型
    def test4_sennior_secrch_YiBiaoType(self):
        self.lp.YiBiaoType_sennior_secrch(self.meterTypeName)
        self.lp.assert_YiBiaoType_name(self.meterTypeName)

    # 编辑仪表类型
    def test3_edit_YiBiaoType(self):
        try:
            self.lp.YiBiaoType_edit(self.meterTypeName)
        except:
            print("编辑失败")
        sleep(1)
        self.lp.assert_YiBiaoType_saveSucc("更新仪表成功！")


    @classmethod
    def tearDownClass(cls):
        cls.lp.quet()
