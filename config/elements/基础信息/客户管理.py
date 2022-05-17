# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index

'''
客户档案页面
'''
客户新建="//button/span[text()='新 增']/.."
客户编辑="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]//a[1]"
客户删除="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]//a[2]"
合并重名客户="//button/span[text()='合并重名客户']/.."
客户档案导出Excel="//button/span[text()='导出Excel']/.."
客户档案搜索框="//input[@placeholder='名称/联系电话']"
客户档案搜索按钮="//span[@class='ant-input-suffix']"
客户向下展开按钮="//a[text()='高级搜索']"
客户向上展开按钮="//a[text()='收起搜索']"
高级搜索按钮="//button/span[text()='搜 索']/.."
高级搜索重置="//button/span[text()='重 置']/.."
选择管理区="id=regionId"
管理区数据="//ul[@role='listbox']/li[1]"
客户名称="id=name"
客户性别男="//div[@id='sex']/label[1]/span[1]"
客户档案保存="//div[@class='ant-modal-footer']/button[2]"
表格中管理区数据="//tbody/tr[1]/td[1]//input"
确认删除按钮="//div[@class='ant-popover-buttons']/button[2]"
合并同名客户title="id=rcDialogTitle0"
关闭合并同名客户="xpath=//div[@class='ant-modal-content']/button"
电话号码="id=phone"
弹框确定="xpath=//div[@class='modal-footer']/button"
#断言
客户档案断言="//span[text()='保存成功！']"
客户名称断言="//tbody/tr[1]/td[4]/span"
删除成功="//span[text()='删除成功!成功条数【1】']"
'''
委员会成员
'''
新增成员="xpath=//div[@class='ListButton___2jlS-']/div/div/button"
委员会批量删除="xpath=//div[@class='ListButton___2jlS-']/div/div/span"
委员会选择管理区="xpath=//div[@class='ListButton___2jlS-']/div/div[2]//i"
委员会管理区数据="xpath=//ul[@role='listbox']/li[last()]"
委会会查看="xpath=//tbody/tr[1]/td[10]//a[1]"
委会会编辑="xpath=//tbody/tr[1]/td[10]//a[2]"
委会会删除="xpath=//tbody/tr[1]/td[10]//a[3]"
#委员会新建页面元素
委员会编号="id=number"
委员会管理区="id=organizationItemId"
委员会确定="//div[@class='ant-modal-footer']//button[2]"
委员会取消="//div[@class='ant-modal-footer']//button[1]"


