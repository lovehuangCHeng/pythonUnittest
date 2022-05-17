# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index
    


账号输入框="Xpath=//input[@type='text']"
密码输入框="Xpath=//input[@type='password']"
#图标版权设置
网站名输入框="Xpath=//form//input[@id='SiteName']"
公司名输入框="Xpath=//form//input[@id='CompanyName']"
图标版权保存按钮="Xpath=//form//button[@id='btnSave']"
##系统参数设置
取舍方法="//form[@id='decimalDigitSetting']//label[2]/div[@id='uniform-RoundingMode']"
小数点输入框="//form[@id='decimalDigitSetting']//input[@id='DecimalDigit']"
小数点位数="//input[@type='text' and@placeholder='请输入小数点位数']"
生成零元账单="//form[@id='decimalDigitSetting']//input[@id='IsKeepZeroBill']"
按应收日期依次收费账单="//form[@id='decimalDigitSetting']//input[@id='IsPayBillByOrder']"
应收款统计包含冻结账单="//form[@id='decimalDigitSetting']//input[@id='IsIncludeFrozenBill']"
系统参数设置保存按钮="//form[@id='decimalDigitSetting']//button[@id='btnSave']"
##新建支付方式
添加支付方式="//main//button"
支付方式名称="//input[@id='name']"
支付方式编号="//input[@id='number']"
使用场景PC="//form/div/div[3]//label[1]//input"
新建支付方式手续费率="//form/div/div[4]//input"
新建支付方式备注="//form//input[@id='remark']"
新建支付方式保存="//div/button[2]"
编辑支付方式按钮="//table/tbody//tr[1]/td[7]/span/a[1]"
编辑支付方式保存按钮="//body/div[2]//button[@class='ant-btn ant-btn-primary']"
删除支付方式按钮="//tbody//td/span/a[2]"
删除支付方式确认按钮="//tbody//td/span/a[2]"
###系统初始化
下载房间客户数据模板="//main//p[1]/a"
下载房间仪表数据模板="//main//p/a"
下载车位数据模板="//main//p/a"
创建收费标准="//main//p"
下载房间历史账单数据模板="//main//p/a"
下载车位历史账单数据模板="//main//p/a"
下载房间收费记录数据模板="//main//p/a"
下载车位收费记录数据模板="//main//p/a"
导入车位历史账单Tab="//main/div/div[3]//span/following-sibling::div[1]/div/div/div/div[2]"
创建车位收费记录Tab="//main/div/div[3]//span/following-sibling::div[1]/div/div/div/div[2]"
上一步="//main//div[1]/button"
下一步="//main//div/button[2]"
完成="//main//div/button[2]"
跳过="//main//div/button[2]/preceding-sibling::button[1]"
初始化完成取消="//body/div[3]//div/button[2]/preceding-sibling::button[1]"
初始化完成确定="//body/div[3]//div/button[2]"
初始化完成重新开启="//button"
#打印设置-新建/编辑
新建打印设置按钮="//button[@id='btnAdd']"
编辑打印设置按钮="//button[@id='btnEdit']"
选择管理区下拉框="//select[@id='RegionId']"
选择管理区="//select[@id='RegionId']/option[2]"
类型下拉框="//span[@id='select2-TemplateType-container']"
类型筛选框="//span/input[@class='select2-search__field']"
选择类型="//ul[@id='select2-TemplateType-results']/li[1]"
总行数输入框="//input[@id='TableRowCount']"
模板下拉框="//*[@id='PrintTemplateForm']/div/div[2]//span[@class='select2-selection select2-selection--single']"
模板筛选框="//li/input[@class='select2-search__field']"
选择模板="//ul[@id='select2-ReportTemplateId-results']/li[1]"
合并仪表类型勾选框="//input[@id='IsMeterType']"
合并项目类型打印勾选框="//input[@id='IsGroupByChargeItemCategory']"
合并时间段打印勾选框="//input[@id='IsJoin']"
合并资源打印勾选框="//input[@id='IsGroupByOrganizationItem']"
打印设置保存按钮="//button[@id='btnSave']"
#打印设置-设计/删除
一条打印设置数据="//tbody/tr[1]/td[1]//input"
打印模板设计按钮="//button[@id='btnDesign']"
打印模板设计操作列="//div[@class='dxrd-menu-button-image']"
保存打印模板设置按钮="//div[@id='reportDesignerContainer']//div[@class='dxrd-menu-button-image']"
打印模板设计关闭按钮="//button[@class='close']"
删除打印模板="//button[@id='btnDelete']"
确认删除打印模板按钮="//a[@class='btn btn-sm btn-danger']"
#数据备份
创建备份按钮="//button[@id='btnAdd']"
确定创建按钮="//i[@class='glyphicon glyphicon-ok']"
下载备份按钮="//tr[1]/td/a[@class='download']"
删除备份按钮="//tr[1]/td/a[@class='deleteRow']"
确认删除备份按钮="//body/div[6]/div/div/div/div[2]/button[@class='btn btn-primary']"
一条备份数据="//tr[1]//div[1]/span/input[@class='select-row']"
批量删除备份按钮="//button[@id='btnDelete']"
确认批量删除备份按钮="//a[@class='btn btn-sm btn-danger']"
备份简单搜索输入框="//input[@id='searchTerm']"
备份搜索简单搜索按钮="//button[@id='btnFilter']"
备份搜索展开="//div[1]/button[@class='btn filter-collapse-toggle']"
文件名输入框="//input[@id='FileName']"
文件大小输入框="//input[@id='FileSize']"
文件创建日期="//input[@id='CreateDateRange']"
选择创建日期本月="//div[@class='ranges']/ul/li[1]"
备份高级搜索按钮="//button[@id='btnFilterDetail']"
设置自动备份按钮="//button[@id='btnAutomaticBackup']"
设置自动备份确定按钮="//button[@id='btnAddAutomaticBackupWindow']"
#操作日志
操作模块下拉框="//div[@id='module']"
选择操作模块="//div[@id='module']/following-sibling::div[1]//ul/li[1]"
操作类型下拉框="//div[@id='type']"
选择操作类型="//div[@id='type']/following-sibling::div[1]//ul/li[1]"
操作人下拉框="//div[@id='staffId']"
选择操作人="//div[@id='staffId']/following-sibling::div[1]//ul/li[1]"
操作时间选择框="//span[@id='createDate']/span"
选择操作时间今天="//span[text()='今天']"
操作详情输入框="//input[@id='title']"
操作日志高级搜索按钮="//button[@class='ant-btn ant-btn-primary']"
#IC卡设置
用户起始值下拉框="//div[@id='IcMeterSettingTabs_userInitNumber']"
用户起始值选择="//ul[@class='ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']/li[1]"
永久编号选择用户填写="//input[@value=1]"
IC卡设置保存按钮="//button[@type='submit']"


'''
组织架构通用的定位
'''
保存按钮="//div[@class='ant-modal-footer']/button[2]"
确认删除按钮="//div[@class='ant-popover-buttons']/button[2]"
简单搜索按钮="//span[@class='ant-input-suffix']"


#组织架构
组织架构新建按钮="//button/span[text()='新建 ']/.."
新建分公司按钮="//li[text()='分公司']"
新建部门按钮="//li[text()='部门']"
删除组织架构按钮="//button/span[text()='删 除']/.."
编辑组织架构按钮="//tbody/tr[1]/td[7]/a"
展开中公司按钮="//tbody/tr[1]/td[2]/div"

上级机构下拉框="//div[@class='ant-select-selection__rendered']/div"
选择上级部门="//li[@role='option'][1]"
分公司部门名称输入框="//input[@id='name']"
分公司序号输入框="//input[@id='code']"
分公司地址输入框="//input[@id='address']"
分公司电话输入框="//input[@id='tel']"
新建分公司部门备注输入框="//textarea[@id='remark']"
新建部门名称="//input[@id='name']"
组织架构简单搜索输入框="//input[@placeholder='请输入名称']"
一条组织架构数据="//tbody/tr[1]/td[1]//input"
第二个复选框="//tbody/tr[2]/td[1]//input"

#权限管理
新建权限按钮="//button/span[text()='新 增']/.."
编辑权限按钮="//tbody/tr[3]/td[3]//a[1]"
权限名称输入框="//input[@id='name']"
权限备注输入框="//textarea[@id='description']"
所有数据权限单选框="//thead/tr/th[2]//input"
所属管理区权限单选框="//thead/tr/th[3]//input"
禁止权限单选框="//thead/tr/th[4]//input]"
简单搜索权限输入框="//input[@placeholder='请输入名称']"
删除权限按钮="//tbody/tr[1]/td[3]//a[2]"

#用户列表
职员列表="//div[@role='tab' and text()='职员列表']"
职员组织结构="//div[@role='tab' and text()='职员组织机构']"
职员岗位="//div[@role='tab' and text()='职员岗位']"
新建用户按钮="//button/span[text()='新 增']/.."
显示按钮="//button/span[text()='显示 ']/.."
显示启用="//li[text()='启用']"
显示禁用="//li[text()='禁用']"
导入职员="//button/span[text()='导入职员 ']/.."
下载职员模板="//li[text()='下载导入模板']"
导入职员模板="//li[text()='导入职员']"
编辑用户按钮="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]//a[1]"
用户名称输入框="//input[@id='name']"
用户电话输入框="//input[@id='tel']"
简单搜索用户输入框="//input[@placeholder='姓名/身份证/电话']"

一条用户数据="//tbody/tr[1]/td[1]//input/.."
禁用用户按钮="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]//a[2]"
启用用户按钮="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]//a[2]"
删除用户按钮="//button/span[text()='删 除']/.."
职员_上传文件="//button/span[text()=' 上传文件']/.."
取消导入职员模板="//div[@class='ant-modal-footer']/button[1]"


职员组织机构_选择左侧组织架构="//tbody/tr[1]/td[1]/div[@role='button']/.."
职员岗位_选择左administrator="//td[text()='Administrator']"
选择职员按钮="//button/span[text()='选择职员']/.."
选择一个职员添加="//div[@class='ant-modal-content']//tbody/tr[1]/td[1]//input/.."
添加员工保存按钮="//div[@class='ant-modal-footer']/button[2]"
选择一个职员移除="//*[@id='memberGrid']/div[2]/table/tbody/tr[1]"
移除职员按钮="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]//a[text()='删除']"






