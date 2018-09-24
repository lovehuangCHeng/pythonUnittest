#coding=utf-8
import  unittest
import HTMLTestRunner

#用例路径
case_path="./case/"
# #报告存放路径
def all_case():
     discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py")
     sutie=unittest.TestSuite()
     sutie.addTest(discover)
     print(discover)
     return sutie
def discover_case():
     case_dir = "./case/"
     # 待执行用例的目录
     testcase = unittest.TestSuite()
     discover = unittest.defaultTestLoader.discover(case_dir, pattern="*.py", top_level_dir=None)
     # discover方法筛选出来的用例，循环添加到测试套件中
     print(discover)
     for test_suite in discover:
          for test_case in test_suite:
               print(test_case)
               # 添加用例到testcase
               # testcase.addTests(test_case)
               testcase.addTests(test_case)

     return (testcase)

if __name__=="__main__":
     #runner=unittest.TextTestRunner()
     fp=open("D:\\GIT\\python\\case\\result.html","wb")
     runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'这个测试报告',description=u'这是测试用例')
     runner.run(discover_case())
     fp.close()