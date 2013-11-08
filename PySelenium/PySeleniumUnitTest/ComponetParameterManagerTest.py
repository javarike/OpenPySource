#coding=utf-8
'''
Created on 2013-7-2

@author: tiande.zhang
'''
from DataManager.ComponetParameterManager import ComponetParameterManager
from Common.GlobalConfig import GlobalConfig

import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        GlobalConfig.ComponetParameterFilePath=r"D:\MyCode\Not.Net\PythonLearning\XMLLearnning\ComponetsParameters.xml"
        componetParameterManager=ComponetParameterManager()
        uiElementNode=componetParameterManager.getComponetParameter("InlandHotelListHotelFilterCheck")
        print(uiElementNode.Parameters["locationFilter"])



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()