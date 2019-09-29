#coding=utf-8
import unittest
from handle import handleWuYeScores
from case import baseCase

class sheBeiGuanli(unittest.TestCase):
    bc = baseCase.BaseCase()
    driver = bc.getDriver()
    lp = handleWuYeScores.louyu(driver)
    fangchan_check = bc.readData("fangchan_check")
    @classmethod
    def setUpClass(cls):
        url = cls.bc.readUrl("shebeiURL")
        cls.lp.get(url)
        cls.lp.setCookie()
        cls.lp.get(url)
        cls.lp.switch_fram("iframe")
    '''
    切换到保养计划
    '''
    def test_1(self):
        url=self.bc.readUrl("baoyangURL")
        self.lp.switch_url(url)

    '''
    切换到保养计划
    '''
    def test_2(self):
        url=self.bc.readUrl("yunweiURL")
        self.lp.switch_url(url)
    '''
    切换到保养计划
    '''
    def test_3(self):
        url=self.bc.readUrl("jiluURL")
        self.lp.switch_url(url)
    @classmethod
    def tearDownClass(cls):
        cls.lp.quet()

if __name__ == "__main__":
    unittest.main()