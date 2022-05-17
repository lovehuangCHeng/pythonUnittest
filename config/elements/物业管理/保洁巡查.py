# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index


'''
下面模块通用的定位方式
'''
导出Excel="//button/span[text()='导出Excel']"
搜索框="//input[@placeholder='搜索...']"
搜索按钮="//span[@class='ant-input-suffix']/i"
高级搜索="//a[@class='seniorSearchBtn']"
高级搜索按钮="//div[@class='ant-card-body']//button[2]"
确认删除="//div[@class='ant-popover-buttons']/button[2]"

	
'''
固定资产

'''

新建资产="//div[@class='ant-col ant-col-16']/button[1]"
园区名称="id=regionId"
园区名称数据选择="//ul[@role='listbox']/li[1]"
资产编号="id=assetNumber"
资产名称="id=assetName"
资产保存="//div[@class='ant-modal-content']/div[3]//button[2]"
资产编辑="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[1]"
资产删除="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[2]"
资产查看="//tbody/tr[1]/td[2]//a"

'''
保洁巡查
'''
####保洁计划#####
新建计划="//div[@class='ant-col ant-col-16']/button"
管理区="id=organizationItemId"
管理区数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][1]//ul[@role='listbox']/li[1]"
计划名称="id=name"
巡查地点="id=patrolPlace"
巡查次数="id=times"
巡更频率="id=frequency"
巡更频率数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
经办人="id=staffId"
经办人数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
保洁计划查看="//tbody/tr[1]/td[2]//a"
##//div[@class='ant-calendar-date-panel']/div[1]//tbody/tr[1]/td[1]#
保洁计划启用="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/span/a[2]"
计划开始时间="//div[@class='ant-modal-content']//tbody/tr/td[2]/span/input"
输入开始时间="//div[@class='ant-time-picker-panel-input-wrap']/input"
计划结束时间="//div[@class='ant-modal-content']//tbody/tr/td[3]/span/input"
输入结束时间="//div[@class='ant-time-picker-panel-input-wrap']/input"
##未启用的状态##
保洁计划删除="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/span/a[1]"
保洁计划复制="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[2]"
##已启用状态##
保洁计划编辑="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[1]"
保洁计划停用="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[2]"
状态="id=status"
已停用="//li[text()='已停用']"
######################################
##保洁任务###
管理区_任务="id=regionIds"
管理区_任务数据="//ul[@role='listbox']/li[1]"
未开始状态="//span[text()='未开始']"
待处理状态="//span[text()='待处理']"
处理中状态="//span[text()='处理中']"
已过期状态="//span[text()='已过期']"
正常完成状态="//span[text()='正常完成']"
超时完成状态="//span[text()='超时完成']"
保洁任务查看="//tbody/tr[1]/td[2]//a"
保洁任务删除="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a"
更多="//a[text()='更多 ']"
任务查询="//div[@style='text-align: right;']/button[1]"
断言巡查地点="//tbody/tr[1]/td[4]"
断言状态="//tbody/tr[1]/td[9]"
计划时间="//span[@id='planStartTime']/span"
######################################
##保洁问题列表###
问题查询="//span[@class='ant-form-item-children']/button[2]"
已解决状态="//span[text()='已解决']"
未解决状态="//span[text()='未解决']"
全部="//span[text()='全部']"
提交日期="//span[@id='createdDate']/span"
开始时间="//div[@class='ant-calendar-date-panel']/div[1]//tbody/tr[1]/td[1]"
结束时间="//div[@class='ant-calendar-date-panel']/div[1]//tbody/tr[last()]/td[last()]"

