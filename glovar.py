
glovalue = {}
glovalue['vn'] = 0
glovalue['e'] = 0
glovalue['n'] = 0
glovalue['k'] = 0
glovalue['username']= ''
glovalue['m']=0
glovalue['x']=''
glovalue['y']=0
choice={}
sendchoice={}
sendchoice['choice1']=0
sendchoice['choice2']=0
sendchoice['choice3']=0
sendchoice['choice4']=0
sendchoice['choice5']=0

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

def choicesend(var):
    global sendchoice
    sendchoice['var']=1