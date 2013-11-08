# -*- coding: utf-8 -*-  
'''
Created on 2013-6-16

@author: tiande.zhang
'''
from Browser.UIBrwoser import UIBrowser
from DataManager.XmlObjectManager import XmlObjectManager
from DataManager.XmlObjectManager import XMLObjectType
from Common.ClassActivator import ClassActivator

class UIWebPage(object):
    


    def __init__(self,uiBrowser):
        '''初始化UIWebpage类 '''
        if not isinstance(uiBrowser,UIBrowser):
            raise TypeError()
        self.currentBrowser=uiBrowser
        
    def __getitem__(self,key):
        uielement=self.getUIElement(key)
        return ClassActivator().createInstance(uielement.ControllType,self.currentBrowser,uielement)
    
    def getUIElement(self,uiElementNodeID):
        return XmlObjectManager.getObject(XMLObjectType.UIElement, uiElementNodeID)