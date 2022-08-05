# http://www.pythonchallenge.com/
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

import os
import zipfile

def py6(): #channel.html 
    '''<html> <!-- <-- zip --> 因此把channel.html改为channel.zip 
        hint1: start from 90052 得到collect the comments
        hint2: answer is inside the zip 说明要打印zip里的comments
        最终得到关键词 HOCKEY，修改 URL 的 channel => hockey，访问链接得到 it's in the air. look at the letters => oxygen.html'''
    path = './challenge/channel/'
    # file_list = []
    # for f in os.listdir(path):
    #     if f != 'readme.txt' and f != 'channel.zip':
    #         file_list.append(os.path.join(path, f))
    
    # next_file = '90052.txt'
    # for i in range(0, len(file_list)):
    #     with open(os.path.join(path, next_file), 'r') as p:
    #         txt = p.read()
    #         next_no = txt[txt.find('is ') + 3:]
    #         print(next_no)
    #         next_file = next_no + '.txt'
    def next_num(next_file):
        with open(os.path.join(path, next_file), 'r') as p:
            txt = p.read()
            next_no = txt[txt.find('is ') + 3:]
            print(next_no)
            next_file = next_no + '.txt'
        return next_file
    
    next_file = '90052.txt'
    comments = []
    with zipfile.ZipFile(path + 'channel.zip', 'r') as file:
        count = len(file.infolist()) - 1
        for i in range(count):
            print(file.getinfo(next_file).comment)
            comments.append(file.getinfo(next_file).comment)
            next_file = next_num(next_file)

    for comment in comments:
        print(comment.decode("utf-8"), end='')

from PIL import Image
def py7(): #oxygen.html
    '''特色像素点->取r->转ascii'''
    image_file = os.getcwd() + '\\challenge\\oxygen.png'
    with Image.open(image_file) as im:
        row = [im.getpixel((x, im.height/2)) for x in range(im.width)]
        #print(row)
    
    row = row[::7] #每七个像素点对应图片上那条灰线的一个色块。
    #print(row)
    row = [r for r, g, b, a in row if r == g == b] #rgba，a表示透明度，因为这条线末端并没有横穿整个图片，过滤灰度图像，R=B=G。
    for i in row:
        print(chr(i), end='') #smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
    for j in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
        print(chr(j), end='')

import bz2
def py8(): #integrity.html
    ''' BZh9 这个前缀有没有感觉，用bz2压缩文本的前缀就是这个，而且从蜜蜂bee的发音，标题working hard = busy，无一不在提示 bz2
        bz2解压缩html里的注释user，password'''
    print(bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
    print(bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))

from PIL import Image
first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
        310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
        190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
        389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
        215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
        290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
        279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
        327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
        328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
        259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
        352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
        120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
        214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
        102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
        113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
        133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
        111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
        332,155,348,156,353,153,366,149,379,147,394,146,399]
second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
        157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
        125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
        77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
        158,121,157,128,156,134,157,136,156,136]

def py9_1(): #good.html
    '''提示first+second，于是两个一组画坐标得到牛，牛：cow, cattle, ox, bull, beef.试试看看，bull.html'''
    print(max(first), max(second))
    im = Image.new('RGB', (500, 500))
    for i in range(len(first)//2):
        im.putpixel((first[i*2], first[i*2+1]), (255, 255, 255))
        
    for i in range(len(second)//2):
        im.putpixel((second[i*2], second[i*2+1]), (255, 255, 255))

    im.show()

from matplotlib import pyplot as plt
def py9_2():
    ls = first + second
    x = []
    y = []

    for i in range(len(ls)):
        if i % 2 == 0:
            x.append(ls[i])
        else:
            y.append(0 - ls[i])
    
    plt.scatter(x, y)
    plt.show()

def py10():
    '''11--- 表示前一个数“1”是 1 个 1； 
        21--- 表示前一个数“11”是 由 2 个 1 组成；
        1211--- 表示前一个数“21”是由1个2、1个1组成； 
        111221--- 即11、12、21 ，表示前一个数“1211”是依次由1个1，1个2；
        312211---即31、22、11，表示前一个数“111221”是依次由 3 个 1，2 个 2
        len(a[30]) = ? 代入31'''
    def get_sequence(n):
        if (n == 1):
            return "1"
        if (n == 2):
            return "11"

        s = "11"
        for i in range(3, n + 1):
            s += '$'
            l = len(s)

            cnt = 1
            tmp = ""

            for j in range(1, l):
                if (s[j] != s[j - 1]):
                    tmp += str(cnt)
                    tmp += s[j - 1]
                    cnt = 1
                else:
                    cnt += 1
            s = tmp
        return s

    print(len(get_sequence(31))) #5808.html

def py11(): #5808.html
    '''odd even'''
    im = Image.open('./challenge/cave.jpg', 'r')
    oddImg = Image.new('RGB', (640, 480))
    evenImg = Image.new('RGB', (640, 480))

    for i in range(im.width):
        for j in range(im.height):
            r, g, b = im.getpixel((i, j))
            if i % 2 == 0 and j % 2 == 0:
                oddImg.putpixel((i, j), (r, g, b))
            else:
                evenImg.putpixel((i, j), (r, g, b))

    oddImg.show() #站起来俯视角度，有一个单词 evil
    evenImg.show()

def py12(): #evil.html
    '''封面发牌分5份，所以步长5分成5张图片，把5张图片单词拼起来disproportional
       evil4.jpg，还真能访问到，但图是裂的。如果有一张能下载到的图片但是是裂图，下载下来，Bert is evil! go back!
       http://www.pythonchallenge.com/pc/return/bert.html 成功跳转，得到一段话：Yes! Bert is evil! '''
    with open('./challenge/evil2.gfx', 'rb') as fp:
        data = fp.read()
        for i in range(5):
            open('./challenge/evil_%d.jpg' % i, 'wb').write(data[i::5])

import xmlrpc.client
def py13(): #disproportional
    '''aultCode 105 | fault String XML error: Invalid document end at line 1, column 1发现是xmlrpc库
        Yes! Bert is evil!
        xmlrpc调用后，把 ITALY 替换到 URL 中，访问得到：SMALL letters.'''    
    conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    print(conn.system.listMethods())
    print(conn.system.methodSignature('phone'))
    print(conn.system.methodHelp('phone'))
    print(conn.phone('Bert')) #555-ITALY

def py14():
    im = Image.open('./challenge/wire.png')
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    out = Image.new('RGB', [100, 100])
    x, y, p = -1, 0, 0
    d = 200
    while d / 2 > 0:
        for v in delta:
            steps = d // 2
            for s in range(steps):
                x, y = x + v[0], y + v[1]
                out.putpixel((x, y), im.getpixel((p, 0)))
                p += 1
            d -= 1
    out.show()


if __name__ == '__main__':
    #py1_1()
    py12()
