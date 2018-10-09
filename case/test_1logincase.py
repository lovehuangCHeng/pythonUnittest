#coding=utf-8
import unittest
from case.baseCase import BaseCase
from page.loginpage import LoginPage
class Test_LoginCase(unittest.TestCase):
     bc=BaseCase()
     driver=bc.getDriver()
     lp=LoginPage(driver)
     username = bc.readData("username")#读取用户名
     password = bc.readData("password")#读取密码
     @classmethod
     def setUp(cls):
          url = cls.bc.readUrl("loginURL")
          cls.lp.get(url)
     def test_login(self):
          self.lp.login(self.username,self.password)
          self.lp.saveCookis()
     @classmethod
     def tearDown(cls):
          cls.lp.quet()
if __name__ =="__main__":
     unittest.main()
