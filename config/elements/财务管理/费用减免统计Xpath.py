# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index
    


账号输入框="//input[@type='text']"
密码输入框="//input[@type='password']"
##########费用减免明细##########
费用减免明细_导出="//button[@id='btnExport']"
费用减免明细_简单搜索输入框="//input[@id='searchTerm']"
费用减免明细_简单搜索按钮="//button[@id='btnFilter']"
费用减免明细_高级搜索展开按钮="//input[@id='searchTerm']/following-sibling::div//button[2]"
费用减免明细_高级搜索_管理区下拉="//select[@id='RegionId']"
费用减免明细_高级搜索_选择管理区="//select[@id='RegionId']/option[2]"
费用减免明细_高级搜索_客户姓名="//input[@id='CustomerName']"
费用减免明细_高级搜索_按钮="//button[@id='btnFilterDetail']"
费用减免明细_查看客户详情="//tbody/tr[1]/td[1]/a"
费用减免明细_客户详情页面验证="//div[@class='ant-drawer-body']/div[1]/div[1]/div[1]//div[@class='ant-card-body']/div[1]/div[1]/span[2]"
费用减免明细_查看资源详情="//tbody/tr[1]/td[2]/a"
费用减免明细_资源详情页面验证="//h2"
费用减免明细_表格="//div[@id='gridFeeDiscountReport']/div/table"
##########费用减免汇总##########
费用减免汇总_资源树搜索框="//input[@id='txtSerachTerm']"
费用减免汇总_收费项目="//input[@class='select2-search__field']"
费用减免汇总_选择收费项目="//ul[@id='select2-ChargeItemTypeIds-results']/li[1]"
费用减免汇总_减免时段开始日期="//input[@id='DiscountStartDate']"
费用减免汇总_减免时段结束日期="//input[@id='DiscountEndDate']"
费用减免汇总_导出="//button[@id='btnExport']"
费用减免汇总_表格="//table"
费用减免汇总_查看客户="//tbody/tr[1]/td[4]/a"
费用减免汇总_客户详情页面验证="//div[@class='ant-drawer-body']/div[1]/div[1]/div[1]//div[@class='ant-card-body']/div[1]/div[1]/span[2]"
费用减免汇总_查看资源="//tbody/tr[1]/td[3]/a"
费用减免汇总_资源详情页面验证="//h2"
