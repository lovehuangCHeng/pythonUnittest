#催费通知单
管理区下拉="//select[@id='Filter_RegionId']"
下拉选择管理区="//select[@id='Filter_RegionId']/option[@value='3']"#未引用
日期选择按钮="//input[@id='Filter_Date']/.."
选择本月="//div[@class='laydate-footer-btns']/span[2]"
搜索欠费账单="//button[@id='btnFilterDetail']"
数据存在断言="//table/tbody/tr[1]/td[3]"
开始打印="//button[@id='btnPrint']"
PDF导出="//button[@id='btnExport']"
断言加载打印="//div[@class='loading-message loading-message-boxed']"