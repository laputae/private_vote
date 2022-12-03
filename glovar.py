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
pubkey=0
def setpubkey(var):
    global pubkey
    pubkey=var
#保存公钥
pai = paillier.Paillier()
pai.__key_gen__()
setpubkey(pai.pubKey)

for i in range(1, 6):
    key= 'choice' + str(i)
    sendchoice[key] = '0'

def setvalue(value, para):
    global glovalue
    glovalue[value]=para

def getvalue(value):
    global glovalue
    return glovalue[value]


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
        else:
            sendchoice[key]='0'

def getsendchoice():
    #返回同态加密后的投票选项
    global sendchoice
    tempchoice={}
    for key in sendchoice:
        tempchoice[key]=str(pai.encipher(sendchoice[key]))
    return tempchoice

#设置得到的总投票结果并解密
def setretchoice(var):
    global sendchoice
    sendchoice=var
    print(sendchoice)
    i=0
    for key in sendchoice:
        i=i+1
        if i<=5:
            print(sendchoice[key])
            sendchoice[key]=str(pai.decipher(sendchoice[key]))

#把总投票结果显示在弹窗里
def getretchoice():
    global sendchoice
    return sendchoice

if __name__ == "__main__":
    getsendchoice()