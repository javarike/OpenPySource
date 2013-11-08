#coding=utf-8
'''
Created on 2013-7-2

@author: tiande.zhang
'''
from DataManager.TestCaseManager import TestCaseManager
from Common.GlobalConfig import GlobalConfig

import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        GlobalConfig.TestCaseFilePath=r"D:\MyCode\Not.Net\PythonLearning\XMLLearnning\UIElements.xml"
        testCaseManager=TestCaseManager()
        testCase=testCaseManager.GetTestCase("WebSite.InlandHotel.HotelListPageCheck")
        print(testCase.ID)
        testComponet=testCase.TestComponets[0]
        print(testComponet.ComponetName)
    
    



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()