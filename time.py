# author:爱在7元钱
# version:1.0
# date:2021年03月15日


import requests
import json

url = 'http://api.tianapi.com/txapi/worldtime/index'

def worldtime():
    currency_str_value = input("请输入要查询的城市(例如：芝加哥):")
    city1 = currency_str_value
    body = {
        "key": "4108a26018b10ff2e99914a1b74d518e",
        "city": city1}
    headers = {'content-type': "application/x-www-form-urlencoded"}
    response = requests.post(url, data=body, headers=headers)
    js = json.loads(response.text)
    if js["code"] == 200:
        city2 = js["newslist"][0]["city"]
        timezone = js["newslist"][0]['timeZone']
        time1 = js["newslist"][0]['strtime']
        print('%s 的时区为：%s' % (city2, timezone))
        print('%s 的当前时间为: %s' %(city2, time1))
    else:
        print('输入错误，请重新输入')


if __name__ == '__main__':
    worldtime()
