# -*- coding:utf-8 -*-  
'''
Created on 2018年6月14日

@author: Administrator
'''

import json
# from translate import Translator
from tools.translation import google_translate_EtoC
from tools.be_relaxing import be_relaxing
import sys

def confir(str):
    for i in range(0,32):
        str = str.replace(chr(i),'')
    str = str.replace("- ","")
    return  str
def get_nice_txt(_input,_ouput):
    print "start to get nice txt"
    i =0
    with open(_input,"r") as fp:
        with open(_ouput,"w") as f_w:
            _print = ''
            _flag = True
    #         _pro = fp.readline()
            for _con in fp.readlines():
                i=i+1
                if (i<20000000000000):
                    if (_con == '\n'):
                        _flag = False
                        if not _print == '':
                            _print = confir(_print)
                            f_w.write(_print+"\n")
#                             print _print[:16]
                            _print = ''
                    else:
                        _print =_print +" "+_con
    print "get nice txt over"
# def translateGoogle2(text):
#     translator= Translator(to_lang="zh")
#     result = translator.translate(text)
#     print result
#     return result
def get_translate(_input,_ouput):
    print "start to translate"
    i=0
    with open(_input,"r") as fp:
        with open(_ouput,"w") as f_w:
            _content = fp.readlines()
            _len = len(_content)
            for _con in _content:
                i=i+1
                if (i<20000000000000):
#                     print _con
                    if(len(_con)>=50):

                        tran = google_translate_EtoC(_con).encode("utf-8")
#                         print ('\r'+str(i*100.0/_len))
                        num1 = i*100/_len
                        s1 = "\r[%s%s] %d%%"%("*"*num1," "*(100-num1),num1)
#                         print('\b' * len(str(i*100.0/_len)), end='', flush=True)
                        sys.stdout.write(s1)
                        sys.stdout.flush()
                        be_relaxing()
#                         print("翻译结果为：%s"%(tran))
                        f_w.write(tran+"\n")
    print "\ntranslate over"
if __name__ == '__main__':
#     get_nice_txt()
    get_translate()