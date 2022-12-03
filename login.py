import json
import requests
import glovar

#登陆界面
def login():
    vn=glovar.getvalue('vn')
    m=glovar.getvalue('m')
    #注意发送的投票选项要用paillier加密
    """
    if vn!=quick_algorithm(m,e,n):
        print('验证失败')
        sys.exit(0)
    else:
        params={'vn':str(vn),'m':str(m)}
        address='https://mockapi.eolink.com/6QVS7t1d18916567af4d46ffb579dc4e035981316fe67b6/mylogin'
        r=requests.post(address,json=params)

        r=json.loads(r.text)
        print(r)
    """
    params={'vn':str(vn),'m':str(m)}
    address='https://mockapi.eolink.com/6QVS7t1d18916567af4d46ffb579dc4e035981316fe67b6/mylogin'
    r=requests.post(address,json=params)
    if r.status_code==200:
        print('登录成功')
    elif r.status_code==507:
        print('验证签名失败')
    r=json.loads(r.text)
    print(r)
    i=0
    for key in r['result']:
        i=i+1
        glovar.setchoice(i,r['result'][key])


    for i in range(1,6):
        print(glovar.getchoice(i))
