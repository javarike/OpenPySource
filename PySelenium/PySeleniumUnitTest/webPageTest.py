# coding=utf-8
'''

'''
import unittest
from Browser.UIBrwoser import UIBrowser
from Browser.UIWebPage import UIWebPage
from Browser.UIBrwoser import BrowserType
from Common.GlobalConfig import GlobalConfig
from UIControll.UIWebButton import WebButton


class Test(unittest.TestCase):


    def testName(self):
        GlobalConfig.UIElementFilePath=r"D:\MyCode\Not.Net\PySelenium\Content\UIElements.xml"
        browser=UIBrowser(BrowserType.FireFox)
        browser.navigateTo("http://www.baidu.com")
        webPage=UIWebPage(browser)
        webPage["WebSite.InlandHotel.HotelList.CityTextBox"].click()
        uibutton=WebButton()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    test=Test()
    test.testName()