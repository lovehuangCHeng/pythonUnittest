#coding=utf-8
from page import BaseDriver

class LoginPage(BaseDriver.BascPage):
     def __init__(self,driver):
          super(LoginPage,self).__init__(driver)
     '''
     获取用户名输入框，并输入值
     '''
     def senkeys_user(self,username):
          self.sendkeys("用户名",username)
     '''
     获取密码输入框，并输入值
     '''
     def sendkeys_password(self,password):
          self.sendkeys("密码",password)
     '''
     获取登录按钮，并点击登录
     '''
     def click_logbutton(self):
          self.click("loginbutton")
     '''
          登录的方法
      '''
     def login(self, username, password,assertkey,assertEle):
          self.senkeys_user(username)
          self.sendkeys_password(password)
          self.click_logbutton()
          self.assertTure(assertkey,assertEle)
