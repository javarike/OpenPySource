'''
Created on 2013-7-6

@author: tiande.zhang
'''
import unittest
from Common.Logger4Py.Logger import Logger


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testLoggerErrorMethod(self):
        msg="errorTest2"
        logger=Logger()
        logger.error("errorTest2")
        logger.info(msg)
        logger.critical(msg)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()