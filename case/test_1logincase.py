#coding=utf-8
import unittest
from page.loginpage import LoginPage
from config.elements import  geturl
from time import  sleep
class test_LoginCase(unittest.TestCase):
     lp=LoginPage()
     url = geturl.首页  # 获取登录URL地址
     username = lp.readData("lognUser")#读取用户名
     password = lp.readData("lognPassword")#读取密码
     @classmethod
     def setUp(cls):
          cls.lp.geturl(cls.url)

     def test_login(self):
          self.lp.login(self.username,self.password)
          sleep(2)
          #self.lp.assertTure('asserloginpass','祝你开心')
          self.lp.saveCookis()

     @classmethod
     def tearDown(cls):
          sleep(2)
          cls.lp.quet()

