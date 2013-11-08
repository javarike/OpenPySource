# coding=utf-8
'''
Created on 2013-7-8

@author: tiande.zhang
'''
from Common.Logger4Py.Logger import Logger

def MethodInvokeTracer(method):
    def tracer(*args):
        traceMessage(method,args)
        return method(*args)
    return tracer


def traceMessage(method,args):
    '''信息记录入日志'''
    logger=Logger()
    logger.TraceLog(method.__name__+" invoked and parameters are "+str(args))
    