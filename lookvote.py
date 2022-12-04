import json

import requests

import glovar


def lookvote():
    vn=glovar.getvalue('vn')
    m=glovar.getvalue('m')
    params={'vn':vn,'m':m}
    address='https://mockapi.eolink.com/6QVS7t1d18916567af4d46ffb579dc4e035981316fe67b6/info'
    r=requests.post(address,json=params)
    if r.status_code==200:
        print('成功收到结果')
    elif r.status_code==510:
        print('签名验证失败')
    elif r.status_code==511:
        print('未投票，禁止查看')

    r=json.loads(r.text)
    glovar.setretchoice(r['result'])