'''
仪表类型 模块
'''
仪表类型新增="xpath==//button/span[text()='新 增']/.."
仪表类型编辑="xpath==//a[text()='编辑']"
仪表类型删除="xpath==//a[text()='删除']"
仪表类型名称="id==name"
计量单位="id==unit"
仪表类型保存="xpath==//div[@class='ant-modal-footer']/button[2]"
仪表类型取消="xpath==//div[@class='ant-modal-footer']/button[1]"
仪表类型搜索框="xpath==//input[@placeholder='搜索...']"
仪表类型高级搜索框="xpath==//span[@class='ant-legacy-form-item-children']/input"
仪表类型搜索按钮="xpath==//button/span[@class='anticon anticon-search']/.."
仪表类型列表数据="xpath==//tbody/tr[1]/td[2]"
仪表类型高级搜索="xpath==//a[text()='高级搜索']"
仪表类型高级搜索按钮="xpath==//button/span[text()='搜 索']/.."
仪表类型高级重置="xpath==//button/span[text()='重 置']/.."
仪表类型确认删除="xpath==//div[@class='ant-popover-buttons']/button[2]"
#断言
更新仪表成功="xpath==//html/body/div[3]/div/div/div/div/div/span[2]"
创建仪表成功="xpath==//html/body/div[3]/div/div/div/div/div/span[2]"
仪表类型名称断言="xpath==//tbody/tr[1]/td[2]/span"
删除仪表类型="xpath==//div[@class='ant-message-custom-content ant-message-success']/span"
'''
房间仪表管理和公摊仪表管理通用的按钮定位
'''
房间仪表新增="id==btnNew"
仪表新建="id==btnAdd"
仪表编辑="id==btnEdit"
仪表删除="id==btnDelete"
仪表换表="id==btnChange"
仪表搜索框="id==searchTerm"
仪表搜索按钮="id==btnFilter"
仪表向下展开按钮="xpath==//div[@class='input-group-btn']/button[2]"
仪表向上展开按钮="xpath==//div[@class='form-horizontal']//button[3]"
仪表高级搜索按钮="id==btnFilterDetail"
仪表高级搜索重置="id==btnReset"
确认删除按钮="xpath==//div[@class='popover-content']/a[1]"
弹框确定="xpath==//div[@class='modal-footer']/button"
仪表房间列表="xpath==//tbody/tr[1]/td[1]"
换表取消按钮="xpath==//div[@class='form-actions']//a"
'''
房间仪表管理模块
'''
房间仪表批量添加="id==btnBatch"
房间仪表名称="id==Name"
房间仪表初始读数="id==InitialReading"
房间仪表保存="id==btnSave"
房间仪表倍率="id==Ratio"
房间仪表最大读数="id==MaxReading"
房间仪表类型="id==select2-MeterTypeId-container"
房间仪表初始日期="xpath==//span[@class='k-icon k-i-calendar']"
房间仪表选择日期="xpath==//div[@class='k-footer']/a"
房间仪表类型数据="xpath==//ul[@id='select2-MeterTypeId-results']/li[1]"
房间仪表房间="id==btnHouseIdToggleModal"
房间仪表房间代码="id==HouseId_HouseNumber"
房间仪表房间搜索按钮="id==HouseId_FilterButton"
房间仪表房间列表确定="id==btnHouseId"
房间仪表列表数据="xpath==//tbody/tr[1]/td[4]"
房间仪表批量添加取消="id==btnBack"
#断言
房间仪表断言="xpath==//div[@class='modal-content']/div/div[2]"
'''
公摊仪表管理模块
'''
公摊仪表名称="id==Name"
公摊仪表类型公摊表="xpath==//div[@id='radioForMeterType']/label[1]/div"
公摊仪表种类="id==select2-MeterTypeId-container"
仪表种类数据="xpath==//ul[@id='select2-MeterTypeId-results']/li[1]"
选择管理区="id==RegionId"
选择管理区数据="xpath==//select[@id='RegionId']/option[2]"
公摊仪表抄表日期按钮="xpath==//form[@id='PublicReterForm']//span[@class='k-icon k-i-calendar']"
选择上一个月公摊表抄表="xpath==//div[@id='LastReadDate_dateview']//span[@class='k-icon k-i-arrow-w']"
选择抄表日期="xpath==//div[@id='LastReadDate_dateview']//tr[1]/td[1]"
#断言
公摊仪表断言="xpath==//div[@class='modal-content']/div/div[2]" 