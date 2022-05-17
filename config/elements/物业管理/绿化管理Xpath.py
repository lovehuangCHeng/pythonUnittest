# Can be used in the test data like ${MyObject()} or ${MyObject(1)}

'''
绿化区域
'''
#新建绿化区域
绿化区域新建按钮="//span[text()='新 建']/.."
选择管理区下拉="//div[@id='regionId']//div[@class='ant-select-selection__rendered']"
选择第一个管理区="//ul[@role='listbox']/li[1]"
区域代码输入框="//input[@id='code']"
区域名称输入框="//input[@id='name']"
责任人下拉="//div[@id='staffId']/div"
选择第一个责任人="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
确认按钮="//span[text()='确 定']/.."
操作成功断言="//div[@class='ant-message-custom-content ant-message-success']/span"
#查看编辑删除
查看按钮="//tr[1]/td[@class='ant-table-row-cell-break-word']/span/a[1]"
编辑按钮="//tr[1]/td[@class='ant-table-row-cell-break-word']/span/a[2]"
删除按钮="//tr[1]/td[@class='ant-table-row-cell-break-word']/span/a[3]"
二次确认="//div[@class='ant-popover-buttons']/button[@class='ant-btn ant-btn-primary ant-btn-sm']"
取消按钮="//span[text()='取 消']/.."

'''
绿化植被等级
'''
#新建绿化植被
绿化植被新建按钮="//span[text()='新 建']/.."
绿化植被选择管理区下拉="//div[@id='regionId']//div[@class='ant-select-selection__rendered']"
绿化植被选择第一个管理区="//ul[@role='listbox']/li[1]"
绿化植被名称输入框="//input[@id='name']"
绿化植被数量输入框="//input[@id='quantity']"
绿化植被区域下拉="//div[@id='greeningAreaId']//div[@class='ant-select-selection__placeholder']"
绿化植被第一个区域="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
绿化养护要求="//input[@id='maintenanceRequirements']"
绿化植被区域新建确定="//span[text()='确 定']/.."

#绿化事件记录
绿化事件新建按钮="//span[text()='新 建']/.."
绿化事件选择管理区下拉="//div[@id='regionId']//div[@class='ant-select-selection__rendered']"
绿化事件选择第一个管理区="//ul[@role='listbox']/li[1]"
绿化事件名称输入框="//input[@id='name']"
绿化事件类型下拉="//div[@id='greeningMaintenanceTypeId']//div"
绿化事件第一个类型="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
绿化事件区域下拉="//div[@id='greeningAreaId']//div"
绿化事件第一个区域="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][3]//ul[@role='listbox']/li[1]"
绿化事件负责人="//div[@id='staffId']/div"
绿化事件第一个负责人="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][4]//ul[@role='listbox']/li[1]"
绿化事件开始时间选择="//span[@id='startDate']//input"
绿化事件开始时间="//div[7]//tr[2]/td[4]"
绿化事件结束时间选择="//span[@id='endDate']/div/input"
绿化事件结束时间="//div[8]//tr[3]/td[4]"
绿化事件具体内容="//textarea[@id='details']"
绿化事件状态下拉="//div[@id='status']//div[@class='ant-select-selection__rendered']"
绿化事件选择计划中="//li[text()='计划中']"
绿化事件区域新建确定="//span[text()='确 定']/.."

#绿化工作检查
绿化工作新建按钮="//span[text()='新 建']/.."
绿化工作选择管理区下拉="//div[@id='regionId']//div[@class='ant-select-selection__rendered']"
绿化工作选择第一个管理区="//ul[@role='listbox']/li[1]"
绿化工作区域下拉="//div[@id='greeningAreaId']//div[@class='ant-select-selection__placeholder']"
绿化工作第一个区域="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"

绿化工作负责人="//div[@id='responsiblePersonId']//div[@class='ant-select-selection__rendered']"
绿化工作第一个负责人="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][3]//ul[@role='listbox']/li[1]"

绿化工作检查人="//div[@id='inspectionPersonId']//div[@class='ant-select-selection__rendered']"
绿化工作第一个检查人="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][4]//ul[@role='listbox']/li[1]"

绿化工作检查时间="//span[@id='inspectionDate']//input"
绿化工作检查时间选择="//tr[@class='ant-calendar-current-week ant-calendar-active-week']/td[1]/div[@class='ant-calendar-date']"

绿化工作检查情况="//input[@id='inspectionResults']"
绿化工作检查结果下拉="//div[@id='status']//div[@class='ant-select-selection__placeholder']"
绿化工作检查结果="//li[text()='合格']"
绿化植被新建确定="//span[text()='确 定']/.."

绿化工作备注文本框="//textarea[@id='remark']"

#通用
搜索框="//input[@placeholder='搜索...']"
搜索="//input[@placeholder='搜索...']/../span/i"

