'''
Created on 2018年7月9日

@author: C
'''
import pyautogui as pag
import aircv as ac
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from flash import *
from _ast import While
class C():
    url ='http://passport2.chaoxing.com/login?fid=1283&refer=http://i.mooc.chaoxing.com' 
    def __init__(self):
        self.driver = webdriver.Edge()
    def input(self,idi,text):
        temp=self.driver.find_element_by_id(idi)
        temp.clear()
        temp.send_keys(text)
    def login(self):
        driver = self.driver
        driver.get(self.url)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "space_nickname")))
        idi=driver.find_element_by_class_name('personalName').get_attribute('title')
        print('欢迎您进入学习系统: '+idi)
    def into(self):
        driver = self.driver
        time.sleep(2)
        driver.switch_to_frame('frame_content')
        title=driver.find_element_by_xpath("//h3[@class='clearfix']/a")
        print('课程：'+title.get_attribute('title'))
        title.click()
        time.sleep(1)
        driver.switch_to.default_content()
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.find_element_by_xpath("//span[@class='articlename']").click()
    def rplay(self):
        driver = self.driver
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.switch_to.default_content()
        driver.switch_to_frame('iframe')
        location=driver.find_element_by_xpath("//div[@class='ans-job-icon']")
        driver.execute_script("arguments[0].scrollIntoView();",location)
    def play(self):
        driver = self.driver
        time.sleep(2)
        list=driver.find_elements_by_xpath("//div[@class='ncells']")
        if list==[]:
            list=driver.find_elements_by_xpath("//div[@class='ncells']")
        for i in range(len(list)):
            driver.switch_to.default_content()
            list1=driver.find_elements_by_xpath("//div[@class='ncells']")
            list1[i].click()
            time.sleep(5)
            str1=driver.find_element_by_xpath("//div[@class='main']/h1").text
            print(str(i)+':'+str1)
            driver.switch_to_frame('iframe')
            try:
                driver.find_element_by_xpath("//div[@class='ans-attach-ct ans-job-finished']")
                print('该小节已经看完，跳过')
                time.sleep(2)
            except:
                print('开始看视频')
                driver.maximize_window()
                while True:
                    if str1[0]=='测':
                        break
                    try:
                        #print('检测是否完成')
                        driver.find_element_by_xpath("//div[@class='ans-attach-ct ans-job-finished']")
                        break
                    except:
                        self.rplay()
                        playmain()
if __name__ == "__main__":
    c=C()
    c.login()
    c.into()
    c.play()