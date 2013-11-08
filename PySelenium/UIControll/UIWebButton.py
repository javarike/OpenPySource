'''
'''
from UIControll.UIWebControll import UIWebControll

class WebButton(UIWebControll):
    '''
    classdocs
    '''


    def __init__(self,browser,uielement):
        '''
        Constructor
        '''
        print(uielement.NodeID)
        super().__init__(browser,uielement)
        