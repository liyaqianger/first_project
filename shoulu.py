# coding:utf-8

import requests
import random, time
from xlwt import *
from lxml import etree


class Shoulu():
        # 设置默认属性
    def __init__(self):
        user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36',
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36"
    ]
        self.headers = {"User_agent": random.choice(user_agent)}
        self.aa = 1

    def send_request(self):
        print "doing send_request..............................."
        for data in self.get_url():
            tool_url = "http://tool.chinaz.com/baidu/?lm=7&wd={}&pn=0&pagesize=20&btime=&etime=".format(data[0])
            # print tool_url
            time.sleep(random.randint(1, 3))
            response = requests.get(url=tool_url, headers=self.headers)
            content = etree.HTML(response.text)
            try:
                num = content.xpath("//span[@class='col-blue02'][3]/a/text()")[0]
                print data[0], response.status_code, num
                yield data[1], num
            except Exception as error:
                num = 0
                print error, data[0], response.status_code, num, "无收录".decode('utf-8')
                yield data[1], num

    def keep_data(self):
        print "downloading the data......"
        # aa = 1
        title_file = Workbook(encoding="utf-8")
        table = title_file.add_sheet("web_shulu")
        # 写入表头
        table.write(0, 0, "id")     # 写入表头第一行第一列
        table.write(0, 1, "url")    # 表头第一行第二列
        table.write(0, 2, "收录量".decode("utf-8"))   # 表头第一行第三列
        # data = self.send_request()
        for data in self.send_request():
            table.write(self.aa, 0, self.aa)
            table.write(self.aa, 1, data[0])
            table.write(self.aa, 2, data[1])

            self.aa += 1
        title_file.save("shoulu.xls")
        # if url =="" or num == "":
        #     print "working done......"
        # title_file.save("shoulu.xls")
        # break

    def get_url(self):  # 获取
        with open("C:\Users\Administrator\Desktop\shoulu.txt") as file:
            for url in file.readlines():
                # print url
                html = url.split("/")[2]
                yield html, url



A = Shoulu()

A.keep_data()

