# https://www.bilibili.com/video/av4050443/?p=54

import urllib.request
response = urllib.request.urlopen("http://www.fishc.com")
html = response.read()
html = html.decode("utf-8") # 解码
print(html)
