#coding=utf-8
from util import utils
from config.elements.基础信息 import 房产档案 as fl
from config.elements import  geturl
class LoginPage(utils.BascUtils):
     '''
     获取用户名输入框，并输入值
     '''
     def senkeys_user(self,username):
          self.sendkeys(fl.用户名,username)
     '''
     获取密码输入框，并输入值
     '''
     def sendkeys_password(self,password):
          self.sendkeys(fl.密码,password)
     '''
     获取登录按钮，并点击登录
     '''
     def click_logbutton(self):
          self.click(fl.立即登录)
     '''
          登录的方法
      '''
     def login(self,username,password):
          # self.geturl(geturl.首页)
          self.senkeys_user(username)
          self.sendkeys_password(password)
          self.click_logbutton()
          self.closetabl(fl.提示框关闭)

# loginPage =LoginPage()
# loginPage.login('testing','123456')