from util import utils
from config.elements.基础信息 import 客户管理 as kh
from config.elements import  geturl
class khgl(utils.BascUtils):
    pass
    '''
    客户档案 
    '''
    # 点击新增
    def click_khadd(self):
        self.click(kh.客户新建)

    '''
        委员会成员 
    '''