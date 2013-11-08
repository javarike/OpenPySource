# -*- coding: utf-8 -*-  
'''
Created on 2013-6-17

@author: tiande.zhang
'''

from DataManager.UIElementManager import UIElementManager
from DataManager.ComponetParameterManager import ComponetParameterManager
from DataManager.TestCaseManager import TestCaseManager

class XMLObjectType(object):
    ''' xml object type enum'''
    
    TestCase="TestCase"
    
    UIElement="UIElement"
    
    ComponetParameter="ComponetParameter"

class XmlObjectManager(object):
    '''
     Xml object manager interface
    '''


    def __init__(self):
        '''
         init xmlObject manager
        '''
    @staticmethod
    def getObject(xmlObjectType,xmlNodeID):
        ''' 获取XML实例化对象'''
        
        if xmlObjectType==XMLObjectType.TestCase:
            return TestCaseManager().GetTestCase(xmlNodeID)
        
        if xmlObjectType==XMLObjectType.UIElement:
            return UIElementManager().GetUIElement(xmlNodeID)
        
        if xmlObjectType==XMLObjectType.ComponetParameter:
            return ComponetParameterManager().getComponetParameter(xmlNodeID)
        
        
        
        
        
        