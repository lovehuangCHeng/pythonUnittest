# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index

    def __str__(self):
        return '<MyObject%s>' % self.index


账号输入框 = "//input[@type='text']"
密码输入框 = "//input[@type='password']"
##########应收年度统计##########
应收年度统计_应收时间段选择框 = "//input[@id='dateRange']"
应收年度统计_应收时间段选择上个月 = "//div[@class='ranges']/ul/li[2]"
应收年度统计_汇总到楼宇勾选框 = "//input[@id='BuildingName']/.."
应收年度统计_所有管理区展开 = "//span[@class='k-icon k-i-arrow-e']"
应收年度统计_所有楼宇展开 = "//tbody/tr[1]/td[3]/span[1]"
应收年度统计_一个列表金额 = "//tbody/tr[1]/td[1]/a"
应收年度统计_跳转页面title验证="//div[@class='page-bar']/ul/li[2]/a"
应收年度统计_汇总到收费项目勾选框 = "//input[@id='ChargeItemTypeName']"
应收年度统计_所有月份展开 = "//tbody/tr[1]/th[1]/span[1]"
应收年度统计_所有项目展开="//tbody/tr[3]/th[1]/span[1]"
应收年度统计_导出按钮 = "//button[@id='btnExport']"
##########欠费年度统计##########
欠费年度统计_应收时间段选择框 = "//input[@id='dateRange']"
欠费年度统计_应收时间段选择上个月 = "//div[@class='ranges']/ul/li[2]"
欠费年度统计_所有管理区展开 = "//span[@class='k-icon k-i-arrow-e']"
欠费年度统计_一个列表金额 = "//tbody/tr[1]/td[1]/a"
欠费年度统计_跳转页面title验证="//div[@class='page-bar']/ul/li[2]/a"
欠费年度统计_汇总到楼宇勾选框 = "//input[@id='BuildingName']"
欠费年度统计_所有楼宇展开 = "//tbody/tr[1]/td[3]/span[1]"
欠费年度统计_汇总到收费项目勾选框 = "//input[@id='ChargeItemTypeName']"
欠费年度统计_所有月份展开 = "//tbody/tr[1]/th[1]/span[1]"
欠费年度统计_所有项目展开="//tbody/tr[3]/th[1]/span[1]"
欠费年度统计_导出年汇总按钮 = "//button[@id='btnExport']"
欠费年度统计_导出年欠费详情按钮 = "//button[@id='btnExportYearDetail']"
##########已收费用年度统计##########
已收费用年度统计_已收费用时间段选择框 = "//input[@id='dateRange']"
已收费用年度统计_已收费用时间段选择上个月 = "//div[@class='ranges']/ul/li[2]"
已收费用年度统计_所有管理区展开 = "//span[@class='k-icon k-i-arrow-e']"
已收费用年度统计_一个列表金额 = "//tbody/tr[1]/td[1]/a"
已收费用年度统计_跳转页面title验证="//div[@class='page-bar']/ul/li[2]/a"
已收费用年度统计_汇总到楼宇勾选框 = "//input[@id='BuildingName']"
已收费用年度统计_所有楼宇展开 = "//tbody/tr[1]/td[3]/span[1]"
已收费用年度统计_汇总到收费项目勾选框 = "//input[@id='ChargeItemTypeName']"
已收费用年度统计_所有月份展开 = "//tbody/tr[1]/th[1]/span[1]"
已收费用年度统计_所有项目展开="//tbody/tr[3]/th[1]/span[1]"
已收费用年度统计_导出按钮 = "//button[@id='btnExport']"
##########收费率年度统计##########
收费率年度统计_应收时间段选择框 = "//input[@id='dateRange']"
收费率年度统计_应收时间段选择上个月 = "//div[@class='ranges']/ul/li[2]"
收费率年度统计_所有管理区展开 = "//span[@class='k-icon k-i-arrow-e']"
收费率年度统计_一个列表金额 = "//tbody/tr[1]/td[1]/a"
收费率年度统计_跳转页面title验证="//div[@class='page-bar']/ul/li[2]/a"
收费率年度统计_汇总到楼宇勾选框 = "//input[@id='BuildingName']"
收费率年度统计_所有楼宇展开 = "//tbody/tr[1]/td[3]/span[1]"
收费率年度统计_汇总到收费项目勾选框 = "//input[@id='ChargeItemTypeName']"
收费率年度统计_所有月份展开 = "//tbody/tr[1]/th[1]/span[1]"
收费率年度统计_所有项目展开="//tbody/tr[3]/th[1]/span[1]"