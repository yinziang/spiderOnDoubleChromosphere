# spiderOnDoubleChromosphere

### Brief Introduction

* get latest double chromosphere number and push it via SMS ( requests + BeautifulSoup + twilio )

***

## 双色球爬虫项目
* 需求
    * 爬取最近一期的双色球号码
    * 按固定格式推送到用户
        * "第2018040期 红 02 16 18 19 27 30 蓝 14"

* 想法
    * 利用爬虫框架爬取
        * 简单库 -- requests、BeautifulSoup
    * 调用短信发送框架快速发送
        * twilio短信发送平台

### 实际操作
* 爬取
    1. 直接爬取福彩官网"http://www.cwl.gov.cn"
    2. 利用搜索引擎接口，搜索关键词然后获取结果
        * 搜索接口
            * 百度 -- http://www.baidu.com/s?wd=keyword
            * 360  -- http://www.so.com/s?q=keyword
        * 代码框架
        ```python
        import requests
        keyword = "福彩双色球"
        try:
            kv = {'wd' : keyword}
            r = requests.get("http://www.baidu.com/s", params=kv)
            print(r.request.url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            # TODO
            print(r.text[-500:])
        except:
            print("爬取失败")
        ```

* 信息提取
    * BeautifulSoup
        * 查找标签然后固定提取目标信息

* 短信发送
    * [Twilio官网](https://www.twilio.com/)
        * 注册账号
        * 获取账户SID和AUTH(认证)标志
        * 建立第一个项目并获取免费手机号
    * 代码框架
    
    ```
    # 使用Twilio的免费手机号发送短信
    def send_sms(msg, my_number):
        # 从官网获得以下信息
        account_sid = 'xxxx'
        auth_token = 'xxxx'
        twilio_number = 'xxxx' # 带世界级区号
        client = Client(account_sid, auth_token)
        try:
            client.messages.create(to=my_number, from_=twilio_number, body=msg)
            print('短信已经发送！')
        except ConnectionError as e:
            print('发送失败，请检查你的账号是否有效或网络是否良好！')
            return e
    ```

### 遇到问题、Bug
* BeautifulSoup库的API不熟
* 电话号码格式
    ```TwilioRestException: Unable to create record: The 'To' number 1817127xxxx is not a valid phone number.```
    * 报错如上
    * 加区号
        * "1817127xxxx" --> "+861817127xxxx"

### 反思
* 不太熟悉BeautifulSoup库API，用的查找是硬代码
* 部署及定期(如周二、周四、周日)推送功能还没有实现

