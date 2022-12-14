import tkinter
import glovar
import login,getregkey,register,lookvote,sendchoice
from tkinter import messagebox

def regkeybutton():
    getregkey.getregkey()
    # 使用消息对话框控件，showinfo()表示提示
    messagebox.showinfo(title='注册码y：', message=glovar.getvalue('y'))
#查看投票结果
def look():
    lookvote.lookvote()
    messagebox.showinfo(title='查看投票结果',message=glovar.getretchoice())

window=tkinter.Tk()
window.title('隐私保护的投票器')
window.geometry('800x600')
labe1=tkinter.Label(window, text="用户名：")
labe1.grid(row=0,column=100)

name= tkinter.StringVar()
e1=tkinter.Entry(window,textvariable=name)
e1.grid(row=0, column=300, padx=10, pady=5)


button1=tkinter.Button(window,text='注册',width=10,height=2,command=lambda :register.register(name.get()))
button1.grid(row=1,column=300)
button1.pack

button2=tkinter.Button(window,text='获得注册码',width=10,height=2,command=regkeybutton)
button2.grid(row=2,column=300)
button2.pack

button3=tkinter.Button(window,text='登录',width=10,height=2,command=login.login)
button3.grid(row=3,column=300)
button3.pack

#弹出投票选项
def createbox():
    var1 = tkinter.StringVar()
    l = tkinter.Label(window, bg='#B0B0B0', font=('微软雅黑', 15), width=20, textvariable=var1)
    l.grid(row=5,column=300)
    def click_button():
        try:
            val = lb.get(lb.curselection())
            var1.set(val)
            glovar.choicesend(val)
        except Exception as e:
            e = '发现一个错误'
            messagebox.showwarning(e,'没有选择任何条目')
    b1 = tkinter.Button(window, text='获取当前选项', command=click_button)
    b1.grid(row=8,column=300)
    var2 = tkinter.StringVar()
    var2.set((glovar.getchoice(1),glovar.getchoice(2), glovar.getchoice(3),glovar.getchoice(4),glovar.getchoice(5)))
    lb = tkinter.Listbox(window, listvariable=var2)
    lb.grid(row=7,column=300)

butt4=tkinter.Button(window,text='显示选项',width=10,height=2,command=createbox)
butt4.grid(row=4,column=300)
butt4.pack

butt5=tkinter.Button(window,text='发送投票结果',width=10,height=2,command=sendchoice.sendchoice)
butt5.grid(row=9,column=300)
butt5.pack

butt6=tkinter.Button(window,text='查看总投票结果',width=12,height=2,command=look)
butt6.grid(row=10,column=300)
butt5.pack

window.mainloop()