#!/Users/yin/anaconda3/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

"""
读取HTML页面文本
"""
def getHTMLText(url, keyword):
    try:
        kv = {'wd' : keyword}
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

"""
解析HTML页面
"""
def getInfo(html):
    soup = BeautifulSoup(html, "html.parser")   
    info_list = []
    try:
        # 查找期数信息
        a = soup.find_all('b')
        info_list.append(a[1].string)
        div_info = soup.find('div', attrs={'class':'c-border c-gap-bottom-small'})
        # 查找红球信息
        # 属性attrs根据页面源代码得知
        red_list = div_info.find_all(attrs={'class':'c-icon c-icon-ball-red op_caipiao_ball_red c-gap-right-small'})
        blue_list = div_info.find_all(attrs={'class':'c-icon c-icon-ball-blue op_caipiao_ball_blue c-gap-right-small'})
        info_list.append('红')
        for i in red_list:
            info_list.append(i.string)
        # 查找蓝球信息
        info_list.append('蓝')
        info_list.append(blue_list[0].string)
        return info_list
    except:
        return info_list

# 使用Twilio的免费手机号发送短信
def send_sms(msg, my_number):
    # 从官网获得以下信息
    account_sid = 'AC26ac1ccfc208665209d2dcad61fbf8e9'
    auth_token = 'afaa1b7f574302e1ea942b69dc66afbe'
    twilio_number = '+12565675704'

    client = Client(account_sid, auth_token)
    try:
        client.messages.create(to=my_number, from_=twilio_number, body=msg)
        print('短信已经发送！')
    except ConnectionError as e:
        print('发送失败，请检查你的账号是否有效或网络是否良好！')
        return e

def main():
    url = "http://www.baidu.com/s"
    keyword = "福彩双色球"
    # 获取所有查询信息
    info_list = getInfo(getHTMLText(url, keyword))
    # 推送信息
    info = ''
    for i in info_list:
        info = info + ' ' + i 
    send_sms(info, '+861817127xxxx')

if __name__ == "__main__":
    main()
