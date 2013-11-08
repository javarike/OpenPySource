# -*- coding: utf-8 -*-  
'''
Created on 2013-6-17

@author: tiande.zhang
'''

from selenium.webdriver.common import by

class UIWebControll(object):
    '''
    所哟页面元素控件基类
    '''
    def __init__(self,browser,uiElement):
        self.browser=browser
        self.UIElement=uiElement
#         self.switchToFrame()
        self.baseElement=self.getElement(browser, uiElement)
    
    def getElement(self,browser,uiElement):
        '''根据uiElement元素信息获取页面元素'''
        baseElement=self.getElementByExactInfo()
        if baseElement==None:
            baseElement=self.getElementByAttr()
        return baseElement
    
    def switchToFrame(self):
        '''切换到frame'''
        print(self.UIElement.FrameName !=None)
        if self.UIElement.FrameName !=None:
            self.browser.currentDriver.switch_to_default_content()
            self.browser.currentDriver.switch_to_frame(self.UIElement.FrameName)
        elif self.UIElement.FrameIndex !=None:
            self.browser.currentDriver.switch_to_default_content()
            self.browser.currentDriver.switch_to_frame(self.UIElement.FrameIndex)
        else:
            self.browser.currentDriver.switch_to_default_content()
            
    
    def getElementByExactInfo(self):
        ''' get element by id,xpath,linktext'''
        result=None
        if self.UIElement.ID !=None:
            result=self.browser.currentDriver.find_element(by.By.ID,self.UIElement.ID)
        elif self.UIElement.XPath !=None:
            result=self.browser.currentDriver.find_element(by.By.XPATH,self.UIElement.XPath)
        elif self.UIElement.LinkText !=None:
            result=self.browser.currentDriver.find_element(by.By.LINK_TEXT,self.UIElement.LinkText)
        return result
    
    def getElementByAttr(self):
        '''get element by attribute'''
        result=None
        if self.UIElement.TagName !=None:
            result=self.browser.currentDriver.find_elements(by.By.TAG_NAME,self.UIElement.TagName)[0]
        elif self.UIElement.Class !=None:
            result=self.browser.currentDriver.find_elements(by.By.CLASS_NAME,self.UIElement.Class)[0]
        elif self.UIElement.Name !=None:
            result=self.browser.currentDriver.find_elements(by.By.NAME,self.UIElement.Name)[0]
        return result
        
        
            
    
    def click(self):
        '''点击页面元素'''
        
        self.baseElement.click()
        
    def getText(self):
        '''获取页面元素文本'''
        
        return self.baseElement.text
    
    def displayed(self):
        '''元素针对用户是否可见'''
        return self.baseElement.is_displayed()
    
    def enabled(self):
        '''页面元素是否可用'''
        return self.baseElement.is_enabled()
        
    def getAttribute(self,name):
        '''根据属性名称获取属性'''
        return self.baseElement.get_attribute(name)
    
    def getChildren(self,tagName):
        '''获取子元素'''
        return self.baseElement.find_elements(by.By.XPATH,tagName)
    
    
        
    
        