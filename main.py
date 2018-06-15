# -*- coding:utf-8 -*-  
'''
Created on 2018年6月15日

@author: Administrator
'''
import os
import sys
os.chdir(sys.path[0])
# import main.main
from tools.convert import convert_pdf_to_txt
from tools.fixttxt import get_nice_txt, get_translate
from optparse import OptionParser 

if __name__ == '__main__':
    usage = "\n %prog [options] arg1 arg2"  
    parser = OptionParser(usage)  
    parser.add_option("-c", "--convert", dest="convert",action="store_true",
                  help="convert pdf to txt")  
    parser.add_option("-f", "--fixtxt", dest="fixtxt",  action="store_true",
                  help="fix txt to nice txt")  
    parser.add_option("-t", "--translate", dest="translate", action="store_true",
                  help="translate txt from English to Chinese")  
    parser.add_option("-a", "--all",  action="store_true",
                  dest="all", 
                  help="do it all")  
#     parser.add_option("-i", "--input",  dest="input", 
#                   help="input filename")
#     parser.add_option("-o", "--output", dest="output", 
#                   help="output filename")
  
    (options, args) = parser.parse_args() 
#     print options
#     print args
    _len = len(args)
#     print _len
    if _len!=2:
        parser.error( "error in number of argv")

    if options.all:
        print "here"
        input_filename = args[0]
        output_filename = args[1]
        input_path = "source/"+input_filename+".pdf"
        output_path1 = "result/"+output_filename+"_1.txt"
        output_path2 = "result/"+output_filename+"_2.txt"
        output_path3 = "result/"+output_filename+"_3.txt"
        # 生成英文文件
        convert_pdf_to_txt(input_path,output_path1)
        # 整理文档： 换行 连接 
        #xxxxx xxx xxx wel-
        #come
        get_nice_txt(output_path1,output_path2)
        get_translate(output_path2,output_path3)
    elif  options.convert:
        input_filename = args[0]
        output_filename = args[1]
        input_path = "source/"+input_filename+".pdf"
        output_path = "result/"+output_filename+".txt"
        convert_pdf_to_txt(input_path,output_path)
    elif  options.fixtxt:
        input_filename = args[0]
        output_filename = args[1]
        input_path = "result/"+input_filename+".txt"
        output_path = "result/"+output_filename+".txt"
        get_nice_txt(input_path,output_path)
    elif  options.translate:
        input_filename = args[0]
        output_filename = args[1]
        input_path = "result/"+input_filename+".txt"
        output_path = "result/"+output_filename+".txt"
        get_translate(input_path,output_path)