import requests
import glovar
import time
#发送投票结果
def sendchoice():
    choice=glovar.getsendchoice()
    timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    params={'vn':glovar.getvalue('vn'),'m':glovar.getvalue('m'),'choice1':choice['choice1'],'choice2':choice['choice2'],'choice3':choice['choice3'],
            'choice4':choice['choice4'],'choice5':choice['choice5'],'timestamp':timestamp}
    address='https://mockapi.eolink.com/6QVS7t1d18916567af4d46ffb579dc4e035981316fe67b6/vote'
    r=requests.post(address,json=params)
    if r.status_code==200:
        print('发送投票成功')
    elif r.status_code==508:
        print('重复投票')
    elif r.status_code==509:
        print('验证签名失败')

if __name__ == "__main__":
    sendchoice()