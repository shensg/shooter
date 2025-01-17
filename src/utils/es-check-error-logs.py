# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

# tg机器人token和群ID，群ID以'-'开头的一串数字
api_token = ''
chat_id = ''
username = "elastic"
password = ""

# 获取今天日期
current_date = datetime.now()
formatted_date = current_date.strftime('%Y.%m.%d')

def notice(message):
    url = f"https://api.telegram.org/bot{api_token}/sendPhoto"
    image = "https://img-blog.csdnimg.cn/img_convert/c21922e02690708f50176370542d44fe.png"
    # 构造要发送的数据
    data_content = {
        "chat_id": chat_id,
        "photo": image,
        "caption": message
    }

    # 发送 POST 请求
    response = requests.post(url, data=data_content)
    # 检查响应
    if response.status_code == 200:
        print("测试消息发送成功!")
    else:
        print(f"测试发送失败，错误码: {response.status_code}")

    return {"code": 200, "msg": "success", "data": ""}


def es_issue(stated):
    # Elasticsearch 地址
    url = f"http://172.16.19.124:9200/nginx-access-{formatted_date}/_search"

    # 查询的请求体 (你可以根据需要更改)
    query = {
        "query": {
            "bool": {
                "filter": [
                    {"term": {"status": stated}},
                    {"range": {"@timestamp": {"gte": "now-15m", "lte": "now"}}}
                ]
            }
        },
        "size": 0
    }

    # 发起 GET 请求并传递身份验证
    response = requests.get(url, json=query, auth=HTTPBasicAuth(username, password))

    # 输出响应内容
    if response.status_code == 200:
        data = response.json()
        formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stated = query['query']['bool']['filter'][0]['term']['status']

        if data['hits']['total']['value'] >= 50:
            level = "紧急"
            content = """*ElasticSearch*\n告警时间: {}\n报警级别: {}\n告警规则: Nginx15分钟内出现<{}>日志超过50次\n监控指标: Nginx-access-{}-logs\n出现次数: {}""".format(
                formatted_time, level, stated, stated, data['hits']['total']['value'])
            r = notice(content)
            print(r)
        elif data['hits']['total']['value'] >= 20:
            level = "告警"
            content = """*ElasticSearch*\n告警时间: {}\n报警级别: {}\n告警规则: Nginx15分钟内出现<{}>日志超过20次\n监控指标: Nginx-access-{}-logs\n出现次数: {}""".format(
                formatted_time, level, stated, stated, data['hits']['total']['value'])
            r = notice(content)
            print(r)
    else:

        print(f"Error: {response.status_code} - {response.text}")


if __name__ == '__main__':
    numbers = [400, 403, 404, 500, 502]
    for number in numbers:
        es_issue(number)

