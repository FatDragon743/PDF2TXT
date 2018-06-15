# PDF2TXT
## Introduction
**将英文论文的PDF文件转化为txt，进行简单的排版整理，爬取google翻译，每个步骤生成一个文件**

要翻译的文章放在source文件夹，将会寻找input_filename.pdf。  
翻译好的文件放在result文件夹，其中 output_filename.txt 。  
如果嫌麻烦，也可以直接在pycharm或者eclipse等IDE里运行 ../main/test_main.py 文件。   
如果认为翻译慢的，可以改变../tools/be_relaxing.py 文件中的random.randint(0,5)语句中的值，用于缩短随机等待时间，默认是0-5s

## Usage:
 python 2.7.*   
 pip install pdfminer==20140328   
 pip install requests   
 pip install beautifulsoup4

    Usage:   
     main.py [options] arg1 arg2
    
    Options:   
      -h, --help    	show this help message and exit   
      -c, --convert 	convert pdf to txt   
      -f, --fixtxt  	fix txt to nice txt   
      -t, --translate  	translate txt from English to Chinese   
      -a, --all			do it all   
  
## Example:
    python2 .\main.py -a 1 2   
    input :1.pdf   
    output:2_1.txt, 2_2.txt, 2_3.txt   
    
    python2 .\main.py -c 1 2   
    input :1.pdf   
    output:2.txt   
    
    python2 .\main.py -f 1 2   
    input :1.txt   
    output:2.txt   
    
    python2 .\main.py -t 1 2  
    input :1.txt  
    output:2.txt  


