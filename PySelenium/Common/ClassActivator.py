# -*- coding: utf-8 -*- 
'''
Created on 2013-6-17

@author: tiande.zhang
'''

class ClassActivator(object): 
    '''本类用来动态创建类的实例'''   
    def createInstance(self,class_name, *args, **kwargs):
        '''动态创建类的实例。 
     [Parameter] 
     class_name - 类的全名（包括模块名） 
    *args - 类构造器所需要的参数(list) 
    **kwargs - 类构造器所需要的参数(dict) 
    [Return] 
              动态创建的类的实例 
    [Example] 
    class_name = 'knightmade.logging.Logger' 
    logger = Activator.createInstance(class_name, 'logname') 
   '''
        (module_name, class_name) = class_name.rsplit('.', 1)
        module_meta = __import__(module_name, globals(), locals(), [class_name]) 
        class_meta = getattr(module_meta, class_name) 
        instance = class_meta(*args, **kwargs) 
        return instance