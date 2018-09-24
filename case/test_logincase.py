#coding=utf-8
import unittest
from case import baseCase
from page import loginpage
class LoginCase(baseCase.BaseCase,unittest.TestCase):
     bc=baseCase.BaseCase()
     driver=bc.getDriver()
     lp=loginpage.LoginPage(driver)
     @classmethod
     def setUp(cls):
          url=cls.bc.readUrl("loginURL")
          cls.lp.get(url)
     def test_login(self):
          self.lp.login("admin","1234567")
          self.lp.saveCookis()
     @classmethod
     def tearDown(cls):
          cls.lp.quet()
if __name__ =="__main__":
     unittest.main()
