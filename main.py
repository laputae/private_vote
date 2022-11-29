import tkinter
import login,getregkey,register,getname

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

button=tkinter.Button(window,text='注册',width=10,height=5,command=register(name.get())).grid(row=3, column=0, sticky="w", padx=10, pady=5)
window.mainloop()