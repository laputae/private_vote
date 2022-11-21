import json

import requests
import hashlib

username=input('请输入你的用户名：')
md5 = hashlib.md5()
md5.update(username.encode('utf-8'))
usrmd5=md5.hexdigest()
params={'ID':usrmd5}
address='https://mockapi.eolink.com/6QVS7t1d18916567af4d46ffb579dc4e035981316fe67b6/myregister'
r=requests.post(address,json=params)
r=json.loads(r.text)
#print(r)
vn=int(r['vn'])
e=int(r['e'].split(',')[0])
n=int(r['e'].split(',')[1])
#print(vn)
#print(e)
#print(n)
x=vn*(k**e)%n

