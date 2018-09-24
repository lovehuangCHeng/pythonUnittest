#coding=utf-8
import  os
import  unittest
import HTMLTestRunner
from case import test_bascinfo,test_logincase

long=unittest.TestLoader().loadTestsFromTestCase(test_logincase.LoginCase)
base=unittest.TestLoader().loadTestsFromTestCase(test_bascinfo.BascinfoCase)
smok_test=unittest.TestSuite([long,base])
#用例路径
# case_path=os.path.join(os.getcwd(),"case")
# #报告存放路径
# report_path=os.path.join(os.getcwd(),"report")
# def all_case():
#      discover=unittest.defaultTestLoader.discover(case_path,
#                                                   pattern="test*.py",
#                                                   top_level_dir=None
#                                                   )
#      print(discover)
#      return (discover)

if __name__=="__main__":
     fp=open(os.getcwd()+"\\result.html","wb")
     runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'这个测试报告',description=u'这是测试用例')
     runner.run(smok_test)
     fp.close()