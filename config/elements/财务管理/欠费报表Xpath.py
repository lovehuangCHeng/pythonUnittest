# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index

    def __str__(self):
        return '<MyObject%s>' % self.index


账号输入框="//input[@type='text']"
密码输入框="//input[@type='password']"
##########欠费按时长分阶统计##########
欠费按时长分阶统计_费用时段="//span[@id='time']"
欠费按时长分阶统计_费用时段_开始="//tr[1]/td[@role='gridcell' and @class='ant-calendar-cell'][1]"
欠费按时长分阶统计_管理区="//div[@id='regionIds']"
欠费按时长分阶统计_选择管理区="//body/div[3]//ul/li[1]"
欠费按时长分阶统计_收费项目="//div[@id='chargeItemTypeIds']"
欠费按时长分阶统计_选择收费项目="//body/div[4]//ul/li[1]"
欠费按时长分阶统计_搜索="//button/span[text()='搜 索']/.."
欠费按时长分阶统计_重置="//button/span[text()='重 置']/.."
欠费按时长分阶统计_导出="//button/span[text()='导出Excel']/.."
欠费按时长分阶统计_表格="//table"
##########欠费按金额分阶统计##########
欠费按金额分阶统计_费用时段="//span[@id='time']"
欠费按金额分阶统计_费用时段_开始="//div[@class='ant-calendar-range-part ant-calendar-range-left']//tr[1]/td[1]"
欠费按金额分阶统计_费用时段_结束="//div[@class='ant-calendar-range-part ant-calendar-range-right']//tr[last()]/td[last()]"
欠费按金额分阶统计_管理区="//div[@id='regionIds']"
欠费按金额分阶统计_选择管理区="//body/div[3]//ul/li[1]"
欠费按金额分阶统计_收费项目="//div[@id='chargeItemTypeIds']"
欠费按金额分阶统计_选择收费项目="//body/div[4]//ul/li[1]"
欠费按金额分阶统计_楼宇停车场="//div[@id='organizationItemIds']"
欠费按金额分阶统计_选择楼宇停车场="//body/div[5]//ul/li[1]"
欠费按金额分阶统计_搜索="//form/div[1]//div/button[1]"
欠费按金额分阶统计_重置="//form/div[1]//div/button[2]"
欠费按金额分阶统计_导出="//form/parent::div/preceding-sibling::div/button"
欠费按金额分阶统计_表格="//table"