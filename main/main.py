# -*- coding:utf-8 -*-  
'''
Created on 2018年6月15日

@author: Administrator
'''
import main.main
from tools.convert import convert_pdf_to_txt
from tools.fixttxt import get_nice_txt, get_translate

if __name__ == '__main__':
    input_path = "../source/1.pdf"
    output_path1 = "../result/1.txt"
    output_path2 = "../result/2.txt"
    output_path3 = "../result/3.txt"
    # 生成英文文件
    convert_pdf_to_txt(input_path,output_path1)
    # 整理文档： 换行 连接 
    #xxxxx xxx xxx wel-
    #come
    get_nice_txt(output_path1,output_path2)
    get_translate(output_path2,output_path3)