def mypow(x, n):
    x_init = x
    bin = []
    while n>0:
        r = n%2
        bin.insert(0, r)
        n = n//2

    for idx in range(1, len(bin)):
        x = x*x
        if bin[idx]==1:
            x = x*x_init
    return x