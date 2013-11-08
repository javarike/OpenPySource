'''
Created on 2013-7-8

@author: tiande.zhang
'''

from  Common.MethodInovkeTracer import MethodInvokeTracer

class Test(object):
    
    @MethodInvokeTracer
    def Test2(self,arg):
        print(arg)
    

if __name__ == '__main__':
    test1=Test()
    test1.Test2(12312332212132)