# import datetime
# d=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d')
# print(d)

from datetime import datetime
d = datetime.strftime(datetime.now(),'%Y-%m-%d')
print(d)
import string
#0
print(2**38)
#1
def py1_1():
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = s.lower()
    source = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
    li = []

    for a in source:
        j = s.find(a)
        if j > 0:
            i = j + 2
            li.append(s[i%26])
        else:
            li.append(a)
    
    print(''.join(li))
    print('map'.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")))
 
def py1_2():
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    res = s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab"))
    print(res)

def py1_3():
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    sl = s.split(" ")
    print (" ".join(["".join(map(lambda x:ord(x)+2>122 and chr(ord(x)+2-26) or chr(ord(x)+2),list(x))) for x in sl]))

import requests
import re
from collections import Counter
def py2():
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    s = requests.get(url)
    reg = re.compile('<!--.*?-->.*?<!--(.*?)-->',re.S)
    res = reg.search(s.text).group(1)
    #print(res)
    counter = Counter(res)
    print(counter.most_common()) 

import urllib.request as rr
def py3(): #equality.html
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    #s = requests.get(url)
    s = rr.urlopen(url)
    j = str(s.read())
    s.close()
    start = j.find('<!--')
    sj = j[start:]
    reg = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]') #[^A-Z]除了大写字母以外的字符，加了这个限定才能表示只能有３个大写字母
    #print(reg.findall(sj))
    res = ''.join(reg.findall(sj))
    print(res)

def py4(): #linkedlist.php
    ss = '12345'
    for x in range(1, 401):
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'.format(ss)
        s = requests.get(url)
        reg = re.compile('nothing is (\d+)',re.S)
        if s.text.find("Divide by two")==-1:
            res = reg.search(s.text).group(1)
        else:
            res = int(res)/2
        print(x, res)
        ss = str(res)

import pickle
def py5(): #peak.html 
    f = open("/home/saizong/workspace/banner.p.txt","rb+")
    s = pickle.load(f)
    f.close()
    for row in s:
        cols = ''.join([col[0]*col[1] for col in row])
        print(cols)
        print('\n')

def py６(): #channel.html
    pass
#py1_1()
py5()
