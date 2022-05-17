# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index
#已出账单
##高级搜索
高级搜索下拉框="//div[@class='input-group-btn']/button[@class='btn filter-collapse-toggle']"
记账日期="//input[@id='billCreateDateRange']"
应收日期="//input[@id='billShouldChargeDateRange']"
应收开始时间输入框="//div[@class='daterangepicker dropdown-menu opensright show-calendar'][2]//div[@class='daterangepicker_start_input']/input[@class='input-mini']"
应收结束时间输入框="//div[@class='daterangepicker dropdown-menu opensright show-calendar'][2]//div[@class='daterangepicker_end_input']/input[@class='input-mini']"
应收日期确定按钮="//div[@class='daterangepicker dropdown-menu opensright show-calendar'][2]/div[@class='ranges']//button[@class='applyBtn btn btn-small btn-sm btn-success']"
客户输入="//input[@id='CustomerName']"
房间代码="//input[@id='Code']"
已出账单管理区="//select[@id='RegionId']"
账单状态="//select[@id='BillStatus']"
选择已出账单="//select[@id='BillStatus']/option[2]"
选择冻结账单="//select[@id='BillStatus']/option[4]"
单击搜索操作="//button[@id='btnFilterDetail']"
##操作
导出="//div[@id='exportMenu']/button"
导出excel="//button[@id='btnExport']"
导出明细excel="//button[@id='btnExportDetail']"
删除账单="//button[@id='btnDeleteBill']"
选择回收票据="//div[@id='uniform-CallbackTicket']//input[@id='CallbackTicket']"
搜索结果="//div[@id='gridReceivableListDetailReport']//tr[1]/td[1]"
勾选外层账单="//div[@id='gridReceivableListDetailReport']//tr[1]/td[1]//input"
勾选账单="//div[@id='partPaidBillItemGrid']/div[1]//input"
撤销并删除账单="//button[@id='bntDeleteBillConfirm']"
关闭撤销删除页面="//button[@id='btnDeleteBillCancel']"
确认撤销账单="//div[@class='modal-dialog']//button[@class='btn btn-primary']"
已出二次确认="//a[@class='btn btn-sm btn-danger']"
冻结账单下拉="//div[@class='col-md-8 col-sm-12 col-xs-12 toolbar']/div[2]/button"
冻结账单="//button[@id='btnFrozenBill']"
解冻账单="//button[@id='btnUnFrozenBill']"
标记为开票="//button[@id='markBillInvoiced']"
标记为未开票="//button[@id='markBillUnInvoiced']"
修改费用承担人="//button[@id='btnUpdateOwner']"
设置欠费原因="//button[@id='btnSetArrearReasonType']"
div确定按钮="//div[@class='modal-content']/div[2]/button"

#固定金额分摊
新建固定金额="//button[@id='btnAdd']"
选择管理区下拉框="//select[@id='RegionId']"
选择管理区="//select[@id='RegionId']/option[@value=${regionid}}"
选择费用名称="//span[@id='select2-ChargeItemId-container']"
选择收费标准="//ul[@id='select2-ChargeItemId-results']/li[1]"
总金额输入="//input[@id='TotalAmount']"
开始时间选择器="//span[@aria-controls='startDate_dateview']/span"
选择开始日期="//div[@id='startDate_dateview']//table[@class='k-content']/tbody/tr[3]/td[3]"
结束时间选择器="//span[@aria-controls='endDate_dateview']/span"
选择结束时间="//div[@id='endDate_dateview']//table[@class='k-content']/tbody/tr[3]/td[4]"
分摊方式下拉框="//select[@id='AllocationType']"
按户分摊="//select[@id='AllocationType']/option[2]"
指定楼宇所有房间="//label[@class='radio-inline'][2]/div[@class='radio']//input"
选择楼宇下拉框="//span[@id='select2-BuildingId-container']"
楼宇搜索输入狂="//input[@class='select2-search__field']"
选择楼宇="//ul[@id='select2-BuildingId-results']/li[1]"
保存分摊="//button[@id='btnSave']"
编辑固定金额分摊="//div[@id='gridCostShare']//tr[1]/td[2]/a[1]"
取消按钮="//form[@id='CostAllocationForm']//button[@class='btn btn-default ajaxify']"
删除固定金额分摊="//div[@id='gridCostShare']//tr[1]/td[2]/a[2]"
二次确认="//div[@class='modal-dialog']//button[@class='btn btn-primary']"
分摊按钮="//div[@id='gridCostShare']//tr[1]/td[2]/a[3]"
查看分摊结果="//div[@id='gridCostShare']//tr[1]/td[2]/a[4]"





