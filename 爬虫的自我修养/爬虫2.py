# download a cat
import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/400/500")
cat_img = response.read()

with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
'''
>>> response.info()
<http.client.HTTPMessage object at 0x03CF2F90>
>>> response.geturl()
'http://placekitten.com/g/500/600'
>>> print(response.info())
Date: Sun, 14 Jul 2019 13:58:43 GMT
Content-Type: image/jpeg
Transfer-Encoding: chunked
Connection: close
Set-Cookie: __cfduid=d10a55a4690c5f68a7d94aa750ef4cdb11563112723; expires=Mon, 13-Jul-20 13:58:43 GMT; path=/; domain=.placekitten.com; HttpOnly
Access-Control-Allow-Origin: *
Cache-Control: public, max-age=86400
Expires: Mon, 15 Jul 2019 13:58:43 GMT
CF-Cache-Status: HIT
Age: 43364
Vary: Accept-Encoding
Server: cloudflare
CF-RAY: 4f6403599e1069db-LHR


>>> response.getcode()
200
>>>
'''
