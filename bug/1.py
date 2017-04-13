import requests

r = requests.get("http://www.baidu.com")
# get(url,) 资源请求对象

print(r.raise_for_status())

print(r.status_code,r.text,r.encoding,r.content)
# status_code 状态码
# text 内容
# encoding 默认编码方式
# apparent_encoding 备选编码(真正编码)
