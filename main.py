import tkinter
import glovar
import login,getregkey,register,getname
from tkinter import messagebox

def regkeybutton():
    getregkey.getregkey()
    # 使用消息对话框控件，showinfo()表示提示
    messagebox.showinfo(title='注册码y：', message=glovar.getvalue('y'))

def main():
    username=getname.user()
    vn,x=register.register(username)
    m=getregkey.getregkey(x)
    login.login(vn,m)

window=tkinter.Tk()
window.title('隐私保护的投票器')
window.geometry('800x600')
labe1=tkinter.Label(window, text="用户名：")
labe1.grid(row=0)
name= tkinter.StringVar()
e1=tkinter.Entry(window,textvariable=name)
e1.grid(row=0, column=1, padx=10, pady=5)


button1=tkinter.Button(window,text='注册',width=10,height=5,command=lambda :register.register(name.get()))
button1.grid(row=1,column=1)
button1.pack

button2=tkinter.Button(window,text='获得注册码',width=10,height=5,command=regkeybutton)
button2.grid(row=2,column=1)
button2.pack

button3=tkinter.Button(window,text='登录',width=10,height=5,command=login.login)
button3.grid(row=4,column=1)
button3.pack

site = [('美团外卖',1),
        ('饿了么外卖',2),
        ('美团闪购',3),
        ('艾奇外卖',4)]
v=tkinter.IntVar

window.mainloop()