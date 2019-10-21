import urllib.request
import urllib.parse
import json

def translate():

    content = input('请输入需要翻译的文本：\n')

    head = {}
    head['User-Agent']="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

    url = 'http://fy.iciba.com/ajax.php?a=fy'

    data = {}
    #data['type'] ='AUTO'
    data['f']= 'auto'
    data['t']= 'auto'
    data['w']= content
    #data['doctype']= 'json'
    #data['xmlVersion']='1.6'
    #data['keyfrom']='fanyi.web'
    #data['ue']='UTF-8'
    #data['typoResult'] = 'true'

    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    target = json.loads(html)
    #print(target)
    try:
        print('翻译结果：\n%s\n' %(target['content']['out']))
    except:
        word_mean = target['content']['word_mean']
        j = len(word_mean) 
        print('翻译结果：\n')
        for i in range(0,j):
            print(word_mean[i])

    input('输入任意键继续程序\n')

    ## 可以从b站学的此程序原理 链接如下
    ## https://www.bilibili.com/video/av4050443/?p=55

while(1):
    translate()
