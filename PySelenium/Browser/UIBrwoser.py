# -*- coding: utf-8 -*-  

'''
Created on 2013-6-16

@author: 张天得
'''
from selenium import webdriver
from selenium.webdriver.common import by


class BrowserType(object):
    '''
    Browser Type enum
    '''
    FireFox="FireFox"
    
    IE="IE"
    
    Chrome="Chrome"
    
    Safari="Safari"

class UIBrowser(object):
    '''浏览器级操作类  
    '''
    
    def __init__(self,browserType,browserPath=None,browserDriverPath=None,timeOut=120):
        '''根据浏览器类型，及浏览器可执行文件地址初始化浏览器      
        '''
        if browserType==BrowserType.Chrome:
            chromeOption=webdriver.ChromeOptions(browserPath)
            self.currentDriver=webdriver.Chrome(executable_path=browserDriverPath,chrome_options=chromeOption)
        
        if browserType==BrowserType.FireFox:
            self.currentDriver=webdriver.Firefox()
          
        if browserType==BrowserType.IE:
            self.currentDriver=webdriver.Ie(executable_path=browserDriverPath)
        
        self.currentDriver.implicitly_wait(timeOut)
    
    def  navigateTo(self,targetUrl):
        ''' 跳转页面到 targeturl'''
        self.currentDriver.get(targetUrl)
        
    def forward(self):
        ''' 切换到前一页面'''
        self.currentDriver.forward()
        
    def back(self):
        '''后退页面'''
        self.currentDriver.back()
    
    def clearCookie(self,name):
        '''清除指定的cookie'''
        self.currentDriver.delete_cookie(name)
    
    def clearAllCookies(self):
        '''清除所有cookies'''
        self.currentDriver.delete_all_cookies()
    
    def switchToWindow(self,windowName=None,containsKeywords=None):
        '''切换到指定窗口
           windowName:要切换到的窗口的name或者handel
           containsKeywords:页面包含的特定字符
        '''
        currentWindowHandel=self.currentDriver.current_window_handle
        if windowName !=None:
            self.currentDriver.switch_to_window(windowName)
        
        if containsKeywords!=None:
            for handel in self.currentDriver.window_handles:
                self.currentDriver.switch_to_window(handel)
                if(containsKeywords in self.currentDriver.page_source):
                    break;
                else:
                    self.currentDriver.switch_to_window(currentWindowHandel)
        
    
    def switchToFrame(self,frameIdentity):
        ''' 切换到其他Frame
            
            frameIdentity: frame name ,id,index,or frameelement
        '''
        self.currentDriver.switch_to_frame(frameIdentity)
    
    def swithToDefault(self):
        ''' 切换到最初默认窗口或者frame'''
        self.currentDriver.switch_to_default_content()

    def switchToOtherWindow(self):
        '''切换到另外一个窗口，仅限于只有两个窗口的情况'''
        for handel in self.currentDriver.window_handles:
            if handel != self.currentDriver.current_window_handle:
                self.currentDriver.switch_to_window(handel)
                break
              
    def maxSizeWindow(self):
        '''最大化window'''
        self.currentDriver.maximize_window()
    
    def refresh(self):
        '''刷新页面'''
        self.currentDriver.refresh()
        
    def executeJavaScript(self,jsString):
        '''同步执行js'''
        self.currentDriver.execute_script(jsString)
    
    def closeAlert(self,timeOut=5,accept=True):
        self.currentDriver.implicitly_wait(timeOut)
        if accept:
            self.currentDriver.switch_to_alert().accept()
        else:
            self.currentDriver.switch_to_alert().dismiss()
    
    def getAlertText(self):
        ''' 获得alert上的提示信息'''
        return self.currentDriver.switch_to_alert().text

    def close(self):
        ''' 关闭当前窗口'''
        self.currentDriver.close()
    
    def quit(self):
        ''' 退出当前执行进程'''
        self.currentDriver.quit()
    
        
if __name__=="__main__":
    browser=UIBrowser(BrowserType.FireFox)
    browser.navigateTo("http://www.baidu.com")
    browser.currentDriver.find_element(by.By.ID, value="kw").send_keys("selenium")
    browser.currentDriver.find_element(by.By.ID, value="su").click()
    print(browser.currentDriver.current_url)
    browser.maxSizeWindow()