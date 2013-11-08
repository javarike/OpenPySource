# -*- coding: utf-8 -*-  
'''
Created on 2013-6-17

@author: tiande.zhang
'''

from Common.GlobalConfig import GlobalConfig
from Common.ParseXMLToElement import ParseXMLToElement
from Common.CustomException.CustomException import XMLElementIsNonException
from DataManager.DataModel.ComponetParameter import ComponetParameter
from Common.MethodInovkeTracer import MethodInvokeTracer

class ComponetParameterManager(object):
    
    def __init__(self):
        self.root=self.root=ParseXMLToElement.getRoot(GlobalConfig.ComponetParameterFilePath)
        self.xmlNodeID=None
    
    @MethodInvokeTracer
    def getComponetParameter(self,componetParameterID):
        self.xmlNodeID=componetParameterID
        componetParameterElement=self.getComponetParameterElement(componetParameterID)
        return self.initializeComponetParameter(componetParameterElement)
    
    def getComponetParameterElement(self,xmlNodeID):
        '''获取TestcaseElement by case id'''
        return ParseXMLToElement.getElementByAttr(self.root,"ID",xmlNodeID)
    
    def initializeComponetParameter(self,componetParameterElement):
        '''实例化componetParameter类'''
        if componetParameterElement is None:
            raise XMLElementIsNonException(self.xmlNodeID)
        componetParameterObject=self.xmlToComponetParameterObject(componetParameterElement)
        return componetParameterObject
        
    
    def getPropertyValue4ComponetParameter(self,componetParameterElement,propertyName):
        '''获取属性值'''
        if ParseXMLToElement.getElementByTag(componetParameterElement,propertyName).text!=None:
            return ParseXMLToElement.getElementByTag(componetParameterElement,propertyName).text
        elif propertyName!="CommandText":
            return ParseXMLToElement.getElementByTag(self.root,propertyName).text

    def xmlToComponetParameterObject(self,componetParameterElement):
        '''获取实例属性'''
        componetParameterObject=ComponetParameter()
        for key in componetParameterObject.__dict__.keys():
            if key !="Parameters":
                componetParameterObject.__dict__[key]=self.getPropertyValue4ComponetParameter(componetParameterElement,key)
            else:
                componetParameterObject.Parameters=self.getParameters(componetParameterElement)
        return componetParameterObject
    
    def getParameters(self,componetParameterElement):
        '''获取TestComponetElement list'''
        parentElement=ParseXMLToElement.getElementByTag(componetParameterElement,"Parameters")
        keys=[]
        values=[]
        for child in parentElement:
            keys.append(child.tag)
            values.append(child.text)
        parameters=dict(zip(keys,values))
        return parameters
    