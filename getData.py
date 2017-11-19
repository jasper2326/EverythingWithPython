# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

import time
import re
import pandas as pd
import xml.etree
from twisted.web.client import getPage


def getList():
    place = raw_input("Please input an area.")
    url = 'http://piao.qunar.com/ticket/list.htm?keyword=' + str(place) \
          + '&region=&from=mpl_search_suggest&page{}'
    i = 1
    sightlist = []
    while i:
        page = getPage(url.format(i))
        selector = xml.etree.HTML(page)
        print '������ȡ��' + str(i) + 'ҳ������Ϣ'
        i += 1
        informations = selector.xpath('//div[@class="result_list"]/div')
        for inf in informations:  # ��ȡ��Ҫ��Ϣ
            sight_name = inf.xpath('./div/div/h3/a/text()')[0]
            sight_level = inf.xpath('.//span[@class="level"]/text()')
            if len(sight_level):
                sight_level = sight_level[0].replace('����', '')
            else:
                sight_level = 0
            sight_area = inf.xpath('.//span[@class="area"]/a/text()')[0]
            sight_hot = inf.xpath('.//span[@class="product_star_level"]//span/text()')[0].replace('�ȶ� ', '')
            sight_add = inf.xpath('.//p[@class="address color999"]/span/text()')[0]
            sight_add = re.sub('��ַ��|��.*?��|\(.*?\)|��.*?$|\/.*?$', '', str(sight_add))
            sight_slogen = inf.xpath('.//div[@class="intro color999"]/text()')[0]
            sight_price = inf.xpath('.//span[@class="sight_item_price"]/em/text()')
            if len(sight_price):
                sight_price = sight_price[0]
            else:
                i = 0
                break
            sight_soldnum = inf.xpath('.//span[@class="hot_num"]/text()')[0]
            sight_url = inf.xpath('.//h3/a[@class="name"]/@href')[0]
            sightlist.append(
                [sight_name, sight_level, sight_area, float(sight_price), int(sight_soldnum), float(sight_hot),
                 sight_add.replace('��ַ��', ''), sight_slogen, sight_url])
        time.sleep(3)
    return sightlist, place



def listToExcel(list,name):
    df = pd.DataFrame(list,columns=['��������','����','��������','�𲽼�','������','�ȶ�','��ַ','����','������ַ'])
    df.to_excel(name + '������Ϣ.xlsx')