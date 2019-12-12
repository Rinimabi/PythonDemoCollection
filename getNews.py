import urllib.request
import chardet
import re
from tkinter import *


def getCnbetaNews():
    page = urllib.request.urlopen(
        'https://www.cnbeta.com/')  # 打开网页
    htmlCode = page.read()
    data = htmlCode.decode('utf-8')
    # 正则表达式
    reg = r'<li><a href=\"(.+?)\" target=\"_blank\">(.+?)\</a></li><li>'
    reg_title = re.compile(reg)
    titlelist = reg_title.findall(data)  # 进行匹配
    num = 0
    print("cnbeta新闻：")
    for name in titlelist:
        num += 1
        if(len(name[1]) > 6):
            print("【", num, "】 -> ", name[1], "，", name[0])


#cnbeta新闻
getCnbetaNews()
