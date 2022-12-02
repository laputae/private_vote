import paillier
glovalue = {}
glovalue['vn'] = 0
glovalue['e'] = 0
glovalue['n'] = 0
glovalue['k'] = 0
glovalue['username']= ''
glovalue['m']=0
glovalue['x']=''
glovalue['y']=0
choice={}       #初始的选项
sendchoice={}   #选择之后的选项
for i in range(1, 6):
    key= 'choice' + str(i)
    print(key)
    sendchoice[key] = '0'

def setvalue(value, para):
    global glovalue
    glovalue[value]=para

def getvalue(value):
    global glovalue
    return glovalue[value]

def is_success(statuscode):
    if statuscode==200:
        print('注册成功')
    elif statuscode==505:
        print('重复注册')

def setchoice(cho,value):
    global choice
    choice[cho]=value

def getchoice(cho):
    global choice
    return choice[cho]

#把选中的投票置为’1‘
def choicesend(var):
    global sendchoice
    for key in sendchoice:
        if sendchoice[key]==var:
            sendchoice[key]='1'

def getsendchoice():
    #返回同态加密后的投票选项
    global sendchoice
    pai = paillier.Paillier()
    pai.__key_gen__()

    for key in sendchoice:
        sendchoice[key]=pai.encipher(sendchoice[key])
    return sendchoice

if __name__ == "__main__":
    getsendchoice()