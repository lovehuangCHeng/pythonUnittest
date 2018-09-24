#coding=utf-8
import unittest
from case.baseCase import BaseCase
from page.loginpage import LoginPage
class LoginCase(unittest.TestCase):
     bc=BaseCase()
     driver=bc.getDriver()
     lp=LoginPage(driver)
     @classmethod
     def setUp(cls):
          url = cls.bc.readUrl("loginURL")
          cls.lp.get(url)
     def test_login(self):
          self.lp.login("admin","1234567")
          self.lp.saveCookis()
     @classmethod
     def tearDown(cls):
          cls.lp.quet()
if __name__ =="__main__":
     unittest.main()
