import json
from born_prime import *
import requests
import hashlib
from fast_exp import quick_algorithm
from extend_gcd import *
from mypow import *

userkey={}
#注册界面
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

k=1234567890
userkey[username]=k

x=(vn*quick_algorithm(k,e,n))%n
x=str(x)
#print(x)

#获得注册码界面
params={'x':x}
address='https://mockapi.eolink.com/6QVS7t1d18916567af4d46ffb579dc4e035981316fe67b6/getm'
r=requests.post(address,json=params)

r=json.loads(r.text)
y=53717050295156175141299666853483104927481852761632004360349585816680051688453198848378519925084430636040329782206407962236517290354334764837330574271798281998113453403848503453838992242361788455599882418763829669566055675077988461656340153058798547448796652096530658269522063786538517299615407873998692939804
m=exgcdinv(y,k)



#登陆界面
if m**e
params={'vn':str(vn),'m':str(m)}
address='https://mockapi.eolink.com/6QVS7t1d18916567af4d46ffb579dc4e035981316fe67b6/mylogin'
r=requests.post(address,json=params)

r=json.loads(r.text)
print(r)
