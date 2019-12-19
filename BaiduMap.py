#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import random
import openpyxl
from openpyxl import Workbook
import requests
import json  # 引用json模块

way_url = 'http://api.map.baidu.com/directionlite/v1/transit'
search_url = 'http://api.map.baidu.com/place/v2/search'
ak = 'M4jyogC1C6iZnbIcF3pt7jx7fYkhS4UW'


def get_way(start, end, region='广州'):
    try:
        paramas = {
            'origin': get_start_position(start, region),
            'destination': get_end_position(end, region),
            'ak': ak,
        }
        response = requests.get(way_url, paramas)
        jsonResponse = response.json()  # 获得返回的结果，结果为json格式
        result = ""
        for route in jsonResponse["result"]["routes"]:
            result += "路线：\n"
            for step in route["steps"]:
                result += "   "+str(step[0]["instruction"])+"\n"
            result += "\n"
        return result
    except Exception as e:
        print(e)


def get_start_position(address, region):
    try:
        paramas = {
            'query': address,
            'region': region,
            'output': 'json',
            'ak': ak,
        }
        response = requests.get(search_url, paramas)
        jsonResponse = response.json()  # 获得返回的结果，结果为json格式
        position = str(jsonResponse["results"][0]["location"]["lat"]) + ","\
            + str(jsonResponse["results"][0]["location"]["lng"])
        return position
    except Exception as e:
        print(e)


def get_end_position(address, region):
    try:
        paramas = {
            'query': address,
            'region': region,
            'output': 'json',
            'ak': ak,
        }
        response = requests.get(search_url, paramas)
        jsonResponse = response.json()  # 获得返回的结果，结果为json格式
        position = str(jsonResponse["results"][0]["location"]["lat"]) + ","\
            + str(jsonResponse["results"][0]["location"]["lng"])
        return position
    except Exception as e:
        print(e)


if __name__ == '__main__':
    start = input("输入起点：\n")
    end = input("输入终点：\n")
    print(get_way(start, end))
