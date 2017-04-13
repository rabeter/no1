import requests as re
import time

def urlToHtml(url):
    try:
        r = re.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "获取资源错误"

if __name__ == '__main__':
    start = time.time()
    for i in range(100):
        url = "http://www.bilibili.com/video/av91390" + str(i)
        print(url)
        print(urlToHtml(url))
    end = time.time()
    print(end-start)