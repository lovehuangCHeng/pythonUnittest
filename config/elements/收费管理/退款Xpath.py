# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index
#退款管理
##新建退款
票据号输入框="//input[@id='TicketNumber']"
票据号搜索按钮="//button[@id='btnFilterDetail']"
搜索重置按钮="//button[@id='btnReset']"
退款管理下拉框="//div[@id='gridTicketsReport']//tr[1]//a[@class='k-icon k-plus']"
退款管理下拉框1="//div[@id='gridTicketsReport']//tr[3]//a[@class='k-icon k-plus']"
退款管理下拉框2="//div[@id='gridTicketsReport']//tr[5]//a[@class='k-icon k-plus']"
退款管理下拉框3="//div[@id='gridTicketsReport']//tr[7]//a[@class='k-icon k-plus']"
退款管理下拉框4="//div[@id='gridTicketsReport']//tr[9]//a[@class='k-icon k-plus']"
退款管理下拉框5="//div[@id='gridTicketsReport']//tr[11]//a[@class='k-icon k-plus']"
退款管理下拉框6="//div[@id='gridTicketsReport']//tr[13]//a[@class='k-icon k-plus']"
退款管理下拉框7="//div[@id='gridTicketsReport']//tr[15]//a[@class='k-icon k-plus']"

选择未退款的账单="//td[text()='未退款']//preceding-sibling::td[9]//input"
退款按钮="//button[@id='btnRefund']"
退款备注="//input[@id='RefundRemark']"
付款方式下拉输入框="//span[@id='select2-PaidMethodId-container']/span[@class='select2-selection__placeholder']"
选择退款方式="//div[@id='chargeConfirmWindow']//span[@class='select2-selection__placeholder']"
选择现金退款="//ul[@id='select2-PaidMethodId-results']/li[1]"
确定但不打印="//button[@id='btnPaymentConfirm']"
确定并开始打印="//button[@id='btnPaymentConfirmAndPrint']"
退款成功判断="//div[text()='退款成功！']"
退款成功确定="//div[@class='modal-dialog']//button[@class='btn btn-primary']"
##退款历史记录
高级搜索下拉="//div[@class='input-group-btn']/button[@class='btn filter-collapse-toggle']"
退款日期="//input[@id='RefundDate']"
选择本月="//div[@class='ranges']/ul/li[1]"
确认搜索="//button[@id='btnFilterDetail']"
导出excel="//button[@id='btnExport']"
重置搜索="//button[@id='btnReset']"
勾选退款历史="//div[@id='gridChargeReturn']//tr[1]/td[1]//input"
查看退款历史="//button[@id='btnViewDetail']"
查看详细返回="//button[@class='btn btn-primary']"
补打票据按钮="//button[@id='btnPaymentPreview']"
打印预览按钮="//div[@id='confirmTicketGrid']//button[@class='btn btn-primary preview-ticket']"
确定但不打印="//button[@id='btnPaymentConfirm']"
确定并开始打印="//button[@id='btnPaymentConfirmAndPrint']"
取消预览="//div[@id='printWindow']//button[@class='btn btn-default']"













