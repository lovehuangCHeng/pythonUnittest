#弹框
提示框关闭="xpath==//button[@aria-label='Close']"
#首页
用户名="id==UserName"
密码="id==Password"
立即登录="xpath==//button"
设置首页="xpath==//a[@style='float: right;']"
设置首页重置="xpath==//div[@class='ant-modal-footer']/button[1]"
设置首页确定="xpath==//div[@class='ant-modal-footer']/button[2]"
设置首页全选="xpath==//thead/tr/th[1]"
##房产管理
#物业资源管理
物业资源搜索框="xpath==//input[@placeholder='编号/名称（分公司/管理区/楼栋/停车场）']"
物业资源搜索="xpath==//span[@class ='ant-input-wrapper ant-input-group' ]/span[2]/button"
资源树管理区="xpath=="
添加下级="xpath==//button/span[text()='新建(分组/楼宇/单元/停车场)']/.. "
取消删除="xpath==//div[@class='ant-popover-buttons']/button[1]"
确认删除="xpath==//div[@class='ant-popover-buttons']/button[2]"
导出Excel="xpath==//div[@role='tabpanel'and@aria-hidden='false']/div/div/div/button/span[text()='导出Excel']"
搜索框="xpath==//div[@role='tabpanel'and@aria-hidden='false']/div/div/div[2]/span/input"
搜索按钮="xpath==//div[@role='tabpanel'and@aria-hidden='false']/div/div/div[2]/span/span"
查看页面title="xpath==//div[@class='ant-drawer-title']"
查看页面关闭按钮="xpath==//button[@class='ant-drawer-close']"
提示信息="xpath==//div[@class='ant-message']//div/span"
#总公司层级定位3个tab页面，房间、车位、广告位,返回的是数组需要处理。
房间tab="xpath==//div[@id='rc-tabs-1-tab-5']"
车位tab="xpath==//div[@id='rc-tabs-1-tab-7']"
广告位tab="xpath==//div[@id='rc-tabs-1-tab-10']"
#分组的按钮
添加分组="xpath==//li/span[text()='分组']"
上级机构="id==parentId"
上级机构数据="//div[@class='ant-select-tree-list-holder-inner']/div[1]/span[3]"
分组名称="xpath==//input[@id='name']"
分组地址="xpath==//textarea[@id='address']"
分组说明="xpath==//textarea[@id='remark']"
分组确定="xpath==//div[@class='ant-modal-footer']//button[2]"
#楼宇的元素
添加楼栋="xpath==//li/span[text()='楼宇']"
楼宇名称="xpath==//input[@id='name']"
楼宇序号="xpath==//input[@id='code']"
楼宇层数="xpath==//input[@id='floors']"
楼宇备注="xpath==//textarea[@id='remark']"
楼宇取消="xpath==//div[@class='ant-modal-footer']//button[1]"
楼宇确定="xpath==//div[@class='ant-modal-footer']//button[2]"
#停车场元素
添加停车场="xpath==//li/span[text()='停车场']"
停车场名称="xpath==//input[@id='carbarnName']"
停车场地址="xpath==//textarea[@id='address']"
停车场说明="xpath==//textarea[@id='remark']"
停车场取消="xpath==//div[@class='ant-modal-footer']//button[1]"
停车场确定="xpath==//div[@class='ant-modal-footer']//button[2]"
#房间
选择房间上级机构数据="xapth==//div[@class='ant-select-tree-list-holder-inner']/div[2]/span[3]"
新建房间="xpath==//button/span[text()='新建房间']/.."
房间编辑="xpath==//tr[2]//a[text()='编辑']"
房间删除="xpath==//tr[2]//a[text()='删除']"
房间拆分="xpath==//tr[2]//a[text()='拆分']"
房间禁用="xpath==//tr[2]//a[text()='禁用']"
房间绑定收费标准="xpath==//tr[2]//a[text()='绑定收费标准']"
绑定收费标准关闭="xpath==//button[@class='ant-modal-close']"
房间查看="xpath==//tbody/tr[2]/td[4]//a"
房间查看页面关闭="xpath==//div/span[@class='anticon anticon-close']"
业主管理="xpath==//div[@class='ant-tabs-extra-content']/button"
迁入业主="xpath==//button/span[text()='迁入业主']"
#迁出="xpath==//tr[1]/td[4]//a[text()='迁出']"
租户tab="xpath==//div/div[text()='租户']"
当前居住成员="xpath==//div[text()='当前居住成员']"
房间楼层="id==floor"
房间序号="id==rank"
房间代码="id==code"
房间建筑面积="id==coveredArea"
房间类型="id==houseTypeId"
办公="xpath==//li[text()='办公']"
房间状态="id==houseStatus"
交房="xpath==//li[text()='交房']"
#车位
车位tab="xpath==//div[@class='ant-spin-container']//div[@class='ant-tabs-nav-scroll']/div/div/div[5]"
添加车位="xpath==//div[@class='drawer-top-bar']//button[2]"
车位查看="xpath==//div[@class='ant-spin-container']/div/div[3]/div[@aria-hidden='false']//tbody/tr[1]/td[2]//a"
车位编辑="xpath==//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]//a[text()='编辑']"
车位删除="xpath==//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]//a[text()='删除']"
绑定业主="xpath==//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]//a[text()='绑定业主']"
车位号="xpath==//input[@id='parkingPlaceNumber']"
车位面积="xpath==//input[@id='parkingArea']"
车位业主="xpath==//div[@id='ownerId']"                      
车牌号1="id==licensePlateNumberOne"
#广告位
广告位tab="xpath==//div[@class='ant-spin-container']//div[@class='ant-tabs-nav-scroll']/div/div/div[6]"
添加广告位="xpath==//li[text()='添加广告位']"
编辑广告位="xpath==//div[@class='ant-spin-container']/div/div[3]/div[@aria-hidden='false']//tbody/tr[1]/td[7]//a[1]"
删除广告位="xpath==//div[@role='tabpanel'and@aria-hidden='false']//tbody/tr[1]/td[7]//a[2]"
查看广告位="xpath==//div[@role='tabpanel'and@aria-hidden='false']//tbody/tr[1]/td[5]/a"
广告位号="xpath==//input[@id='code']"
广告位楼层="xpath==//input[@id='floor']"
已出租="xpath==//span[text()='已出租']"
未出租="xpath==//span[text()='未出租']"
#单元
添加单元="xpath==//li/span[text()='单元']"
删除单元="xpath==//div[@class='title___PhrXt']//button[2]"
编辑单元="xpath==//div[@class='title___PhrXt']//button[1]"
单元名称="id==name"
单元序号="id==code"
#断言
删除成功断言="xpath==//div[@class='ant-message-custom-content ant-message-success']/span"
楼宇名称断言="xpath==//div[@role='tabpanel'and @aria-hidden='false']//tbody/tr[1]/td[3]//a"
停车场名称断言="xpath==//div[@role='tabpanel'and @aria-hidden='false']//tbody/tr[1]/td[3]//a"
房间代码断言="xpath==//tbody/tr[1]/td[4]//a"
车位号断言="xpath==//tbody/tr[1]/td[2]//a"
广告位号断言="xpath==//div[@role='tabpanel'and@aria-hidden='false']//tbody/tr[1]/td[5]/a"
#资源平面图
关闭平面图查看="xpath==//i[@class='anticon anticon-close']"
资源导出Excel="xpath==//button/span"
房间链接="xpath==//div[@class='floorBorder___2zapF'][1]//a[1]/div"
资源查看title="xpath==//div[@class='ant-drawer-title']//span"
#房产状态统计
房产状态导出Excel="id==btnExport"
房产状态输入框="id==searchTerm"
房产状态输入框搜索="id==btnFilter"
高级向下展开按钮="xpath==//div[@class='input-group-btn']/button[2]"
高级向上展开按钮="xpath==//div[@class='form-horizontal']//button[3]"
高级搜索确定按钮="id==btnFilterDetail"
#房产管理员
绑定="xpath==//button"
绑定页面标签="id==rcDialogTitle0"
房产管理员="xpath==//div[@class='ant-modal-body']//div[@class='ant-select-selection__placeholder']"
admin员工="xpath==//li[text()='admin']"
管理区范围="xpath==//div[@class='ant-spin-container']/span/input"
管理区范围搜索按钮="xpath==//div[@class='ant-spin-container']/span/span/i[2]"
第一个管理区="xpath==//ul[@role='tree']/li[1]/span[2]"
绑定编辑="xpath==//tbody/tr[1]/td[4]//a[1]"
解绑="xpath==//tbody/tr[1]/td[4]//a[2]"
表头房产管理员="xpath==//thead//th[2]/span//span[1]"
#微信绑定状态统计
按房间统计tab="xpath==//div[text()='按房间统计']"
按客户统计tab="xpath==//div[text()='按客户统计']"
微信绑定_管理区选择框="xpath==//div[@id='filterRegion']/div/div"
微信绑定_选择管理区数据="xpath==//ul[@role='listbox']/li[1]"
微信绑定_楼宇输入框="xpath==//div[text()='请选择楼宇']"
微信绑定_查询="xpath==//button/span[text()='查 询']/.."
微信绑定_客户查询="xpath==//div[@role='tabpanel']//div[@role='tabpanel'][2]//button/span[text()='查 询']/.."
微信绑定_重置="xpath==//button/span[text()='重 置']/.."
微信绑定_导出Excel="xpath==//button/span[text()='导出Excel']/.."
查看绑定信息="xpath==//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/a"
微信绑定_详情页面_房间title="xpath==//span[text()='房间绑定信息']"
微信绑定_详情页面_客户title="xpath==//span[text()='客户绑定信息']"
微信绑定_关闭详情页面="xpath==//i[@class='anticon anticon-close']" 
微信绑定_管理区选择框_客户="xpath==//div[@id='filterRegionByCustomer']/div/div"
微信绑定_查看绑定信息_客户="xpath==//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/a[@title='客户绑定信息']"
#车位状态统计
车位状态_选择管理区="xpath==//span[text()='请选择管理区']"
车位状态_查询="xpath==//button/span[text()='搜 索']/.."
车位状态_重置="xpath==//button/span[text()='重 置']/.."
车位状态_导出Excel="xpath==//button/span[text()='导出EXCEL']/.."
车位状态_合计汇总超链接="xpath==//div[@class='ant-table-footer']//td[3]/a/div"
车位状态_明细页面title="xpath==//span[text()='车位状态统计明细']"
车位状态_明细页面_导出="xpath==//div[@class='ant-drawer-wrapper-body']//button"
车位状态_楼宇停车场="xpath==//span[text()='请选择楼宇/停车场']"
车位状态_选择停车场="xpath==//div[@id='rc-tree-select-list_2']//li/ul/li[1]/span[2]"
#房间绑定业主状态统计
房间绑定_选择管理区="xpath==//span[text()='请选择管理区']"
房间绑定_查询="xpath==//button/span[text()='搜 索']/.."
房间绑定_重置="xpath==//button/span[text()='重 置']/.."
房间绑定_导出Excel="xpath==//button/span[text()='导出Excel']/.."
房间绑定_合计汇总超链接="xpath==//div[@class='ant-table-footer']//td[4]/a/div"
房间绑定_明细页面title="xpath==//span[text()='房间绑定业主状态统计明细']"
房间绑定_明细页面_导出="xpath==//div[@class='ant-drawer-wrapper-body']//button"
房间绑定_楼宇用途数据="xpath==//li[text()='住宅用途']"
房间绑定_楼宇用途="xpath==//div[text()='请选择楼宇用途']"
房间绑定_楼宇数据="xpath==//div[@id='rc-tree-select-list_2']//li/ul/li[1]/span[2]"
房间绑定_楼宇="xpath==//span[text()='请选择楼宇']"