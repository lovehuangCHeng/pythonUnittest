#coding=utf-8
import unittest
from case.baseCase import BaseCase
from page.loginpage import LoginPage
import pytest
import allure

@allure.feature('登录模块')
class Test_LoginCase(unittest.TestCase):
     bc=BaseCase()
     driver=bc.getDriver()
     lp=LoginPage(driver)
     url = bc.readUrl("loginURL")  # 获取登录URL地址
     username = bc.readData("用户名")#读取用户名
     password = bc.readData("密码")#读取密码
     @classmethod
     def setUp(cls):
          cls.lp.get(cls.url)
     def test_login(self):
          try:
               self.lp.login(self.username,self.password)
               self.lp.assertTure('asserloginpass','祝你开心')
               self.lp.saveCookis()
          except:
               print("登录失败")
     @classmethod
     def tearDown(cls):
          cls.lp.quet()
if __name__ =="__main__":
     pytest.main(['-s', '-q', '--alluredir', './report/xml'])
