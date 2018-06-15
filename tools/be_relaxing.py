# -*- coding:utf-8 -*-  
'''
Created on 2018年6月14日

@author: Administrator
'''
import random
import time
def be_relaxing(mute=True):
    '''
    随机休息一会儿
    '''
    _first = random.randint(0,5)
    _seconds = random.randint(0,3+_first)
    if not mute:
        print ("sleep for little time : "+str(_seconds))
    time.sleep(_seconds)
if __name__ == '__main__':
    be_relaxing()
        