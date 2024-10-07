import os
import time

from selenium import webdriver


class WebHelper(object):
    """封装selenium基本操作"""

    def startBrowser(self):
        """启动览器"""
        real_path = f'{os.path.dirname(__file__)}/drivers'
        if self.browserType == 'CR':
            real_path += '/chromedriver'
            self.driver = webdriver.Chrome(real_path)
        elif self.browserType == 'SF':
            self.driver = webdriver.Safari()
        # 窗口最大化
        self.driver.maximize_window()
        # 跳转浏览器地址
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def readToComplete(self):
        """判断页面是否加载完成"""
        for i in range(self.dWaitTime):
            status = self.driver.execute_script("return document.readystate")
            if str(status) == 'complete':
                break
            else:
                time.sleep(1)

    def findElementsByXpath(self, xpath):
        """寻找元素的方法，只返回筛选后的元素集合"""
        self.readToComplete()
        eReturn = []
        elements = self.driver.find_elements_by_xpath(xpath)
        for ele in elements:
            try:
                # 判断元素是否可以进行操作，比如，点击，输入等。
                enabledPro = ele.is_enabled()
            except:
                enabledPro = None
            try:
                # 判断元素是否可见
                disPro = ele.is_displayed()
            except:
                disPro = None
            if enabledPro is not None or disPro is not None:
                eReturn.append(ele)
        return eReturn

    def __init__(self, driver: webdriver, browserType='SF', url=''):
        """初始化操作"""
        self.url = url
        self.browserType = browserType
        if driver:
            self.driver = driver
        else:
            self.startBrowser()
        self.dictWindow = {}
        self.dWaitTime = 5
        # self.wait = WebDriverWait(self.driver, 0)

        # 初始化字典，用于存储iframe层级关系
        self.myframesDict1 = {}
        self.myframesDict2 = {}
        self.myframesDict3 = {}
        self.myframesDict4 = {}
        self.myframesDict5 = {}

    def findElementsInFram(self, xpath):
        """自动遍历iframe查找元素"""
        self.myframesDict1.clear()
        self.myframesDict2.clear()
        self.myframesDict3.clear()
        self.myframesDict4.clear()
        self.myframesDict5.clear()
        eReturn = []
        framesLevel1 = self.findElementsByXpath("//iframe|//frame")
        self.readToComplete()
        # 第一层查找
        if len(framesLevel1) > 0:
            for frame1 in framesLevel1:
                # 先切换到最外层
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame(frame1)
                eReturn = self.findElementsByXpath(xpath)
                if len(eReturn) == 0:
                    # 当前查找失败，记录第二层的iframe
                    tempframeslevel2 = self.findElementsByXpath("//iframe|//frame")
                    if len(tempframeslevel2) > 0:
                        self.myframesDict1[frame1] = tempframeslevel2
                    else:
                        return eReturn
        # 第二层查找
        if len(eReturn) == 0 and len(self.myframesDict1.keys()) > 0:
            for frame1, frame2List in self.myframesDict1.items():
                for frame2 in frame2List:
                    self.driver.switch_to.default_content()
                    self.driver.switch_to.frame(frame1)
                    self.driver.switch_to.frame(frame2)
                    eReturn = self.findElementsByXpath(xpath)
                    if len(eReturn) == 0:
                        # 当前查找失败，记录第三层的iframe
                        tempframeslevel3 = self.findElementsByXpath("//iframe|//frame")
                        if len(tempframeslevel3) > 0:
                            self.myframesDict2[frame2] = tempframeslevel3
                        else:
                            return eReturn
        # 第三层查找
        if len(eReturn) == 0 and len(self.myframesDict2.keys()) > 0:
            for frame1, frame2List in self.myframesDict1.items():
                for frame2 in frame2List:
                    if frame2 in self.myframesDict2.keys():
                        for frame3 in self.myframesDict2[frame2]:
                            self.driver.switch_to.default_content()
                            self.driver.switch_to.frame(frame1)
                            self.driver.switch_to.frame(frame2)
                            self.driver.switch_to.frame(frame3)
                            eReturn = self.findElementsByXpath(xpath)
                            if len(eReturn) == 0:
                                # 当前查找失败，记录第四层的iframe
                                tempframeslevel4 = self.findElementsByXpath("//iframe|//frame")
                                if len(tempframeslevel4) > 0:
                                    self.myframesDict3[frame3] = tempframeslevel4
                                else:
                                    return eReturn

        # 第四层查找
        if len(eReturn) == 0 and len(self.myframesDict3.keys()) > 0:
            for frame1, frame2List in self.myframesDict1.items():
                for frame2 in frame2List:
                    if frame2 in self.myframesDict2.keys():
                        for frame3 in self.myframesDict2[frame2]:
                            if frame3 in self.myframesDict3.keys():
                                for frame4 in self.myframesDict3[frame3]:
                                    self.driver.switch_to.default_content()
                                    self.driver.switch_to.frame(frame1)
                                    self.driver.switch_to.frame(frame2)
                                    self.driver.switch_to.frame(frame3)
                                    self.driver.switch_to.frame(frame4)
                                    eReturn = self.findElementsByXpath(xpath)
                                    if len(eReturn) == 0:
                                        # 当前查找失败，记录第五层的iframe
                                        tempframeslevel5 = self.findElementsByXpath("//iframe|//frame")
                                        if len(tempframeslevel5) > 0:
                                            self.myframesDict4[frame4] = tempframeslevel5
                                        else:
                                            return eReturn

        # 第五层查找
        if len(eReturn) == 0 and len(self.myframesDict4.keys()) > 0:
            for frame1, frame2List in self.myframesDict1.items():
                for frame2 in frame2List:
                    if frame2 in self.myframesDict2.keys():
                        for frame3 in self.myframesDict2[frame2]:
                            if frame3 in self.myframesDict3.keys():
                                for frame4 in self.myframesDict3[frame3]:
                                    if frame4 in self.myframesDict4.keys():
                                        for frame5 in self.myframesDict4[frame4]:
                                            self.driver.switch_to.default_content()
                                            self.driver.switch_to.frame(frame1)
                                            self.driver.switch_to.frame(frame2)
                                            self.driver.switch_to.frame(frame3)
                                            self.driver.switch_to.frame(frame4)
                                            self.driver.switch_to.frame(frame5)
                                            eReturn = self.findElementsByXpath(xpath)
                                            if len(eReturn) == 0:
                                                # 当前查找失败，记录第六层的iframe
                                                tempframeslevel6 = self.findElementsByXpath("//iframe|//frame")
                                                if len(tempframeslevel6) > 0:
                                                    self.myframesDict5[frame5] = tempframeslevel6
                                                else:
                                                    return eReturn

        # 第六层查找
        if len(eReturn) == 0 and len(self.myframesDict5.keys()) > 0:
            for frame1, frame2List in self.myframesDict1.items():
                for frame2 in frame2List:
                    if frame2 in self.myframesDict2.keys():
                        for frame3 in self.myframesDict2[frame2]:
                            if frame3 in self.myframesDict3.keys():
                                for frame4 in self.myframesDict3[frame3]:
                                    if frame4 in self.myframesDict4.keys():
                                        for frame5 in self.myframesDict4[frame4]:
                                            if frame5 in self.myframesDict5.keys():
                                                for frame6 in self.myframesDict5[frame5]:
                                                    self.driver.switch_to.default_content()
                                                    self.driver.switch_to.frame(frame1)
                                                    self.driver.switch_to.frame(frame2)
                                                    self.driver.switch_to.frame(frame3)
                                                    self.driver.switch_to.frame(frame4)
                                                    self.driver.switch_to.frame(frame5)
                                                    self.driver.switch_to.frame(frame6)
                                                    eReturn = self.findElementsByXpath(xpath)

        return eReturn

    def webSwitchWindow(self, newUrl):
        """窗口切换"""
        if self.driver is not None:
            if newUrl in self.driver.title or newUrl in self.driver.current_url:
                return True
            else:
                win_handles = self.driver.window_handles
                for item_handle in win_handles:
                    try:
                        self.driver.switch_to.window(item_handle)
                        if newUrl in self.driver.title or newUrl in self.driver.current_url:
                            return True
                    except:
                        return False
                else:
                    return False
        else:
            return False

    def findElements(self, xpath):
        """按照传递的xpath查找元素"""
        self.readToComplete()
        times, waitTime = 5, 0.5
        for i in range(times):
            try:
                eReturn = self.findElementsByXpath(xpath)
                # 如果没有找到元素，自动切回default层继续查找
                if len(eReturn) < 1:
                    self.driver.switch_to.default_content()
                    eReturn = self.findElementsByXpath(xpath)
                    # 在default查找失败，调用自动切换iframe层继续查找
                    if eReturn is not None and len(eReturn) < 1:
                        eReturn = self.findElementsInFram(xpath)
                        if eReturn is not None and len(eReturn) > 0:
                            return eReturn
                        else:
                            time.sleep(waitTime)
                else:
                    return eReturn
            except:
                time.sleep(waitTime)
        else:
            return []


if __name__ == '__main__':
    WebHelper(url='http://www.baidu.com')
