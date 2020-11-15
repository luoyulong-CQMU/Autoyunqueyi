#########adb shell dumpsys window windows | findstr mFocusedApp

from appium import webdriver
import time
import subprocess
from time import ctime
import os
import sys
import socket

class auto_study():
    def __init__(self):
        super(auto_study, self).__init__()
        self.study_list = []
        self.review_list = []
        self.continue_list = []
        self.start_appium()
    def start_appium(self):
        self.release_port(4723)
        host='127.0.0.1'
        port=4723
        self.start_appiumserver(host,port)
        self.android_message()


    def android_message(self):   #创建一个字典，包装相应的启动参数
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '192.168.4.222:5555'
        desired_caps['appPackage'] = 'com.picahealth.yunque'
        desired_caps['appActivity'] = '.activitys.mainpage.home.MainPageActivity'
        desired_caps['noReset'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(8)
        self.find_studytitle()

    def find_studytitle(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@text='专项合作']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[contains(@text,"高血压系列")]').click()
        time.sleep(2)
        self.find_studyclass()

    def find_studyclass(self):
        Review=self.check_element("去复习")
        new=self.check_element("去学习")
        self.print_works()
        while new is False:
            before_swipe = self.driver.page_source
            self.driver.swipe(444, 1750, 444, 1200)
            self.print_works()
            after_swipe=self.driver.page_source
            if before_swipe == after_swipe:
                swiped=False
                print("到底啦")
            else:
                swiped=True

                print("向下滑动屏幕")
            if swiped is True:
                new=self.check_element("去学习")
            else:
                high_class = self.check_element("高级课程")
                enter_class = self.check_element("进阶课程")
                print('high_class:',high_class,'enter_class:',enter_class)
                if high_class is False and enter_class is False:
                    print('没有找到可以学习的课程,即将停止')
                    print('已学习课程:')
                    print(self.review_list)
                    sys.exit(0)
                elif high_class is True:
                    self.driver.find_element_by_xpath('//*[contains(@text,"高级课程")]').click()
                    print('学习高级课程')

                elif enter_class is True:
                    self.driver.find_element_by_xpath('//*[contains(@text,"进阶课程")]').click()
                    print('学习进阶课程')
        try:
            willstudy_title = self.driver.find_element_by_xpath(
                '//*[contains(@text,"去学习")]/preceding-sibling::*/child::*[2]')
            print('即将开始学习课程：', willstudy_title.text)
        except:
            pass
        self.driver.find_element_by_xpath('//*[contains(@text,"去学习")]').click()
        self.find_studyvideo()

    def find_studyvideo(self):
        time.sleep(1)
        self.driver.find_element_by_id("com.picahealth.yunque:id/ivStart").click()
        self.check_returnbutton()

    def check_returnbutton(self):
        check=self.check_element("您已完成")

        while check is False:
            check=self.check_element("您已完成")
            time.sleep(2)
        self.next_class = self.check_element("学习下一课")
        self.exam = self.check_element("您已完成学习，参加考试巩固学习成果")
        self.next_lesson()

    def next_lesson(self):
        if self.next_class is True:
            self.driver.find_element_by_xpath('//*[contains(@text,"学习下一课")]').click()
            self.check_returnbutton()
        elif self.exam is True:
            self.driver.find_element_by_id("com.picahealth.yunque:id/btn_left").click()
            time.sleep(2)
            self.driver.keyevent(4)  #系统返回键
        else:
            self.back_studyclass()



    def back_studyclass(self):
        self.driver.find_element_by_id("com.picahealth.yunque:id/btn_left").click()
        self.find_studyclass()

    def check_element(self,element):
        source= self.driver.page_source
        if element in source:
            return True
        else:
            return False

    def start_appiumserver(self,host,port):
        bootstrap_port=str(port+1)
        cmdclose='taskkill /F /t /IM node.exe'
        cmd='start appium -a  '+host +' -p '+str(port)
        print('%s at %s' % (cmd, ctime()))
        subprocess.call(cmd,shell=True)
       # os.system(cmd)

    def check_port(self,host,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host,port))
            s.shutdown(2)
        except OSError as msg:
            print('port %s is available! ' % port)
            print(msg)
            return True
        else:
            print('port %s already be in use !' % port)
            return False

    def release_port(self,port):
        # 查找对应端口的pid
        cmd_find = 'netstat -aon | findstr %s' % port
        print(cmd_find)
        # 返回命令执行后的结果
        result = os.popen(cmd_find).read()
        print(result)
        if str(port) and 'LISTENING' in result:
            # 获取端口对应的pid进程
            i = result.index('LISTENING')
            start = i + len('LISTENING') + 7
            end = result.index('\n')
            pid = result[start:end]
            # 关闭被占用端口的pid
            cmd_kill = 'taskkill -f -pid %s' % pid
            print(cmd_kill)
            os.popen(cmd_kill)

        else:
            print('port %s is available !' % port)
    def print_works(self):
        Review = self.check_element("去复习")
        new = self.check_element("去学习")
        continue_study=self.check_element("继续学习")
        if Review is True:
            go_review_title = self.driver.find_elements_by_xpath(
                '//*[contains(@text,"去复习")]/preceding-sibling::*/child::*[2]')
            for i in range(len(go_review_title)):
                if go_review_title[i].text in self.review_list:
                    pass
                else:
                    print(go_review_title[i].text, '：已学习，跳过')
                    self.review_list.append(go_review_title[i].text)
        if new is True:
            go_study_title = self.driver.find_elements_by_xpath(
                '//*[contains(@text,"去学习")]/preceding-sibling::*/child::*[2]')
            for i in range(len(go_study_title)):
                if go_study_title[i].text in self.study_list:
                    pass
                else:
                    print(go_study_title[i].text, '：未学习')
                    self.study_list.append(go_study_title[i].text)
        if continue_study is True:
            go_continue_study = self.driver.find_elements_by_xpath(
                '//*[contains(@text,"继续学习")]/preceding-sibling::*/child::*[2]')
            for i in range(len(go_continue_study)):
                if go_continue_study[i].text in self.continue_list:
                    pass
                else:
                    print(go_continue_study[i].text, '：学习了一部分，就先不学了吧')
                    self.continue_list.append(go_continue_study[i].text)




        # try:
        #     len(go_review_title) == 0
        # except:
        #     for i in len(go_review_title):
        #         print(go_review_title[i],'：已学习，跳过')
        # try:
        #     len(go_study_title) == 0
        # except:
        #     for i in len(go_study_title):
        #         print(go_study_title[i],'：未学习')
        # try:
        #     len(go_continue_study) == 0
        # except:
        #     for i in len(go_continue_study):
        #         print(go_continue_study,'：学习了一部分，就先不学了吧')

        # try:
        #     go_study=self.driver.find_elements_by_xpath('//*[contains(@text,"去学习")]')
        #     go_study_title=self.driver.find_elements_by_xpath('//*[contains(@text,"去学习")]/preceding-sibling::*/child::*[2]')
        #     # print('go_study:',go_study)
        #     # print('go_study_title:',go_study_title)
        #     for i in range(len(go_study_title)):
        #         print(go_study_title[i].text,'：未学习')
        # except:
        #     go_review=self.driver.find_elements_by_xpath('//*[contains(@text,"去复习")]')
        #     go_review_title = self.driver.find_elements_by_xpath('//*[contains(@text,"去复习")]/preceding-sibling::*/child::*[2]')
        #     # print('go_review:',go_review)
        #     # print('go_review_title',go_review_title)
        #     for i in range(len(go_review_title)):
        #         print(go_review_title[i].text,'：已学习,跳过')



if __name__ == '__main__':

    auto_study()