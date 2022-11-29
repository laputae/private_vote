def ext_gcd(a,b,x,y): #扩展欧几里得算法
    if b == 0:          
        x=1
        y=0
        return a
    d=ext_gcd(b,a%b,x,y)
    t=x
    x=y
    y=t-a/b*x
    return d

def exgcdinv(a,b):
    x=0
    y=0
    ext_gcd(a,b,x,y)
    return x