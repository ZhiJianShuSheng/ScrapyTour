import base64
import os
import socket

import requests
import time
from scrapy.cmdline import execute

if __name__ =="__main__":
    #epubw_spider
    #huxiu_article_spider
    execute("scrapy crawl epubw_spider".split())

    '''import requests

    proxies = {
        "http": "http://HFUU10742178293P:2BCDA5632F8DC8C1@proxy.abuyun.com:9010",
        "https": "https://HFUU10742178293P:2BCDA5632F8DC8C1@proxy.abuyun.com:9010",
    }

    for i in range(1,2):
       baidu_response = requests.get(url="http://www.landchina.com/", proxies=proxies)
       time.sleep(2)
       print baidu_response.status_code
       '''
