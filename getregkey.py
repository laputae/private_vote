import json
import requests
from extend_gcd import *
import glovar

def getregkey():
    x=glovar.getvalue('x')
    k=glovar.getvalue('k')
    params={'x':x}
    address='https://mockapi.eolink.com/6QVS7t1d18916567af4d46ffb579dc4e035981316fe67b6/getm'
    r=requests.post(address,json=params)
    if r.status_code==200:
        print('签名成功，获得注册码成功')
    elif r.status_code==506:
        print('签名失败')
    r=json.loads(r.text)
    print('注册码y ',''.join(str(ord(c)) for c in r['y']))
    #y=53717050295156175141299666853483104927481852761632004360349585816680051688453198848378519925084430636040329782206407962236517290354334764837330574271798281998113453403848503453838992242361788455599882418763829669566055675077988461656340153058798547448796652096530658269522063786538517299615407873998692939804
    y=int(''.join(str(ord(c)) for c in r['y']))
    glovar.setvalue('y',y)
    m=exgcdinv(y,k)
    glovar.setvalue('m', m)