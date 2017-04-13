# python
---

##
Python 2有31个关键字：
and del from not while
as elif global or with
assert else if pass yield
break except import print
class exec in raise
continue finally is return
def for lambda try
In Python 3, exec is no longer a keyword, but nonlocal is.
在Python 3中，exec不再是一个关键字，但nonlocal是。


range(star,end,step) 生成一个链表(不可以直接打印)


除法7/2=3.5 7//2=3

循环带有else
for x in range(2,10):
    if 7/x ==0:
        print("NO")
else:
    print('YES')

函数可以作为对象或参数进行赋值

hw12 = '%s %s %d' % (hello, world, 12)
# sprintf style string formatting
print hw12
# prints "hello world 12"

i = 5
def f(arg=i):
print arg
i = 6
f()==5 //函数默认变量替换

数组链表内置函数
count(x) sort() reverse() index(x) pop(i) remove(x)
append(x) extend(L) insert(i,x)

filter(function(x), sequence)
map(function(x,...), sequence)
reduce(function(x,y), sequence)返回单值，由参数反复迭代产生
链表推导式
vec = [2, 4, 6]
[3 * x for x in vec if x > 3]

数组使用[]进行标示
元组使用()进行标示
字典使用{}进行标示
元组为常量不可改变(不能进行改变内容的自操作)
zip(x,y)合并x/y返回元组
字典有一个被称作items的方法，其返回一个元组的列表， 其中每个元组是一个键-值对。
不同对象之间比较是合法的，确定的
list<string<tuple
数值比较时会统一数据类型

print格式化输出
print('%2d,%3d,%4d'%(x,x**2,x**3))

try ... except 带有else语句
for arg in sys.argv[1:]:
    try:
        f = open(arg, ’r’)
    except IOError:
        print ’cannot open’, arg
    else:
        print(arg, ’has’, len(f.readlines()), ’lines’)
        f.close()

类class
属性、方法都为公开的、虚拟的
一般使用_init_等方式人为设计私有属性、方法

同名的对象属性会覆盖对象方法


迭代器

生成器


字符串
    slice/切片
    wa = "wang"[0:2]
    wang = "wang"[:]
    list()返回字符
    .split("-")切割字符串，默认空格切割
    "-".join()字符串合并
    .upper()大写
    .find()
s = "hello"
print s.capitalize()  # Capitalize a string; prints "Hello"
print s.upper()       # Convert a string to uppercase; prints "HELLO"
print s.rjust(7)      # Right-justify a string, padding with spaces; prints "  hello"
print s.center(7)     # Center a string, padding with spaces; prints " hello "
print s.replace('l', '(ell)')  # Replace all instances of one substring with another;
                               # prints "he(ell)(ell)o"
print '  world '.strip()  # Strip leading and trailing whitespace; prints "world"


random
    .choice([1,8,6])
    .random()
    .randint(begin,end)



文件I/O
text = open(file, mode='r', buffering=-1, encoding=None,
errors=None, newline=None, closefd=True, opener=None)
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'+'       open a disk file for updating (reading and writing)

text.write(text)
text.read()
text.close()

$$ \vec{F}=m \frac{d \vec{v}}{dt} + \vec{v}\frac{dm}{dt} $$





