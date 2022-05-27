#coding=utf-8
import  unittest
from handle.handleWuYeScores import louyuHandle as ly
class Test_BascinfoCase(unittest.TestCase):
     url=ly.khda_url
     lp =ly()
     @classmethod
     def setUpClass(cls):
          cls.lp.geturl(cls.url)
          cls.lp.setCookie()
          cls.lp.geturl(cls.url)


     @classmethod
     def tearDownClass(cls):
          cls.lp.quet()



