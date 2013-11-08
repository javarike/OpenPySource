# coding=utf-8
'''
Created on 2013-7-1

@author: tiande.zhang
'''
from xml.etree import ElementTree

class ParseXMLToElement(object):
    '''
    转换xml为对象
    '''
    @staticmethod
    def getRoot(xmlFileName):
        '''获取文件根节点'''
        etree=ElementTree.parse(xmlFileName)
        return etree.getroot()
    
    @staticmethod
    def getChildrenByTag(parent,tagName):
        '''通过tag获取子元素列表'''
        return parent.findall(tagName)
    
    @staticmethod
    def getElementByAttr(parent,attributeName,attributeValue):
        '''通过属性获取元素'''
        result=None
        for child in parent.getchildren():
            if child.get(attributeName)==attributeValue:
                result=child
                break
        return result
                
    
    @staticmethod
    def getElementByTag(parent,tagName):
        '''通过tag获取元素'''
        result=None
        for child in parent.getchildren():
            if child.tag==tagName:
                result=child
                break
        return result
        
            
        