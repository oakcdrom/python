# author:爱在7元钱
# version:1.0
# date:2021年03月11日



import requests
import json, re
url = 'http://api.tianapi.com/txapi/fxrate/index'

def usd():
        currency_str_value = input("请输入要转换的货币金额(例如：100USD):" )
        unit = currency_str_value[-3:].upper()  # 第一次判断
        money = re.findall(r"\d+\.?\d*",currency_str_value)
        body = {
            "key": "your_key",#需要自己去申请
            "fromcoin":unit,
            "tocoin":"CNY",
            "money":money}
        headers = {'content-type': "application/x-www-form-urlencoded"}
        response = requests.post(url, data=body, headers=headers)
        js = json.loads(response.text)
        if js["code"] == 200:
            usd2 = js["newslist"][0]["money"]
            b = {"USD": "美元", "HKD": "港币", "TWD": "新台币", "JPY": "日元", "EUR": "欧元", "AUD": "澳元"}
            name = b.get(unit)
            print('%s 兑换人民币的金额为：%s' % (name, usd2))
        else:
           print('输入错误，请重新输入')


if __name__ == '__main__':
    usd()
