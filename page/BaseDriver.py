# #coding=utf-8
#
# import time
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
# import configparser
# import json
# class BascPage():
#      '''
#      构造方法，初始化driver
#      '''
#      def __init__(self,driver):
#           self.driver = driver
#           self.driver.implicitly_wait(10)
#      '''
#           通过下面七种方法找元素的方法，并返回元素
#      '''
#      def get_element(self,key):
#           config = configparser.ConfigParser()
#           config.read("./config/element.ini",encoding="utf-8-sig")
#           vak = config.get("ELE", key)
#           by = vak.split("----")[0]
#           by_value = vak.split("----")[1]
#           try:
#                if by == "id":
#                     return self.driver.find_element_by_id(by_value)
#                elif by == "name":
#                     return self.driver.find_element_by_name(by_value)
#                elif by == "className":
#                     return self.driver.find_element_by_class_name(by_value)
#                elif by == "cssSelector":
#                     return self.driver.find_element_by_css_selector(by_value)
#                elif by == "xpath":
#                     return self.driver.find_element_by_xpath(by_value)
#                elif by == "textLink":
#                     return self.driver.find_element_by_link_text(by_value)
#                elif by == "tagName":
#                     return self.driver.find_element_by_tag_name(by_value)
#           except Exception as e:
#                print(e)
#                print("无法找到元素"+key)
#
#      '''
#      输入框的输入方法，先清除输入框的内容，再输入值
#      '''
#      def sendkeys(self, key, value):
#           element = self.get_element(key)
#           try:
#                element.clear()
#           except Exception as e:
#                print(e)
#           element.send_keys(value)
#      '''
#      点击的方法
#      '''
#      def click(self,key):
#           element = self.get_element(key)
#           element.click()
#      '''
#      定位下拉框，获取下拉框的的元素，通过元素text值定位
#      '''
#      def selector(self, key, text):
#           element = Select(self.get_element(key))
#           element.select_by_visible_text(text)
#
#      '''
#           定义打开 url 的方法,打开浏览器
#      '''
#      def get(self, url):
#           self.driver.geturl(url)
#           try:
#                self.driver.maximize_window()
#           except:
#                print("窗口不用最大化了")
#
#
#      '''
#      定义script方法，用于执行js脚本，范围执行结果
#      '''
#      def script(self, src):
#           time.sleep(1)
#           self.driver.execute_script(src)
#      '''
#      关闭浏览器
#      '''
#      def quet(self):
#           self.driver.quit()
#      '''
#          删除cookie 的方法
#      '''
#      def delCookie(self):
#           self.driver.delete_all_cookies()
#
#      '''
#      获取cookiename=nova_pms_auth_Default，保存cookie到文件中cookies.txt
#       '''
#      def saveCookis(self):
#           for cookie in self.driver.get_cookies():
#                if (cookie['name'] == "nova_pms_auth_Default"):
#                     with open('D:/GitHub/pythonUnittest-master/config/cookies.txt', 'w') as fp:
#                          # ss=cookie['value']
#                          json.dump(cookie, fp)
#      '''
#           从文件中读取cookie
#      '''
#      def setCookie(self):
#           with open('D:/GitHub/pythonUnittest-master/config/cookies.txt', 'r', encoding="utf-8-sig") as fp:
#                # s = fp.read()
#                cookies = json.load(fp)
#                #print(cookies)
#                self.driver.add_cookie(cookies)
#      '''
#         切换ifram 窗口
#      '''
#      def switch_fram(self, key):
#           fram = self.get_element(key)
#           time.sleep(2)
#           self.driver.switch_to.frame(fram)
#      '''
#      切换回默认窗口
#      '''
#      def switch_default(self):
#           self.driver.switch_to.default_content()
#      '''
#      断言的方法,通过元素的字符串判断是否有这个元素
#      '''
#      def assertTure(self,key,exceptasser):
#           time.sleep(2)
#           element=self.get_element(key).text
#           assert exceptasser in element
#      '''
#      刷新浏览器的方法
#      '''
#      def refresh(self):
#           self.driver.refresh()
#
#      '''
#      右击  context_click()
#      左击  click_and_hold()
#      双击  double_click()
#      拖动  drag_and_drop()
#      悬停  move_to_element()
#      使用perform()提交生效操作
#      使用语法：ActionChains(网页窗口对象).事件(元素对象).perform()
#      '''
#      #鼠标左击
#      def charis_left(self,element):
#           ActionChains(self.driver).click_and_hold(element).perform()
#      #鼠标悬停
#      def charis_moveto_ele(self,element):
#           ActionChains(self.driver).move_to_element(element).perform()
#      #鼠标右击
#      def charis_right(self,element):
#           ActionChains(self.driver).context_click(element).perform()
#      #鼠标双击事件
#      def charis_double_click(self,element):
#           ActionChains(self.driver).double_click(element).perform()
#      #滑动到页面底部事件
#      def charis_sliding(self):
#           js = "var q=document.documentElement.scrollTop=100000"
#           self.driver.execute_script(js)
#
#
#
#      '''
#       Ele.send_keys(Keys.BACK_SPACE) 将搜索框中的Python1中的1删除
#       Ele.send_keys(Keys.CONTRL,’a’) 将搜索框中的Python字样全选
#       Ele.send_keys(Keys.CONTRL,’x’) 将搜索框中的Python字样剪切
#       Ele.send_keys(Keys.CONTRL,’v’) 将搜索框中的Python字样粘贴
#      '''
#      # # 键盘回车事件
#      # def keys_ebter(self,element):
#      #      element.send_keys(Keys.CONTROL.Enter)
#
