# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index
		
'''
活动管理

'''
###活动列表####
新建活动="//button[@class='ant-btn ant-btn-primary']"
编辑活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[2]"
查看活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[1]"
发布活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[4]"
删除活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[3]"
下线活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[2]"
搜索活动框="//input[@placeholder='搜索...']"
搜索活动按钮="//div[@style='float: right;']/span/span"
活动类别="//div[@id='category']//div[@class='ant-select-selection__rendered']"
活动类别数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][1]//div[@role='listbox']/div[1]"
活动类别添加="//li[text()='+ 添加']"
活动类别名称="//input[@id='category']"
活动类别保存="//body/div[4]//div[@class='ant-modal-content']/div[3]//button[2]"
发送范围="//div[@id='regions']//div[@class='ant-select-selection__rendered']"
发送范围数据选择="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//div[@role='listbox']/div[2]"
活动主题="id=title"
活动简介="id=introInfo"
活动地址="id=address"
活动内容="//div[@contenteditable='true']"
活动时间="id=campaignRangeTime"
活动报名时间="id=registrationRangeTime"
开始时间="//div[@class='ant-calendar-date-panel']/div[1]//tbody/tr[1]/td[1]"
结束时间="//div[@class='ant-calendar-date-panel']/div[1]//tbody/tr[last()]/td[last()]"
活动保存="//div[@class='ant-modal-content']/div[3]//button[2]"
查看页面取消="xpath=//button/span[text()='取 消']"
###报名结果##
导出Excel="//button/span[text()='导出Excel']"
确认删除按钮="//div[@class='ant-popover-buttons']/button[2]"
'''
人事管理
'''
###考勤管理###


###排班设置###
排班新建="//div[@class='ant-tabs-content ant-tabs-content-top']//div[@role='tabpanel'and @aria-hidden='false']/div/div/button"
分组新建="//div[@class='ant-tabs-content ant-tabs-content-top']//div[@role='tabpanel'and @aria-hidden='false']/div/div/button"
班次名称="id=className"
编辑班次="//tbody/tr/td[5]//a[1]"
日历管理="//div[@role='tab'and text()='日历管理']"
周期管理="//div[@role='tab'and text()='周期管理']"
排班分组="//div[@role='tab'and text()='排班分组']"
日历名称="id=name"
编辑日历="//div[@class='ant-row']/div[1]//li[1]/span/a[text()='编辑']"
周期名称="id=cycleName"
第一天="//input[@id='flight1']"
第二天="//input[@id='flight2']"
每天的值="//div[text()='假']"
第二天的值="//div[@id='flight2_list']/..//div[@title='白班']/div"
班组名称="//div[@class='ant-modal-content']//input[@id='groupName']"
排班周期="//input[@id='cycle']"  
排班周期的值="//div[@id='cycle_list']/..//div[text()='两天计划']"      
排班日历="//input[@id='calendar']"
排班日历的值="//div[@id='calendar_list']/..//div[text()='周末双休']" 
班组员工="//div[@class='ant-select-selection-overflow']"
班组员工数据="//div[@class='ant-select-tree-list-holder-inner']/div[1]/span[4]/span"
预设班次="//tbody//td[@newgroup='[object Object]'][2]"
排班分组编辑="//tbody/tr[1]/td[6]//a[1]"
排班分组查看="//tbody/tr[1]/td[1]//a"
自动排班="//button/span[text()='自动排班']"

'''
考勤管理
'''
考勤新建="//div/span[1]/button"
职员姓名="id=name"
考勤列表数据="//tbody/tr[1]/td[1]"
职员性别="//div[@id='sex']/label[1]/span[@class='ant-radio']"
职员导出="//button/span[text()='导 出']"
职员搜索框="//input[@placeholder='搜索...']"
职员搜索按钮="//span[@class='ant-input-group-addon']/button"
职员查看="//tbody/tr[2]/td/span/a[text()='查看']"
职员查看页面返回="//button/span[text()='返 回']"
职员添加="//tbody/tr[2]/td/span//a[text()='添加']"
考勤类型="id=Type"
出差="//div[text()='出差']"
小时="id=hours"
职员查看页面删除="//tbody/tr[1]/td[10]/span/a"
职员查看页面编辑="//tbody/tr[1]/td[10]/span/span/a"
考勤管理高级搜索="//a[@class='seniorSearchBtn']"
职员名称="id=staffName"
高级搜索按钮="//div[@class='ant-card-body']//button[2]"


