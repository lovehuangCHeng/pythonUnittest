# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index
#抄表管理
##标签切换
抄表进度概况="//li[1]/a[@class='ajaxify']"
抄表进度明细="//li[2]/a[@class='ajaxify']"
抄表历史记录="//li[3]/a[@class='ajaxify']"

##抄表概况
进度概况选择表下拉="//span[@id='select2-MeterType-container']"
进度概况选择表类型="//ul[@id='select2-MeterType-results']/li[1]"
进度概况管理区下拉="//select[@id='RegionId']"
进度概况选择管理区="//select[@id='RegionId']/option[2]"
楼宇选择下拉="//span[@id='select2-BuildingId-container']"
选择楼宇="//ul[@id='select2-BuildingId-results']//li[1]"
清除楼宇按钮="//span[@id='select2-BuildingId-container']/span[@class='select2-selection__clear']"
批量录入按钮="//tbody/tr[1]//button[@class='btn btn-default btnBatchEntering']"

##抄表进度明细
查看全部抄表数据="//div[@id='houseMeterReadingStatus']/label[1]"
查看已抄表数据="//div[@id='houseMeterReadingStatus']/label[2]"
查看未抄表数据="//div[@id='houseMeterReadingStatus']/label[3]"
导出抄表数据="//button[@id='btnExport']"
批量录入="//button[@id='btnBatchEntering']"
仪表种类输入框删除="//span[text()='×']"
抄表房间搜索输入="//input[@id='HouseNumber']"
抄表搜索按钮="//button[@id='btnFilterDetail']"
本期读数输入框="//tr[1]//input[@class='tooltip-show']"
本次抄表日期选择器="//div[@class='input-group date form_date col-md-8']//button[@class='btn default date-set']"
选择本次抄表日期="//div[@class='datetimepicker datetimepicker-dropdown-top-left dropdown-menu']//tbody/tr[3]/td[1]"
抄表保存按钮="//button[@id='btnSave']"
录入成功确定="//div[@class='modal-dialog']//button[@class='btn btn-primary']"
录入返回按钮="//a[@id='btnBack']"

##抄表历史疾苦
选择状态为已录入的数据="//tbody[@role='rowgroup']//td[text()='已录入']"
删除抄表数据="//button[@id='btnDelete']"
删除抄表二次确认="//a[@class='btn btn-sm btn-danger']"

#公摊仪表抄表
##标签切换
公摊进度概况="//li[1]/a[@class='ajaxify']"
公摊抄表进度明细="//li[2]/a[@class='ajaxify']"
公摊历史记录="//li[3]/a[@class='ajaxify']"
分摊进度明细="//li[4]/a[@class='ajaxify']"
分摊结果="//li[5]/a[@class='ajaxify']"

##公摊进度概况
选择仪表种类下拉框="//span[@id='select2-MeterTypeId-container']"
选择仪表种类="//ul[@id='select2-MeterTypeId-results']/li[last()]"
管理区下拉="//select[@id='RegionId']"
选择管理区="//select[@id='RegionId']/option[2]"
批量录入按钮="//button[@id='btnEntering']"
公摊输入用量="//td[text()='未分摊']/../td[6]/input"
批量录入取消="//a[@id='btnBack']"
导入抄表数据="//button[@class='btn btn-primary dropdown-toggle hover-initialized']"
导入数据="//a[@id='btnImport']"
取消导入="//div[@id='importWindow']//button[@class='btn btn-default']"
公摊抄表搜索="//button[@id='btnFilter']"
选择未分摊抄表历史="//td[text()='未分摊']"
切换未分摊标签="//div[@id='readingRange']/label[2]"
分摊按钮="//tbody/tr[1]/td/a[1]"
勾选未分摊数据="//tbody/tr[1]/td//input"
确认分摊="//div[@class='modal-dialog']/div[@class='modal-content']//button[@class='btn btn-primary']"
批量分摊="//button[@id='btnAssign']"
查看分摊结果="//tbody/tr[1]/td/a[2]"
分摊结果搜索="//button[@id='btnFilter']"









