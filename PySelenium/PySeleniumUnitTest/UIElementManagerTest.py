#coding=utf-8
'''
Created on 2013-7-2

@author: tiande.zhang
'''
from DataManager.UIElementManager import UIElementManager
from Common.GlobalConfig import GlobalConfig

import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        GlobalConfig.UIElementFilePath=r"D:\MyCode\Not.Net\PythonLearning\XMLLearnning\UIElements.xml"
        uiElementManager=UIElementManager()
        uiElementNode=uiElementManager.GetUIElement("WebSite.InlandHotel.HotelList.CheckInDateTextBox")
        print(uiElementNode.ControllType)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()