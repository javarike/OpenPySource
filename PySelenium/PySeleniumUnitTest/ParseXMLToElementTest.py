# coding=utf-8
'''
Created on 2013-7-1

@author: tiande.zhang
'''
from Common.ParseXMLToElement import ParseXMLToElement
from DataManager.DataModel.TestCase import TestCase

import unittest
import os


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testgetRoot(self):
        root= ParseXMLToElement.getRoot(r"D:\MyCode\Not.Net\PythonLearning\XMLLearnning\TestCases.xml")
        print(root)
    
    def testgetElementByTag(self):
        root= ParseXMLToElement.getRoot(r"D:\MyCode\Not.Net\PythonLearning\XMLLearnning\TestCases.xml")
        element=ParseXMLToElement.getElementByTag(root,"TestCase")
        print(element)
    
    def testgetElemen1tByTag(self):
        root= ParseXMLToElement.getRoot(r"D:\MyCode\Not.Net\PythonLearning\XMLLearnning\TestCases.xml")
        element=ParseXMLToElement.getElementByAttr(root,"TestCaseID", "WebSite.InlandHotel.HotelListPageCheck")
        print(element.get("Name"))
        
    def testTestCase(self):
        testCase=TestCase()
        for key in testCase.__dict__.keys():
            print(key)
            testCase.__dict__[key]="123"
        for key in testCase.__dict__.keys():
            print(testCase.__dict__[key])
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    fp=open(r"d:\testResult.txt",'a')
    suite=unittest.makeSuite(Test, "test")
    runner=unittest.TextTestRunner(stream=fp)
    runner.run(suite)