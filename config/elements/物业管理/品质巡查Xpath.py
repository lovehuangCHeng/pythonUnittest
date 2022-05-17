# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
'''
通用
'''
新建按钮="//span[text()='新 建']/.."
保存按钮="//span[text()='保 存']/.."
编辑按钮="//tr[1]/td[@class='ant-table-row-cell-break-word']/span//a[text()='编辑']"
删除按钮="//tr[1]/td[@class='ant-table-row-cell-break-word']/span//a[text()='删除']"
禁用按钮="//tr[1]/td[@class='ant-table-row-cell-break-word']/span//a[text()='禁用']"
复制按钮="//tr[1]/td[@class='ant-table-row-cell-break-word']/span//a[text()='复制']"
启用按钮="//tr[1]/td[@class='ant-table-row-cell-break-word']/span//a[text()='启用']"
停用按钮="//tr[1]/td[@class='ant-table-row-cell-break-word']/span//a[text()='停用']"

删除二次确认按钮="//div[text()='']/../..//span[text()='确 定']/.."
禁用二次确认按钮="//div[text()='']/../..//span[text()='确 定']/.."
停用二次确认按钮="//div[text()='']/../..//span[text()='确 定']/.."
启用二次确认按钮="//div[text()='']/../..//span[text()='确 定']/.."

普通搜索框="//input[@placeholder='搜索...']"
普通搜索="//input[@placeholder='搜索...']/../span/i"
高级搜索="//a[@class='seniorSearchBtn']"

全部状态="//span[text()='全部']"
未解决状态="//span[text()='未解决']"
已解决状态="//span[text()='已解决']"
未开始状态="//span[text()='未开始']"
待处理状态="//span[text()='待处理']"
处理中状态="//span[text()='处理中']"
正常完成状态="//span[text()='正常完成']"
超时完成状态="//span[text()='超时完成']"


'''
巡查类别
'''
#新建巡查类别
巡查类别名称输入框="//input[@id='name']"
巡查类别说明="//textarea[@id='remark']"

'''
巡查事项
'''
#新建巡查类别
巡查事项名称输入框="//input[@id='name']"
巡查类别下拉="//div[text()='请选择巡查类别']/.."
选择第一个类别="//div[3]//ul[@role='listbox']/li[1]"
级别删除="//input[@placeholder='请输入分值']/../../../../../../../..//a[text()='删除']"
级别添加="//a[text()='+添加']"
一级检查内容输入="//textarea[@id='items_0_content']"
一级检查方法输入="//textarea[@id='items_0_checkMethod']"
一级评分标准输入="//textarea[@id='items_0_scoreItems']"
一级分值输入="//input[@id='items_0_score']"

'''
巡查计划
'''
#新建巡查计划
管理区下拉="//div[@id='regionIds']//div[@class='ant-select-selection__placeholder']"
选择第一个管理区="//div[3]//ul[@role='listbox']/li[1]"
巡更计划名称输入框="//input[@id='name']"
经办人下拉="//div[@id='handlerId']//div[@class='ant-select-selection__rendered']"
选择第一个经办人="//div[4]//ul[@role='listbox']/li[1]"
巡查次数输入框="//input[@id='times']"
任务开始时间="//td[2]//input[@class='ant-time-picker-input']"
选择任务开始时间1="//div[5]//div[@class='ant-time-picker-panel-combobox']/div[1]//li[@class='ant-time-picker-panel-select-option-selected']"
选择任务开始时间2="//div[5]//div[@class='ant-time-picker-panel-combobox']/div[2//li[@class='ant-time-picker-panel-select-option-selected']"
选择任务结束时间1="//div[6]//div[@class='ant-time-picker-panel-combobox']/div[1]//li[@class='ant-time-picker-panel-select-option-selected']"
选择任务结束时间2="//div[6]//div[@class='ant-time-picker-panel-combobox']/div[2]//li[@class='ant-time-picker-panel-select-option-selected']"
任务结束时间="//td[3]//input[@class='ant-time-picker-input']"
巡查事项下拉="//span[text()='请选择巡查事项']/.."
选择第一个巡查事项="//div[7]//li[1]/span[@class='ant-select-tree-checkbox']/span"
#高级搜索

'''
巡查任务
'''
#新建巡查类别
任务计划开始时间="//span[@id='planTime']/span/i"
任务计划结束时间="//span[@id='planTime']//input[2]"
选择开始时间="//div[@class='ant-calendar-range-part ant-calendar-range-left']//table[@role='grid']//tr[1]/td[1]/div"
选择结束时间="//div[@class='ant-calendar-range-part ant-calendar-range-right']//table[@role='grid']//tr[1]/td[1]/div"
确定选择日期="//a[@role='button'and text()='确 定']"
经办人下拉2="//div[@id='handlerId']//div[@class='ant-select-selection__rendered']"
择第一个经办人2="//div[5]//ul[@role='listbox']/li[1]"
巡查事项下拉2="//span[text()='请选择巡查事项']/.."
选择第一个巡查事项2="//div[6]//ul[@class='ant-select-tree']/li[1]/span[@class='ant-select-tree-checkbox']/span"
#高级搜索
任务名称输入框="//input[@placeholder='请输入任务名称']"
时间删除图标="//label[text()='计划开始日期']/../..//span//i"

'''
巡查任务
'''
#巡查问题
提交日期="//label[text()='提交日期']/../..//input[1]"
选择开始时间2="//div[@class='ant-calendar-range-part ant-calendar-range-left']//table[@role='grid']//tr[1]/td[1]/div"
选择结束时间2="//div[@class='ant-calendar-range-part ant-calendar-range-right']//table[@role='grid']//tr[1]/td[1]/div"
查询按钮="//span[text()='查 询']/.."










