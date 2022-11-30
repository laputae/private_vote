import requests
import hashlib
from fast_exp import quick_algorithm
import json
import glovar

#注册界面
def register(username):
    print('hahhahhahahhaha')
    print(username)
    md5 = hashlib.md5()
    md5.update(username.encode('utf-8'))
    usrmd5=md5.hexdigest()
    params={'ID':usrmd5}
    address='https://mockapi.eolink.com/6QVS7t1d18916567af4d46ffb579dc4e035981316fe67b6/myregister'
    r=requests.post(address,json=params)
    print(r.status_code==200)
    r=json.loads(r.text)

    vn=int(r['vn'])
    glovar.setvalue('vn', vn)
    e=int(r['e'].split(',')[0])
    glovar.setvalue('e',e)
    n=int(r['e'].split(',')[1])
    glovar.setvalue('n',n)
    k=1234567890
    glovar.setvalue('k',k)
    x=(vn*quick_algorithm(k,e,n))%n
    x=str(x)
    glovar.setvalue('x', x)
