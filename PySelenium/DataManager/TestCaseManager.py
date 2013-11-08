# -*- coding=utf-8 -*-  
'''
Created on 2013-6-17

@author: tiande.zhang
'''

from Common.GlobalConfig import GlobalConfig
from Common.ParseXMLToElement import ParseXMLToElement
from Common.CustomException.CustomException import XMLElementIsNonException
from DataManager.DataModel.TestCase import TestCase
from DataManager.DataModel.TestComponet import TestComponet
from Common.MethodInovkeTracer import MethodInvokeTracer

class TestCaseManager(object):
    '''
    用例管理对象
    '''


    def __init__(self):
        '''
                           初始化实例属性
        '''
        self.root=self.root=ParseXMLToElement.getRoot(GlobalConfig.TestCaseFilePath)
        self.xmlNodeID=None
        
    @MethodInvokeTracer
    def GetTestCase(self,xmlNodeID):
        self.xmlNodeID=xmlNodeID
        testCaseElement=self.getTestCaseElement(xmlNodeID)
        return self.initializeTestCase(testCaseElement)
    
    def getTestCaseElement(self,xmlNodeID):
        '''获取TestcaseElement by case id'''
        return ParseXMLToElement.getElementByAttr(self.root,"ID",xmlNodeID)
    
    def initializeTestCase(self,testCaseElement):
        '''实例化testcase类'''
        if testCaseElement is None:
            raise XMLElementIsNonException(self.xmlNodeID)
        testCaseObject=self.xmlToTestCaseObject(testCaseElement)
        testCaseObject.TestComponets=self.xmlToTestComponet(testCaseElement,testCaseObject)
        return testCaseObject
        
    
    def getPropertyValue4Case(self,testCaseElement,propertyName):
        '''获取属性值'''
        if propertyName in testCaseElement.attrib.keys():
            return testCaseElement.get(propertyName)
        elif ParseXMLToElement.getElementByTag(self.root, propertyName):
            return ParseXMLToElement.getElementByTag(self.root, propertyName).text
        else:
            return None

    def xmlToTestCaseObject(self,testCaseElement):
        '''获取实例属性'''
        testCaseObject=TestCase()
        for key in testCaseObject.__dict__.keys():
            testCaseObject.__dict__[key]=self.getPropertyValue4Case(testCaseElement,key)
        return testCaseObject
    
    def getTestComponetElements(self,testCaseElement):
        '''获取TestComponetElement list'''
        parentElement=ParseXMLToElement.getElementByTag(testCaseElement,"TestComponets")
        return ParseXMLToElement.getChildrenByTag(parentElement,"TestComponet")
    
    def xmlToTestComponet(self,testCaseElement,parentCase):
        '''将testcomponet从xml转换为实例'''
        testComponetElements=self.getTestComponetElements(testCaseElement)
        testComponetList=[]
        for componet in testComponetElements:
            testComponet=TestComponet()
            if componet!=None:
                for key in testComponet.__dict__.keys():
                    testComponet.__dict__[key]=self.getPropertyValue4Componet(componet, parentCase, key)
            testComponetList.append(testComponet)
        return testComponetList
    
    def getPropertyValue4Componet(self,componetElement,parentCase,propertyName):
        '''实例化Componet'''
        if propertyName in componetElement.attrib.keys():
            return componetElement.get(propertyName)
        elif propertyName in parentCase.__dict__.keys():
            if parentCase.__dict__[propertyName]!=None:
                return parentCase.__dict__[propertyName]
        else:
            return None
        
        
        
        
        
        
        