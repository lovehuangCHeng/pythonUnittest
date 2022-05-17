# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index


'''
下面模块通用的定位方式
'''
搜索框="//input[@placeholder='搜索...']"
搜索按钮="//span[@class='ant-input-suffix']/i"
保存="//div[@class='ant-modal-footer']//button[2]"
确认删除="//div[@class='ant-popover-buttons']/button[2]"
导入Excel="//button/span[text()='导入Excel']"
下载模板="//button/span[text()='下载模板']"
高级搜索="//a[@class='seniorSearchBtn']"
高级搜索按钮="//div[@class='ant-card-body']//button[2]"
'''
巡更点
'''
新建巡更点="//button/span[text()='新建巡更点']/.."
编辑巡更点="//tbody/tr[1]/td[7]//a[1]"
删除巡更点="//tbody/tr[1]/td[7]//a[2]"
作废巡更点="//tbody/tr[1]/td[7]//a[3]"
查看二维码巡更点="//tbody/tr[1]/td[7]//a[4]"
关闭二维码页面="//button[@class='ant-modal-close']"
管理区="id=organizationItemId"
管理区数据="//ul[@role='listbox']/li[1]"
巡更点名称="id=name"
巡更点编码="id=number"
检查要点="id=checkList"
签到定点自拍="//div[@id='signMethodIds']/label[1]/span[1]"
签到NFC="//div[@id='signMethodIds']/label[2]/span[1]"
签到蓝牙="//div[@id='signMethodIds']/label[3]/span[1]"

'''
巡更路线
'''
新建巡更路线="//div[@class='ant-col ant-col-16']/button[1]"
编辑巡更路线="//tbody/tr[1]/td[7]//a[1]"
删除巡更路线="//tbody/tr[1]/td[7]//a[2]"
作废巡更路线="//tbody/tr[1]/td[7]//a[3]"
查看二维码巡更路线="//tbody/tr[1]/td[7]//a[4]"
管理区_巡更路线="id=organizationItemId"
巡更路线名称="id=name"
巡更路线编码="id=number"
巡更路线备注="id=remark"
默认签到方式="id=signMethodId"
默认定点自拍="//ul[@role='listbox']/li[text()='定点自拍']"
添加巡更点="//div[@id='pointIds']/button"
选择巡更点="//div[@class='ant-modal-content']//tbody/tr[1]/td[1]"
巡更点确定="//body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]" 
			
		
		

'''
巡更计划
'''
新建巡更计划="//button/span[text()='新建巡更计划']/.."
管理区_计划="id=organizationItemId"
管理区_高级搜索="id=OrganizationItemId"
管理区_计划数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][1]//ul[@role='listbox']/li[1]"
计划名称="id=name"
巡查路线="id=patrolLineId"
巡更路线数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
巡查次数="id=times"
巡更频率="id=frequency"
经办人="id=handlers"
经办人数据="//tr[1]/td[@class='ant-table-selection-column']/span/label"
确定经办人="//body/div[5]/div/div[2]/div/div[2]/div[@class='ant-modal-footer']/button[2]"
巡更计划开始时间="//div[@class='ant-modal-content']//tbody/tr/td[2]/span/span/i"
输入开始时间="//div[@class='ant-time-picker-panel-input-wrap']/input"
巡更计划结束时间="//div[@class='ant-modal-content']//tbody/tr/td[3]/span/span/i"
输入结束时间="//div[@class='ant-time-picker-panel-input-wrap']/input"
##未启用的状态##
巡更计划查看="//tbody/tr[1]/td[2]//a"
巡更计划启用="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/span/a[2]"
巡更计划删除="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/span/a[1]"
巡更计划复制="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[2]"
##已启用状态##
巡更计划编辑="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[1]"
巡更计划停用="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[2]"
状态="id=status"
已停用="//li[text()='已停用']"

'''
巡更任务
'''
##巡更任务###
管理区_任务="id=regionIds"
管理区_任务数据="//ul[@role='listbox']/li[1]"
待分派状态="//span[text()='待分派']"
未开始状态="//span[text()='未开始']"
待处理状态="//span[text()='待处理']"
处理中状态="//span[text()='处理中']"
已过期状态="//span[text()='已过期']"
正常完成状态="//span[text()='正常完成']"
超时完成状态="//span[text()='超时完成']"
巡更任务查看="//tbody/tr[1]/td[2]//a"
###待分派状态##
巡更任务添加备注="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/span[3]/a"
添加备注信息="id=remark"
巡更任务删除="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/span[2]/a"
巡更任务分派="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/span[1]/a"
巡更人员选择框="id=staffId"
巡更人员数据="//ul[@role='listbox']/li[1]"
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





