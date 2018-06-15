# -*- coding:utf-8 -*-  
'''
Created on 2018年6月14日

@author: Administrator
'''
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path,save_name):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    try:
        fp = file(path, 'rb')
        print "read %s succeed!"%path
    except:
        print "error in read input file"
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    try:
        with open("%s"%save_name,"w") as f:#格式化字符串还能这么用！
            for i in str:
                f.write(i)
        print "%s write succeed!"%save_name
    except:
        print "Writing Failed!"

if __name__ == '__main__':   
    convert_pdf_to_txt('1.pdf',"c.txt")