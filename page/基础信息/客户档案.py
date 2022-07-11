from util import utils
from config.elements.基础信息 import 客户管理 as khgl
from config.elements import  geturl
class KuHuPage(utils.BascUtils):
     url_kehudangan = geturl.客户档案

     # 获取客户档案-新增按钮，并点击
     def click_addKeHu(self):
          self.click(khgl.客户新建)

     #    获取客户档案-编辑按钮，并点击
     def click_editKeHu(self):
          self.click(khgl.客户编辑)

     #    获取客户档案-删除按钮，并点击
     def click_delKeHu(self):
          self.click(khgl.客户删除)

     #     获取客户档案-合并重名钮，并点击
     def click_mergeKeHu(self):
          self.click(khgl.合并重名客户)

     #     获取客户档案-导出excel，并点击
     def click_excelKeHu(self):
          self.click(khgl.客户档案导出Excel)

     #     获取搜索输入框，并输入数据
     def sendkeys_Kehu_secrch(self, text):
          self.sendkeys(khgl.客户档案搜索框, text)

     #    获取客户档案-搜索按钮，并点击
     def click_KeHu_secrch(self):
          self.click(khgl.客户档案搜索按钮)

     #     获取客户档案-高级搜索-向下展开按钮，并点击
     def click_KeHu_secrh_down(self):
          self.click(khgl.客户向下展开按钮)

     #    获取客户档案-高级搜索-向上折叠，并点击
     def click_KeHu_secrh_up(self):
          self.click(khgl.客户向上展开按钮)

     #     获取客户档案-高级搜索按钮，并点击
     def click_KeHu_secrh_senior(self):
          self.click(khgl.高级搜索按钮)

     #     获取客户档案-高级搜索-重置，并点击
     def click_KeHu_secrh_Reset(self):
          self.click(khgl.高级搜索重置)

     #     获取新建-点击管理区下拉框，并点击
     def click_add_kehu_region(self):
          self.click(khgl.新建_选择管理区)

     #     获取新建-点击管理区下拉框,选择数据，并点击
     def click_add_kehu_regiondata(self):
          self.click(khgl.新建_管理区数据)

     #     获取客户名称输入框，并输入数据
     def sendkeys_add_kehu_name(self, text):
          self.sendkeys(khgl.新建_客户名称, text)

     #     获取电话号码，并输入数据
     def sendkeys_add_kehu_phone(self, text):
          self.sendkeys(khgl.新建_电话号码, text)

     #     获取客户档案-新增保存按钮，并点击
     def click_addKeHu_save(self):
          self.click(khgl.新建_客户档案保存)

     #     获取客户档案-表单中复选框，并点击
     def click_KeHu_table_input(self):
          self.click(khgl.表格中管理区数据)

     #     获取客户档案-确认删除按钮，并点击
     def click_delKeHu_confirm(self):
          self.click(khgl.确认删除按钮)

     #     获取客户档案-关闭合并同名客户，并点击
     def click_megerKeHu_close(self):
          self.click(khgl.关闭合并同名客户)

     #     获取客户档案-知道了，并点击
     def click_knowe(self):
          self.click(khgl.知道了)

     '''
     断言
     '''
     # 获取客户档案-保存成功，并返回element
     def find_element_savesucc(self):
          return  self.find_element(khgl.客户档案断言).text

     #     获取客户档案-客户名称断言，并返回element
     def find_element_kehuname(self):
          return self.find_element(khgl.客户名称断言).text

     #     获取 -删除成功，并返回element
     def find_element_delsuss(self):
          return self.find_element(khgl.删除成功).text

     #     获取-合并同名客户title，并返回element
     def find_element_megertitle(self):
          return self.find_element(khgl.合并同名客户title)