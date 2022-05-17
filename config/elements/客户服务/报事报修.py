'''
报事报修
'''
#通用定位按钮
搜索框="//input[@placeholder='搜索...']"
搜索按钮="//span[@class='ant-input-suffix']/i"
保存="//div[@class='ant-modal-footer']//button[2]"
取消="//button/span[text()='取 消']/.."
确认删除="//div[@class='ant-popover-buttons']/button[2]"
新建="//div[@class='ant-tabs ant-tabs-top ant-tabs-line']//div[@role='tabpanel'and @aria-hidden='false']//button/span[text()='新 建']/.."
导出Excel="//button/span[text()='导出Excel']/.."
批量删除="//button/span[text()='批量删除']/.."
派工="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='派工']"
编辑="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='编辑']"
删除="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='删除']"
更多="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='更多 ']"
列表第一个复选框="//tbody/tr/td[1]/span/label/span"
高级搜索="//button/span[text()='查 询']/.."
列表元素="//tbody/tr[1]/td[1]"

#断言
保存成功="//span[text()='保存成功']"
新建成功="//span[text()='新建成功']"
删除成功="//span[text()='删除成功!成功条数【1】']"


'''
工单设置
'''
#工单大类
工单类型管理tab="//div[text()='工单类型管理']"
工单大类第一个数据="//div[@class='ant-col ant-col-6']//ul/li[1]"
工单大类新增="//a/i[@title='新增']"
工单名称="id=name"
工单编号="id=code"
删除工单大类="//ul/li/span[text()='服务家政']/..//a/i[@title='删除']"
编辑工单大类="//ul/li/span[text()='服务家政']/..//a/i[@title='编辑']"
#工单子类
工单子类编辑="//tbody/tr[1]/td/a[text()='编辑']"
工单子类勾选第一个="//tbody/tr[1]/td[1]/span"
工单时限管理tab="//div[text()='工单时限管理']"
工单处理时限设置tab="//div[text()='工单处理时限设置']"
工单时限编辑="//tbody/tr[1]/td//a[text()='编辑']"
工单时限删除="//tbody/tr[1]/td//a[text()='删除']"
工单时限名称="id=name"
工单时限编号="id=code"
工单时限工时="id=hours"
工单时限备注="id=remark"
工单时限搜索="//div[@class='ant-tabs ant-tabs-top ant-tabs-line']//div[@role='tabpanel'and @aria-hidden='false']//input[@placeholder='搜索...']"
工单时限搜索按钮="//div[@class='ant-tabs ant-tabs-top ant-tabs-line']//div[@role='tabpanel'and @aria-hidden='false']//span[@class='ant-input-suffix']/i"

功能设置tab="//div[text()='功能设置']"

#断言
操作成功="//span[text()='操作成功!']"
工单时限删除成功="//span[text()='删除成功!']"

'''
报修管理、待我跟进的报修单
'''

#报修管理
新建报修="//button/span[text()='新建报修']/.."
报修_公区单选框="//span[text()='公区']/../span[1]"
报修_报修位置="id=organizationItemIds"
报修_报修位置_管理区="//ul[@class='ant-cascader-menu']/li[1]"
报修_报修位置_楼宇="//ul[@class='ant-cascader-menu'][2]/li[1]"
报修_报修位置_房间="//ul[@class='ant-cascader-menu'][3]/li[1]"
报修_报修地点="id=place"
报修_报修详情="id=details"
报修_报修人="//div[@class='ant-modal-body']//input[@id='customerName']"
报修_联系电话="id=phone"
报修_预约时间="id=appointmentTime"
报修_预约时间_此刻="//a[text()='此刻']"
报修_报修来源="id=serviceSource"
报修_报修来源_上门="//ul/li[text()='上门']"
报修_工单时限="id=dispatchPriorityId"
报修_工单时限选择="//li[text()='8小时内处理（适用于一般单）']"
报修_工单大类="id=dispatchTypeParentId"
报修_工单大类_报修业务="//li[text()='报修业务']"
报修_工单子类="//div[@class='ant-modal-body']//div[@id='dispatchTypeId']"
报修_工单子类_一般单="//li[text()='一般单']"
报修_完结="//div[@class='ant-modal-footer']//button[3]"
报修_派工="//div[@class='ant-modal-footer']//button[4]"
保存并关闭工单="//button/span[text()='保存并关闭工单']/.."
#报修状态
报修状态_全部="//h3[text()='状态:']/../span[text()='全部']"
报修状态_待分派="//h3[text()='状态:']/../span[text()='待分派']"
报修状态_已分配="//h3[text()='状态:']/../span[text()='已分配']"
报修状态_处理中="//h3[text()='状态:']/../span[text()='处理中']"
报修状态_已处理="//h3[text()='状态:']/../span[text()='已处理']"
报修状态_已确认已完成="//h3[text()='状态:']/../span[text()='已确认已完成']"
报修状态_已确认未完成="//h3[text()='状态:']/../span[text()='已确认未完成']"
报修状态_已关闭="//h3[text()='状态:']/../span[text()='已关闭']"
报修状态_已作废="//h3[text()='状态:']/../span[text()='已作废']"
报修状态_已撤销="//h3[text()='状态:']/../span[text()='已撤销']"
#报修列表
报修_列表报修人="//tbody/tr[1]/td[3]/span"
报修_列表报修来源="//tbody/tr[1]/td[11]/span"
报修_列表报修业务="//tbody/tr[1]/td[9]/span"
报修_列表报修单号="//tbody/tr[1]/td[1]/a[@title]"
报修_获取报修单号="//tbody/tr[1]/td[1]/a[@title]/span"
报修_关闭查看页面="//i[@class='anticon anticon-close']"
报修_查看页面_编辑="//button/span[text()='编 辑']/.."
报修_查看页面_派工="//button/span[text()='派 工']/.."
报修_查看页面_完成="//button/span[text()='完 结']/.."
报修_查看页面_添加说明="//button/span[text()='添加说明']/.."
报修_查看页面title="//span[text()='报修详情']"
添加作废说明详情="id=remark"

#待分派的报修单-更多操作下的按钮定位
报修_转交="//ul[@role='menu' and @tabindex]/li/a[text()='转交']"
报修_更多_添加说明="//ul[@role='menu' and @tabindex]/li/a[text()='添加说明']"
报修_更多_作废="//ul[@role='menu' and @tabindex]/li/a[text()='作废']"
工单_更多_打印派工单="//ul[@role='menu' and @tabindex]/li/a[text()='打印派工单']"
#确定完成的报修单
报修_回访="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='回访']"
报修_添加说明="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='添加说明']"
报修_作废="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='作废']"
报修_启用="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='启用']"
报修_派工类型="id=chargeType"
报修_派工类型_无偿="//li[text()='无偿服务']"
报修_指派给="id=assigneeIds"
报修_指派给_testing="//li[text()='testing']"

报修_回访对象="id=returnVisitPerson"
报修_访问电话="id=returnVisitPhone"
报修_评价="id=Comment"
报修_评价_满意="//ul[@role='listbox']/li[1]"
报修_评价内容="id=CommentContent"
报修_转交给="id=regionId"
报修_转交选择管理区数据="//ul[@role='listbox']/li[1]"
#报修高级搜索
报修_搜索更多="//span[text()='更多 ']"
报修_搜索_报修来源="id=repairSource"
报修_搜索_工单大类="id=dispatchTypeId"
报修_报修单号="id=voucherNo"
#断言
派工成功="//span[text()='派工成功']"
启用成功="//span[text()='启用报修单成功！']"

'''
派工单管理
'''
#派工单管理list
回退="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='回退']"
开始处理="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='开始处理']"
回单="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='回单']"
确认="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='确认']"
打印派工单="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='打印派工单']"
工单_列表报派工单号="//tbody/tr[1]/td[1]/a[@title]"
工单_获取报派工单号="//tbody/tr[1]/td[1]/a[@title]/span"
#工单状态
工单状态_全部="//h3[text()='状态:']/../span[text()='全部']"
工单状态_待开始="//h3[text()='状态:']/../span[text()='待开始']"
工单状态_进行中="//h3[text()='状态:']/../span[text()='进行中']"
工单状态_已处理="//h3[text()='状态:']/../span[text()='已处理']"
工单状态_已确认已完成="//h3[text()='状态:']/../span[text()='已确认已完成']"
工单状态_已确认未完成="//h3[text()='状态:']/../span[text()='已确认未完成']"
工单状态_已关闭="//h3[text()='状态:']/../span[text()='已关闭']"
工单状态_已作废="//h3[text()='状态:']/../span[text()='已作废']"
#工单查看页面
工单_新工单时限="id=extendTime"
工单_申请原因="id=requestReason"
工单_完工说明="id=processRemark"
工单_已完成="//div[@id='completeStatus']/label[1]/span[1]"
工单_未完成="//div[@id='completeStatus']/label[2]/span[1]"
工单_完成情况说明="id=remark"
工单_查看页面_编辑="//button/span[text()='编 辑']/.."
工单_查看页面_领料="//button/span[text()='领 料']/.."
工单_查看页面_退料="//button/span[text()='退 料']/.."
工单_查看页面_添加费用="//button/span[text()='添加费用']/.."
工单_查看页面_添加说明="//button/span[text()='添加说明']/.."
工单_查看页面_延时申请="//button/span[text()='延时申请']/.."
工单_查看页面_回单="//button/span[text()='回 单']/.."
工单_查看页面_收费="//button/span[text()='收 费']/.."
工单_查看页面_领料材料="//div[@class='ant-modal-body']/div/div[2]//tbody/tr[1]/td[1]/span"
工单_查看页面_领料数量="//td[@class='ant-table-row-cell-break-word'][6]//input"
工单_查看页面_退料数量="//tbody/tr[1]//div[@class='ant-input-number']//input"
#派工单高级搜索
工单_查询_派工单号="id=dispatchingNo"
工单_打印="//button/span[text()='打 印']"
工单_取消打印="//button/span[text()='取 消']"

#断言
作废派工单成功="//span[text()='作废派工单成功！']"
启用派工单成功="//span[text()='启用派工单成功！']"
延时申请成功="//span[text()='延时申请成功！']"

#维修延时审批
维修_进入查看页面="//tbody/tr[1]/td[2]/a[@title]"
维修_同意="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='同意']"
维修_拒绝="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='拒绝']"
维修_拒绝原因="id=reason"
维修_审批中="//h3[text()='状态:']/../span[text()='审批中']"
#断言


#及时率报表

#汇总统计

#投诉建议
