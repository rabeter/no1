class first():
    def __init__(self,real=1,imag=0):
        self.real = real
        self.imag = imag
    def f(self):
        print((self.real,self.imag))

class second:
    "wangqingjian "
    i = 123
    def f(self):
        print(self.i)

a = second()
b = first()
c = first(1,1)
a.f()
b.f()
cf = c.f
cf()

first.f(b)
