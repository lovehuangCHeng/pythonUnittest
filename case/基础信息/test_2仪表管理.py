# coding=utf-8
import unittest
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

from handle.基础信息.仪表管理 import YiBiaoTypeHandle as ly
from time import sleep


class Test_BascinfoCase(unittest.TestCase):
    url = ly.url_YiBiaoType
    lp = ly()

    @classmethod
    def setUpClass(cls):
        cls.lp.geturl(cls.url)
        cls.lp.setCookie()
        sleep(3)
        cls.lp.geturl(cls.url)
        cls.lp.closetabl()
        cls.lp.geturl(cls.url)

    # 新增仪表类型
    def test2_add_YiBiaoType(self):
        try:
            self.lp.YiBiaoType_delete("测试水表勿动")
        except:
            print("删除数据成功")
        self.lp.YiBiaoType_add("测试水表勿动", "吨")
        sleep(1)
        self.lp.assert_YiBiaoType_newSucc("创建仪表类型成功！")


    # 查询仪表类型
    def test2_secrch_YiBiaoType(self):
        self.lp.YiBiaoType_secrch("测试水表勿动")
        self.lp.assert_YiBiaoType_name("测试水表勿动")

    # 高级查询仪表类型
    def test2_sennior_secrch_YiBiaoType(self):
        self.lp.YiBiaoType_sennior_secrch("测试水表勿动")
        self.lp.assert_YiBiaoType_name("测试水表勿动")


    # 编辑仪表类型
    def test2_edit_YiBiaoType(self):
        try:
            self.lp.YiBiaoType_edit("测试水表勿动")
        except:
            print("编辑失败")
        sleep(1)
        self.lp.assert_YiBiaoType_saveSucc("更新仪表成功！")


    @classmethod
    def tearDownClass(cls):
        cls.lp.quet()
