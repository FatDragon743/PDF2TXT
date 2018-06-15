# -*- coding:utf-8 -*-  
'''
Created on 2018年6月14日

@author: Administrator
'''

import json
from translate import Translator
from tools.translation import google_translate_EtoC
from tools import be_relaxing

def confir(str):
    for i in range(0,32):
        str = str.replace(chr(i),'')
    str = str.replace("- ","")
    return  str
def get_nice_txt():
    i =0
    with open("c.txt","r") as fp:
        with open("cc.txt","w") as f_w:
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
                            print _print[:16]
                            _print = ''
                    else:
                        _print =_print +" "+_con
def translateGoogle2(text):
    translator= Translator(to_lang="zh")
    result = translator.translate(text)
    print result
    return result
def get_translate():
    i=0
    with open("cc.txt","r") as fp:
        with open("ccc.txt","w") as f_w:
            for _con in fp.readlines():
                i=i+1
                if (i<20000000000000):
#                     print _con
                    if(len(_con)>=50):
                        be_relaxing()
                        tran = google_translate_EtoC(_con).encode("utf-8")
#                         print("翻译结果为：%s"%(tran))
                        f_w.write(tran+"\n")
if __name__ == '__main__':
#     get_nice_txt()
    get_translate()