from util import utils
from config.elements.OA系统 import OAXpath as oa
from config.elements import  geturl
class LoginPage(utils.BascUtils):
     url_ggao=geturl.公告管理
     url_dbsx = geturl.待办事项
     url_wdlb = geturl.文档类别管理
     url_wdzl = geturl.文档资料管理
     url_hyjl = geturl.会议记录
     url_hylb = geturl.会议类别管理
     url_gzjh = geturl.工作计划
     url_jhlb = geturl.计划类别管理
     '''
          获取新建公告按钮按钮，并点击
     '''
     def click_addggao(self):
          self.click(oa.新建公告按钮)
     '''
          获取公告类别输入框按钮，并点击
     '''
     def click_addggao_lb(self):
          self.click(oa.公告类别输入框)
     '''
          获取新建公告按钮按钮，并点击
     '''
     def click_logbutton(self):
          self.click(oa.新建公告按钮)

     '''
          获取 公告类别输入框，并输入值
     '''
     def sendkeys_password(self, text):
          self.sendkeys(oa.公告类别输入框, text)