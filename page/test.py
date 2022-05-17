from config.elements.基础信息 import 房产档案
class pagetest:
    def getname(self):
        element=房产档案.设置首页
        print(element)
        return  element

test1=pagetest()
test1.getname()
