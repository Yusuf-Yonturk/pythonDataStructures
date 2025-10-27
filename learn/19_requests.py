import requests
import os
from PIL import Image


url = 'https://www.ibm.com/'
r=requests.get(url)
print(r.status_code)

print(r.request.headers)
print("request body: ",r.request.body)

header=r.headers
print(header)
print(header['Date'])
print(header['Content-Type'])
print(r.encoding)

print(r.text[0:100])

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":123}
r=requests.get(url_get,params=payload)
print(r.url)
print(r.request.body)
print(r.status_code)
print(r.text)
print(r.headers)

url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)


print("POST request URL:", r_post.url)  

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)
