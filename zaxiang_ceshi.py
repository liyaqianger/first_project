# coding:utf-8

# 字符串切割

aa = "http://news.cncjw.com.cn/xinwen/2018/0730/694.html"
print aa.split("/")

html = aa.split("/")[0]+"//"+aa.split("/")[2]
print html


a1 = "https://www.baidu.com/s?wd=site%3Anews.cncjw.com.cn&pn=0&oq=site%3Anews.cncjw.com.cn&ct=2097152&ie=utf-8&si=news.cncjw.com.cn&rsv_pq=f29f46d600070bf7&rsv_t=be52QPsIod5rLjSH0lYeaFq6j%2B9dz6y3Er1E%2BRSkVl3SGsbsvm3YTesHVrA&gpc=stf%3D1546566779%2C1547171579%7Cstftype%3D1&tfflag=1&sl_lang=cn&rsv_srlang=cn"
a2 = "https://www.baidu.com/s?wd=site%3Anews.cncjw.com.cn&pn=0&oq=site%3Anews.cncjw.com.cn&ct=2097152&ie=utf-8&si=news.cncjw.com.cn&rsv_pq=ff56079900073eb0&rsv_t=8446KQf%2BiGVw0cVdIZ5y47KFLouuQxunzmTwEncr6Upcn0ljrgCS7HZ4zKw&gpc=stf%3D1544495124%2C1547173524%7Cstftype%3D1&tfflag=1&sl_lang=cn&rsv_srlang=cn"
c1 = "https://www.baidu.com/s?wd=site%3Amoney.china.com&pn=0&oq=site%3Amoney.china.com&ct=2097152&ie=utf-8&si=money.china.com&rsv_pq=88a6a59c0007ccf7&rsv_t=e8e8k825wYvNToRRvRYUu0S8NsUs5GYjsTTs78h4iFhilWwCt9owwfTLxK8&gpc=stf%3D1546570752%2C1547175552%7Cstftype%3D1&tfflag=1&sl_lang=cn&rsv_srlang=cn"
c2 = "https://www.baidu.com/s?wd=site%3Amoney.china.com&pn=0&oq=site%3Amoney.china.com&ct=2097152&ie=utf-8&si=money.china.com&rsv_pq=9308b3c40007efd6&rsv_t=f3a6dIpfr3TNIDasa9mLHiCEE9U0BfLcbqfHlh%2B1jcDpfWlI8ng5BMJx9nw&gpc=stf%3D1546571299%2C1547176099%7Cstftype%3D1&tfflag=1&sl_lang=cn&rsv_srlang=cn"


site = "http://tool.chinaz.com/baidu/?lm=7&wd=news.cncjw.com.cn&pn=0&pagesize=20&btime=&etime="

c = "/html/body/div[@class='m-content g-wp f-cb']/div[@class='main']/div[@class='m-article']/div[@id='content']/p[1]/img/@src"
a = "/html/body/div[@class='m-content g-wp f-cb']/div[@class='main']/div[@class='m-article']/div[@id='content']/p[1]//img/@src"
b = "/html/body/div[@class='m-content g-wp f-cb']/div[@class='main']/div[@class='m-article']/div[@id='content']/p[1]/img/@src"

bb = "//div[@class='w1000 information_box right']/span[1]"
cc = "//div[@class='w1000 information_box right']/a/text()"

