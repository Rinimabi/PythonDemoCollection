import urllib.request
import json
import threading
from tkinter import *
import sys
import imp
imp.reload(sys)

def get_zhanji():
    name = str(et.get())
    print('name:', name)
    url = 'http://api.lolbox.duowan.com/api/v2/player/search/?player_name_list=%s&callback=jQuery111200161216930093' \
          '95033_1470488155157&_=1470488155158' % name
    res = urllib.request.urlopen(url)
    html = res.read()[44:-1]
    print(html)
    zhanji = json.loads(html)[u'player_list']
    t.delete(0.0, END)
    for i in zhanji:
        print('服务器：%s   当前战力：%s' % (i['game_zone']['alias'], i['box_score']))
        print('当前段位：%s' % (i['tier_rank']['tier']['full_name_cn'] + i['tier_rank']['rank']['name']))
        # print i['game_zone']['alias']
        # print zhangji
        # print html
        t.insert(END, '服务器：%s   当前战力：%s' %
                 (i['game_zone']['alias'], i['box_score']))
        t.insert(END, '当前段位：%s\n' % (
            i['tier_rank']['tier']['full_name_cn'] + i['tier_rank']['rank']['name']))


def rukou():
    if et.get() == '':
        print('请输入召唤师名称')
    else:
        get_zhanji()


# def qidong():
#     t1 = threading.Thread(target=rukou)
#     t1.start()
# get_zhanji()
# print len(jQuery11120016121693009395033_1470488155157()

root = Tk()
root.title('LOL战绩查询')
root.geometry()

et = Entry(root, font=('宋体, 16'))
et.grid()

b = Button(root, text='开始查询', font=('宋体， 12'), command=rukou)
b.grid()

t = Text(root, font=('宋体, 16'))
t.grid()

root.mainloop()
