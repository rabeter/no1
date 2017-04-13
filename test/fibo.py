
def fib(n):
    a =[]
    b,c = 0,1
    while c < n:
        a.append(c)
        b,c = c,b+c
    return a
