# coding=utf-8
'''
Created on 2013-7-1

@author: tiande.zhang
'''

class XMLElementIsNonException(Exception):
    '''
    找不到xmlelement异常
    '''


    def __init__(self,errorMessage):
        '''
        找不到xmlelement元素
        '''
        self.errorMessage=errorMessage
    def __str__(self):
        print("Can not found xml element for: "+self.errorMessage)
        
class UIElementAttributIsNonException(Exception):
    ''' 页面元素定位属性找不到'''
    def __init__(self,errorMessage):
        self.errorMessage=errorMessage
    
    def __str__(self):
        print("value for attribute: "+self.errorMessage+" is None")
    
        