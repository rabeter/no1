
from fibo import fib
import first as cla

if __name__ == '__main__':
    print(fib(100))
    s = "阿姨洗铁路"
    f = open('wang.txt','r+',-1,'utf-8')
    f.writelines(str(fib(100)))
    print(f.readline())
    for line in f:
        print(line)
    f.close()
    cla.first.f()
    cla.second.f()
    cla.first.f()
    cla.first.f()
    cla.second.f()
