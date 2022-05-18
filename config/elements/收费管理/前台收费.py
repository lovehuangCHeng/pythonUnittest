#预存款收费
预缴按钮="xpath==//button[@id='btnAdd']"
搜索栏="xpath==//span[@id='select2-CustomerId-container']/span[@class='select2-selection__placeholder']"
搜索栏输入框="xpath==//span[@class='select2-dropdown select2-dropdown--below']//input"
下拉选择客户="xpath==//ul[@id='select2-CustomerId-results']/li[1]"
预缴_房间下拉框="xpath==//input[@id='HouseId']/.."#选择房间数据#//ul/li[text()='${YCKCode}']
预存款输入框="xpath==//input[@id='Balance']"
选择预存款账户="xpath==//span[@id='select2-ChargeItemTypeId-container']"
选择通用账户="xpath==//ul[@id='select2-ChargeItemTypeId-results']/li[1]"
选择付款方式="xpath==//span[@id='select2-PaidMethodId-container']"
付款方式现金="xpath==//ul[@id='select2-PaidMethodId-results']/li[1]"
确认收款="xpath==//button[@id='btnPaymentPreview']"
确认但不打印="xpath==//button[@id='btnPaymentConfirm']"
充值成功断言="xpath==//div[text()='预存款充值成功！']"
确定充值成功="xpath==//div[@class='bootbox modal bootbox-alert in']//button[@class='btn btn-primary']"
##冲抵欠费
预存款账户搜索="xpath==//input[@id='searchTerm']"
选择账户账单="xpath==//tbody/tr[1]/td[1]/div/span"
确认搜索="xpath==//button[@id='btnFilter']"
选择账户="xpath==//tbody/tr[1]/td[3]"
冲抵欠费按钮="xpath==//button[@id='btnPayBill']"
确认冲抵收费="xpath==//button[@id='btnAdvancePayConfirm']"
收费成功断言="xpath==//div[text()='收费成功！']"
查看收支明细="xpath==//button[@id='btnDetail']"
选择支出="xpath==//div[@id='gridDetail']//td[text()='支出']"
查看支出明细="xpath==//button[@id='btnDetail']"
关闭支出明细="xpath==//div[@id='ViewBillDetailWindow']//button[@class='btn btn-default']"
欠费冲抵返回="xpath==//div[@class='page-content-body']//a[@class='btn btn-primary']"
查看核销明细="xpath==//button[@id='btnViewBillDetail']"
出现核销账单="xpath==//div[@id='gridViewBillDetail']//tbody/tr[1]/td[1]"
勾选核销账单="xpath==//div[@id='gridViewBillDetail']//div[@class='k-link']//input"
批量打印票据="xpath==//button[@id='btnBatchPrint']"
确定并开始打印="xpath==//button[@id='btnPaymentConfirmAndPrint']"
预存款退款="xpath==//button[@id='refund']"
退款金额输入框="xpath==//input[@id='Amount']"
退款原因="xpath==//textarea[@id='Reason']"
退款保存="xpath==//button[@id='btnSave']"
退款成功断言="xpath==//div[text()='退款成功！！']"
确定退款="xpath==//div[@class='bootbox modal bootbox-alert in']//button[@class='btn btn-primary']"
#经营性收费
##收费
客户搜索栏="xpath==//span[@id='select2-CustomerId-container']/span"
客户搜索栏输入框="xpath==//span[@class='select2-dropdown select2-dropdown--below']//input"
下拉选择客户="xpath==//ul[@id='select2-CustomerId-results']/li[1]/div"
添加临时费用="xpath==//button[@id='btnAddCost']"
标准搜索栏="xpath==//span[@id='select2-TemporaryCostChargeItem-container']"
标准搜索栏输入框="xpath==//span[@class='select2-dropdown select2-dropdown--below']//input[@class='select2-search__field']"
下拉选择收费标准="xpath==//ul[@id='select2-TemporaryCostChargeItem-results']/li[1]"
选择开始时间按钮="xpath==//form[@id='temporaryCostForm']//div[@class='form-group'][4]//button"
选择开始时间="xpath==//div[@class='datetimepicker datetimepicker-dropdown-top-left dropdown-menu'][1]//tbody/tr[4]/td[@class='day'][2]"
选择结束时间按钮="xpath==//form[@id='temporaryCostForm']//div[@class='form-group'][5]//button"
选择结束时间="xpath==//div[@class='datetimepicker datetimepicker-dropdown-top-left dropdown-menu'][2]//tbody/tr[4]/td[@class='day'][2]"
经营性金额输入框="xpath==//input[@id='Amount']"
确认添加="xpath==//div[@id='temporaryCostWindow']//button[@class='btn btn-primary btnOkWindow']"
添加成功断言="xpath==//div[text()='添临时性收费成功！']"
确认添加成功="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
选择付款方式="xpath==//span[@id='select2-PaidMethodId-container']"
付款方式现金="xpath==//ul[@id='select2-PaidMethodId-results']/li[1]"
确认收款="xpath==//button[@id='btnPaymentPreview']"
确认但不打印="xpath==//button[@id='btnPaymentConfirm']"
收费成功断言="xpath==//div[text()='收费成功！']"
确认收费成功="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
##添加客户
添加客户按钮="xpath==//button[@id='btnAddCustomer']"
管理区下拉框="xpath==//select[@id='CustomerRegionId']"
下拉框选择管理区="xpath==//select[@id='CustomerRegionId']//option[2]"
客户类型下拉框="xpath==//span[@id='select2-CustomerTypeId-container']"
下拉选择客户类型="xpath==//ul[@id='select2-CustomerTypeId-results']/li[1]"
客户名称输入框="xpath==//div[@class='col-md-6'][1]//input[@id='CustomerName']"
确认添加客户="xpath==//button[@id='btnConfirmAddCustomer']"
创建客户成功断言="xpath==//div[text()='创建客户成功']"
确认客户创建成功="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
##收费历史记录
管理区下拉="xpath==//select[@id='RegionId']"
下拉选择管理区="xpath==//select[@id='RegionId']/option[@value='3']"#未引用
客户名称输入框="xpath==//input[@id='CustomerName']"
房间名称输入框="xpath==//input[@id='HouseNumber']"
收费日期输入框="xpath==//input[@id='ChargeDate']"
确认日期="xpath==//button[@class='applyBtn btn btn-small btn-sm btn-success']"
选择秒左="xpath==//div[@class='calendar left']//select[@class='minuteselect']"
选择00秒左="xpath==//div[@class='calendar left']//select[@class='minuteselect']/OPTION[@selected]/preceding-sibling::option[1]"
选择秒右="xpath==//div[@class='calendar right']//select[@class='minuteselect']"
选择60秒右="xpath==//div[@class='calendar right']//select[@class='minuteselect']/OPTION[@selected]/following-sibling::option[1]"
搜索按钮="xpath==//button[@id='btnFilterDetail']"
导出excel="xpath==//button[@id='btnExport']"
展开明细="xpath==//div[@id='PaymentHistory']//tr[1]/td[1]/a"
查看票据="xpath==//div[@id='PaymentHistory']//li[2]/span[@class='k-link']"
更改票号="xpath==//div[@id='PaymentHistoryTicketDetails']//tbody//a[5]"
更改票号输入框="xpath==//input[@id='newTicketNumber']"
确认修改="xpath==//form[@id='changeTicketNumberForm']//button[@class='btn btn-primary update']"
再次确认修改="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
修改成功断言="xpath==//div[text()='修改成功!']"
修改成功确认="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
补打按钮="xpath==//div[@id='PaymentHistoryTicketDetails']//tbody//a[4]"
作废并重打按钮="xpath==//div[@id='PaymentHistoryTicketDetails']//tbody//a[3]"
确认单不打印="xpath==//button[@id='btnPaymentConfirm']"
确定并开始打印="xpath==//button[@id='btnPaymentConfirmAndPrint']"
撤销收费="xpath==//a[@class='undoCharge']"
撤销回收票据="xpath==//button[@id='bntCallbackTicketConfirm']"
回收票据失败断言="xpath==//strong[@id='errorMessage']"
撤销不回收票据="xpath==//button[@id='bntNotCallbackTicketConfirm']"
撤销收费成功="xpath==//div[text()='收费撤销成功！']"
撤销成功确定="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
已撤销的再撤销断言="xpath==//div[text()='该收费记录已经撤销,不能反复撤销！']"
撤销成功数据断言="xpath==//td[text()='已撤销']"
按房间车位收费历史="xpath==//li[2]/a[@class='ajaxify']"
数据存在判断="xpath==//div[@id='PaymentHistory']//tr[@class='k-master-row']/td[4]"
票据数据存在断言="xpath==//table/tbody/tr[@class='k-master-row'][1]/td[6]"
按票据搜索收费历史="xpath==//li[3]/a[@class='ajaxify']"
票据号输入框="xpath==//input[@id='TicketNumber']"
退款撤销断言="xpath==//strong[text()='已经退款不能撤销！']"
#催费通知单
日期选择按钮="xpath==//input[@id='Filter_Date']/.."
选择本月="xpath==//div[@class='laydate-footer-btns']/span[2]"
搜索欠费账单="xpath==//button[@id='btnFilterDetail']"
数据存在断言="xpath==//table/tbody/tr[1]/td[3]"
开始打印="xpath==//button[@id='btnPrint']"
PDF导出="xpath==//button[@id='btnExport']"
断言加载打印="xpath==//div[@class='loading-message loading-message-boxed']"
#客户零头明细
业主姓名="xpath==//input[@id='filterCustomer']"
开始日期="xpath==//input[@placeholder='收费起始日期']"
开始日期输入="xpath==//input[@placeholder='收费起始日期' and @class='ant-calendar-input ']"
结束日期="xpath==//input[@placeholder='收费结束日期']"
结束日期输入="xpath==//input[@placeholder='收费结束日期' and @class='ant-calendar-input ']"
搜索账户="xpath==//button/span[text()='查 询']/.."
概览数据存在断言="xpath==//tbody/tr[1]/td[1]"
明细数据存在断言="xpath==//table//tr[1]/td[6]"
收起明细按钮="xpath==//tbody/tr[1]/td[1]/div"
展开明细按钮="xpath==//tbody/tr[1]/td[1]/div"
重置搜索="xpath==//button/span[text()='重 置']/.."
导出Excel="xpath==//button/span[text()='导出EXCEL']/.."
#交款申请
新建交款申请="xpath==//button[@id='btnAdd']"
交款数据存在断言="xpath==//div[@id='gridProject']//table[@class='k-selectable']/tbody/tr[1]/td[1]"
明细数据存在断言="xpath==//div[@id='gridDetail']//tbody/tr[1]/td[1]"
项目数据存在断言="xpath==//div[@id='gridItemTypeDetail']//tr[1]/td[1]"
导出excel="xpath==//button[@id='btnExportProject']"
导出明细excel="xpath==//button[@id='btnExportDetail']"
导出项目excel="xpath==//button[@id='btnExportItemTypeDetail']"
收款明细="xpath==//ul[@class='nav nav-tabs']/li[2]/a"
项目明细="xpath==//ul[@class='nav nav-tabs']/li[3]/a"
交款备注="xpath==//textarea[@id='Remark']"
保存交款="xpath==//button[@id='btnSave']"
交款成功断言="xpath==//div[text()='提交轧账成功！']"
确定交款成功="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
搜索交款申请="xpath==//button[@id='btnFilter']"
选择交款申请="xpath==//div[@id='gridAccountStatement']//td[text()='未审核']/../td[1]//input"
交款申请编辑="xpath==//button[@id='btnEdit']"
更新成功断言="xpath==//div[text()='更新轧账成功！']"
交款申请查看明细="xpath==//button[@id='btnDetail']"
查看明细返回="xpath==//a[@class='btn btn-default']"
审核交款申请="xpath==//button[@id='btnConfirm']"
审核成功断言="xpath==//div[text()='审核成功！']"
审核成功确定="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
撤销交款审核="xpath==//button[@id='btnUndoAudit']"
选择已审核交款="xpath==//div[@id='gridAccountStatement']//td[text()='已审核']/../td[1]//input"
撤销审核成功断言="xpath==//div[text()='撤销审核成功！']"
撤销审核确定="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
撤销扎帐="xpath==//button[@id='btnCancel']"
撤销成功断言="xpath==//div[text()='1条记录撤销成功！']"
撤销扎帐确定="xpath==//div[@class='modal-dialog']//button[@class='btn btn-primary']"
