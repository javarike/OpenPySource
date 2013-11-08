# -*- coding: utf-8 -*-  
'''
Created on 2013-6-17

@author: tiande.zhang
'''
from Common.GlobalConfig import GlobalConfig
from Common.ParseXMLToElement import ParseXMLToElement
from Common.CustomException.CustomException import XMLElementIsNonException
from Common.MethodInovkeTracer import MethodInvokeTracer
from DataManager.DataModel.UIElement import UIElement

class UIElementManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
                           初始化实例属性
        '''
        self.root=self.root=ParseXMLToElement.getRoot(GlobalConfig.UIElementFilePath)
        self.xmlNodeID=None
    
    @MethodInvokeTracer
    def GetUIElement(self,uiElementNodeID):
        self.xmlNodeID=uiElementNodeID
        uiElementNode=self.getUIElementXmlElement(uiElementNodeID)
        return self.initializeUIElements(uiElementNode)
    
    def getUIElementXmlElement(self,xmlNodeID):
        '''获取UIElementNode by case id'''
        return ParseXMLToElement.getElementByAttr(self.root,"NodeID",xmlNodeID)
    
    def initializeUIElements(self,uiElementNode):
        '''实例化UIElements类'''
        if uiElementNode is None:
            raise XMLElementIsNonException(self.xmlNodeID)
        uiElementObject=self.xmlToUIElementObject(uiElementNode)
        return uiElementObject
    
    def xmlToUIElementObject(self,uiElementNode):
        '''返回UIElement对象'''
        uiElement=UIElement()
        for item in uiElement.__dict__.keys():
            uiElement.__dict__[item]=uiElementNode.get(item)
        return uiElement

            
        
        