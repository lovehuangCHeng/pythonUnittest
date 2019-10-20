#coding=utf-8

import time
import configparser
import json
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class BascPage():
     '''
     构造方法，初始化driver
     '''

     def __init__(self,driver):
          self.driver = driver
          self.driver.implicitly_wait(15)
     '''
          通过下面七种方法找元素的方法，并返回元素
     '''
     def get_element(self, key):
          config = configparser.ConfigParser()
          config.read("./config/element.ini",encoding="utf-8-sig")
          vak = config.get("ELE", key)
          by = vak.split("/")[0]
          by_value = vak.split("/")[1]
          try:
               if by == "id":
                    return self.driver.find_element_by_id(by_value)
               elif by == "name":
                    return self.driver.find_element_by_name(by_value)
               elif by == "className":
                    return self.driver.find_element_by_class_name(by_value)
               elif by == "cssSelector":
                    return self.driver.find_element_by_css_selector(by_value)
               elif by == "xpath":
                    return self.driver.find_element_by_xpath(by_value)
               elif by == "textLink":
                    return self.driver.find_element_by_link_text(by_value)
               elif by == "tagName":
                    return self.driver.find_element_by_tag_name(by_value)
          except Exception as e:
               print(e)

     '''
     通过xptah和classname 等方法找到元素
     '''
     def find_element(self,value):
          try:
               element =self.driver.find_element_by_class_name(value)
               return element
          except:
               element=self.driver.find_element_by_xpath(value)
               return  element
     '''
     输入框的输入方法，先清除输入框的内容，再输入值
     '''
     def sendkeys(self, key, value):
          element = self.get_element(key)
          try:
               element.clear()
          except Exception as e:
               print(e)
          element.send_keys(value)
     '''
     点击的方法
     '''
     def click(self,key):

          element = self.get_element(key)

          element.click()
     '''
     定位下拉框，获取下拉框的的元素，通过元素text值定位
     '''
     def selector(self, key, text):

          element = Select(self.get_element(key))

          element.select_by_visible_text(text)

     '''
          读取url文件
          '''

     def readUrl(self, key):
          conf = configparser.ConfigParser()
          conf.read("./dataconfig/url.ini",encoding="utf-8-sig")
          url = conf.get("ZIP", key)
          return url

     '''
          定义打开 url 的方法,打开浏览器
          '''

     def get(self, url):
          self.driver.get(url)
          try:
               self.driver.maximize_window()
          except:
               print("窗口不用最大化了")


     '''
     定义script方法，用于执行js脚本，范围执行结果
     '''

     def script(self, src):
          time.sleep(1)
          self.driver.execute_script(src)

     '''
     关闭浏览器
     '''

     def quet(self):
          self.driver.quit()

     '''
         删除cookie 的方法
     '''

     def delCookie(self):
          self.driver.delete_all_cookies()

     '''
          保存cookie到文件中
     '''

     def saveCookis(self):
          dict_cookies = {}
          for cookie in self.driver.get_cookies():
               dict_cookies[cookie['name']] = cookie['value']
               with open('./config/cookies.txt', 'w') as f:
                    cook = json.dumps(cookie)
                    f.write(cook)
               f.close()

     '''
     从文件中读取cookie
     '''

     def setCookie(self):
          with open('./config/cookies.txt', 'r', encoding="utf-8-sig") as f:
               s = f.read()
               cookies = json.loads(s)
               print(cookies)
               self.driver.add_cookie(cookies)

     '''
        切换ifram 窗口
        '''

     def switch_fram(self, key):
          fram = self.get_element(key)
          time.sleep(2)
          self.driver.switch_to.frame(fram)
     '''
     切换回默认窗口
     '''
     def switch_default(self):
          self.driver.switch_to.default_content()
     '''
     断言的方法,通过元素的字符串判断是否有这个元素
     '''
     def assertTure(self,key,exceptasser):
          time.sleep(2)
          element=self.find_element(key).text
          assert exceptasser in element
     '''
     刷新浏览器的方法
     '''
     def refresh(self):
          self.driver.refresh()

     '''
     右击  context_click()
     左击  click_and_hold()
     双击  double_click()
     拖动  drag_and_drop()
     悬停  move_to_element()
     使用perform()提交生效操作
     使用语法：ActionChains(网页窗口对象).事件(元素对象).perform()
     鼠标左击
     '''
     def charis_left(self,element):
          ActionChains(self.driver).click_and_hold(element).perform()
     #鼠标悬停
     def charis_moveto_ele(self,element):
          ActionChains(self.driver).move_to_element(element).perform()
     #鼠标右击
     def charis_right(self,element):
          ActionChains(self.driver).context_click(element).perform()
     #鼠标双击事件
     def charis_double_click(self,element):
          ActionChains(self.driver).double_click(element).perform()