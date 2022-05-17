# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index

#收费参数设置
##收费项目定义
收费项目搜索="//input[@class='ant-input ant-input-lg']"
项目大类营业类="//span[@class='ant-tree-title'][text()='00001 主营业务收入']"
项目大类保证类="//span[@class='ant-tree-title'][text()='00003 保证金']"
项目大类预存款="//span[@class='ant-tree-title'][text()='00005 预存款']"
新建收费项目按钮="//div/button[@class='ant-btn ant-btn-primary']"
收费项目名称输入框="//input[@id='name']"
收费项目房间状态下拉框="//div[@id='changHouseStauts']//div[@class='ant-select-selection__rendered']"
收费后状态选择交房="//li[@class='ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active'][last()]"
收费项目备注文本框="//textarea[@id='remark']"
收费项目保存按钮="//div[@class='ant-modal-footer']/button[@class='ant-btn ant-btn-primary']"
收费项目取消按钮="//div[@class='ant-modal-footer']/button[@class='ant-btn']"
编辑收费项目="//div[@class='ant-table-body-inner']//tr[1]//span/a[1]"
删除收费项目="//div[@class='ant-table-body-inner']//tr[1]//span/a[2]"
收费项目搜索框="//input[@class='ant-input ant-input-lg']"
收费项目复选框="//tbody/tr[1]//span//span"
批量删除收费项目="//button[@class='ant-btn']"
预存费充值限制复选框="//input[@id='hasAccountRule']"
收费项目选择下拉框="//div[@id='chargeItemTypeId']//div[@class='ant-select-selection__placeholder']"
收费项目多选框="//div[@id='chargeItemTypeIds']//div[@class='ant-select-selection__placeholder']"
下拉框选择收费标准="//div[3]//ul[@role='listbox']/li[last()]"
下拉框多选收费标准="//div[4]//ul[@role='listbox']/li[last()]"
预存款充值限制金额输入框="//input[@id='oweAmountOrMonths']"
最多充值XX元="//input[@id='amount']"
挑选时间按钮="//span[@class='ant-form-item-children']/button"
预存款账户选择图片="//img[1]/@src"
保存账户图片="/html/body/div[5]//button[@class='ant-btn ant-btn-primary']"

##收费标准设置
###新建、编辑、删除收费标准
收费标准新建按钮="//div[@class='ant-col ant-col-16']/button[@class='ant-btn ant-btn-primary'][1]"
管理区下拉按钮="//div[@id='OrganizationItemId']//span"
收费标准选择管理区="//div[3]//li[@role='option'][last()]"
收费项目下拉按钮="//div[@id='ChargeItemTypeId']//span"
收费标准选择收费项目="//div[4]//li[@role='option'][1]"
收费标准名称="//input[@id='Name']"    
勾选按月计费="//input[@type='radio' and @value='0']"
勾选按用量计费="//input[@type='radio' and @value='2']"
勾选按数量计费="//input[@type='radio' and @value='3']"
勾选按固定金额计费="//input[@type='radio' and @value='4']"
勾选指定金额计费="//input[@type='radio' and @value='5']"
输入月单价="//input[@id='UnitPrice']"
输入天单价="//input[@id='DatePrice']"
输入用量单价="//input[@id='AmountPrice']"
收费标准仪表下拉框="//div[@id='MeterTypeId']//div"
收费标准选择仪表="//div[5]//li[@role='option'][last()]"
输入数量单价="//input[@id='NumberPrice']"
输入固定金额="//input[@id='FixedAmount']"
勾选滞纳金="//input[@id='IsLateCharge']"
输入收取比例="//input[@id='LateChargeRatio']"
收费标准备注="//textarea[@id='Remark']"
保存收费标准="//div[@class='ant-modal createCharges']//button[@class='ant-btn ant-btn-primary']"
收费标准list复选框="//tr[1]/td//input"
编辑标准="//div[@class='ant-col ant-col-16']/button[@class='ant-btn ant-btn-primary'][2]"
删除标准="//div[@class='ant-col ant-col-16']/button[@class='ant-btn ant-btn-primary'][3]"
###复制收费标准
复制标准="//div[@class='ant-col ant-col-16']/button[@class='ant-btn ant-btn-primary'][3]"
源管理区下拉框="//div[@class='ant-card ant-card-bordered'][1]//div[@class='ant-select-selection__placeholder']"
选择源管理区="//div[3]//li[@role='option'][last()]"
目标管理区下拉框="//div[@class='ant-card ant-card-bordered'][2]//div[@class='ant-select-selection__placeholder']"
选择目标管理区="//div[4]//li[@role='option'][last()-1]"
复制收费标准复选框="//div[@class='ant-table-scroll']//tr[1]/td//input"
下一步="//div[@class='ant-modal-content']//button[@class='ant-btn ant-btn-primary']"
上一步="//div[@class='ant-modal-content']//button[@class='ant-btn ant-btn-primary'][1]"
下一步2="//div[@class='ant-modal-content']//button[@class='ant-btn ant-btn-primary'][2]"
操作成功提示="//div[@class='ant-steps-item-title' and text()='操作成功']"
关闭复制收费标准="//button[@class='ant-btn ant-btn-cancel']"
###其他
导出收费标准excel="//button[@class='ant-btn ant-btn-primary'][4]"
高级搜索下拉="//a[@class='seniorSearchBtn']"
根据名称搜索输入框="//input[@id='Name']"
搜索按钮="//div[@class='ant-col ant-col-24']/button[@class='ant-btn ant-btn-primary']"
###断言
创建成功="//span[text()='创建成功']"
编辑成功="//span[text()='更新收费标准成功！']"
删除成功="//div[@class='ant-message-custom-content ant-message-success']/span"

##绑定收费标准
###添加绑定
添加绑定按钮="//a[@id='btnAddBindCharge']"
添加绑定选择管理区下拉框="//select[@id='batchAddRegionId']"
添加绑定选择管理区="//select[@id='batchAddRegionId']/option[@value='2366']"
添加绑定搜索房间="//a[@id='batchAddFilterOk'	]"
添加绑定勾选楼宇="//li[@id='7586']//i[@class='jstree-icon jstree-checkbox']"
绑定下一步="//div[@class='form-wizard']/div[2]/div/div/a[2]"
添加绑定项目下拉="//span[@id='select2-AddChargeItemTypeId-container']"
添加绑定1项目="//ul[@id='select2-AddChargeItemTypeId-results']/li[1]"
添加绑定标准下拉="//span[@id='select2-AddChargeItemId-container']"
添加绑定1标准="//ul[@id='select2-AddChargeItemId-results']/li[1]"
开始收费日期选择器="//input[@id='addChargeItemStartDate']"
选择收费开始日期="//div[@class='datetimepicker datetimepicker-dropdown-top-left dropdown-menu'][5]//tr[4]/td[4]"
确认添加页面下一步="//div[@class='form-wizard']/div[2]/div/div/a[3]"
添加绑定确认添加="//div[@id='batchAddConfirmModal']//button[@id='batchAddConfirmBtn']"
绑定收费标准确定="//div[@class='bootbox modal bootbox-alert in']//button[@class='btn btn-primary']"
添加绑定回第一步="//div[@id='fastIntialization_Wizard_Add']//a[@class='btn btn-primary toStepOne']"
添加绑定关闭="//div[@id='fastIntialization_Wizard_Add']//a[@class='btn button-cancel-batch-add default']"
###批量修改
批量修改按钮="//a[@id='btnBatchEditChargeItem']"
批量修改选择管理区下拉框="//select[@id='BatchEditRegionId']"
批量修改选择管理区="//select[@id='batchAddRegionId']/option[@value='2366']"
批量修改搜索房间="//a[@id='batchEditFilterOk']"
批量修改下一步="//div[@id='btnEditChargeItemWindow']//div[@class='form-wizard']/div[1]/div/div/a[2]"
勾选修改开始日期="//input[@id='batchEditStartDateCheckBox']"
批量修改开始日期选择器="//div[@id='editBatchChargeItemContainer']//div[@class='row'][1]//button[@class='btn default date-set']"
选择修改收费开始日期="//div[@class='datetimepicker datetimepicker-dropdown-top-left dropdown-menu'][5]//tr[4]/td[3]"
确认修改页面下一步="//div[@id='btnEditChargeItemWindow']//div[@class='form-wizard']/div[1]/div/div/a[3]"
修改绑定确认修改="//div[@id='batchEditConfirmModal']//button[@id='batchEditConfirmBtn']"
批量修改关闭="//div[@id='fastIntialization_Wizard_Batch']//a[@class='btn button-cancel-batch-edit default']"

###批量解除
批量解除按钮="//a[@id='btnCancelChargeItemSetting']"
批量解除选择管理区下拉框="//select[@id='CancelRegionId']"
批量解除选择管理区="//select[@id='CancelRegionId']/option[@value='2366']"
批量解除搜索房间="//a[@id='cancelFilterOkBtn']"
批量解除下一步="//div[@id='btnCancelChargeItemSettingWindow']//div[@class='form-wizard']/div[1]/div/div/a[2]"
批量解除确认下一步="//div[@id='btnCancelChargeItemSettingWindow']//div[@class='form-wizard']/div[1]/div/div/a[3]"
修改解除确认解除="//div[@id='batchCancelConfirmModal']//button[@id='batchCancelConfirmBtn']"
批量解除关闭="//div[@id='btnCancelChargeItemSettingWindow']//a[@class='btn button-cancel default']"

###左侧树操作
搜索房间代码="//input[@id='txtSerachTerm']"
####编辑收费标准
编辑绑定收费标准="//div[@id='gridChargeItem']//tbody/tr[1]/td[3]/a[1]"
勾选修改开始时间="//span/input[@id='batchEditStartDateCheckBox']"
单击编辑开始时间输入框="//input[@id='batchEditStartDate']"
选择编辑开始日期="//div[@class='datetimepicker datetimepicker-dropdown-top-left dropdown-menu'][1]//tr[4]/td[@class='day'][3]"
单击编辑保存="//button[@id='batchRoomEditWindowConfim']"
解除绑定按钮="//div[@id='gridChargeItem']//tbody/tr[1]/td[3]/a[2]"
确认编辑="//div[@class='modal-dialog']//button[@class='btn btn-primary']"
确认解除="//button[@id='batchRoomCancelConfim']"

###断言
绑定收费标准成功="//font[text()='绑定收费标准成功！']"
批量修改收费标准成功="//span[@id='batchEditResult' and text()='批量修改成功!']"
批量解除成功="//span[@id='batchCancelSuccess']"

##设置制动账单生成
每月自动生成日1="//select[@id='Day1']"
生成日1选择5号="//select[@id='Day1']/option[6]"
每月自动生成日2="//select[@id='Day2']"
生成日2选择5号="//select[@id='Day2']/option[6]"
预存款自动冲抵日="//select[@id='PreDay']"
自动冲抵日选择5号="//select[@id='PreDay']/option[6]"
保存自动生成账单="//button[@id='btnSave']"
配置成功提示="//font[text()='配置成功！']"
配置成功页面确定="//div[@class='modal-dialog']//button[@class='btn btn-primary']"






