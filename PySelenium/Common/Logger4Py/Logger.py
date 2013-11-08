# coding=utf-8
'''
Created on 2013-7-2

@author: tiande.zhang
'''
import logging.config
import os
import inspect
from Common.Logger4Py.LoggerEnum import LoggerEnum
from Common.GlobalConfig import GlobalConfig
from Common.ObjectInvoker import ObjectInvoker


class Logger(object):
    '''
    所有logger的基类
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.createLogDir()
        logging.config.fileConfig(GlobalConfig.LoggerConigPath)
    
    def info(self,msg):
        '''将信息记录为到Trace.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileInfoLogger)
        logger.info(self.getInvokerInfo()+msg)
    
    def error(self,msg):
        '''将信息记录为到Error.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileErrorLogger)
        logger.error(self.getInvokerInfo()+msg)
    
    def critical(self,msg):
        '''将信息记录为到Critical.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileCriticalLogger)
        logger.critical(self.getInvokerInfo()+msg)
    
    def LogToConsole(self,msg):
        '''将信息记录为到Critical.log文件中'''
        logger=logging.getLogger(LoggerEnum.StreamLogger)
        logger.debug(self.getInvokerInfo()+msg)
    
    def TraceLog(self,msg):
        '''将信息记录为到trace.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileTraceLogger)
        logger.debug(self.getInvokerInfo()+msg)
    
    def createLogDir(self):
        if not os.path.exists(GlobalConfig.LoggerFilePath):
            os.mkdir(GlobalConfig.LoggerFilePath)
    
    def getCurrentFrame(self):
        return inspect.currentframe()
    
    def getInvokerInfo(self):
        invoker=ObjectInvoker(self.getCurrentFrame())
        return invoker.getModule()+"    "+invoker.getMethod()+"    "+str(invoker.getLineNumber())+"    "
    
        

        
    

    
        
        