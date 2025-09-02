# # 1.函数
# def add(a,b):
#     return a + b
# print(add(1,2))
#
# # 1.1默认参数
# def add1(b,a = 1):
#     return a + b
# print(add1(1))
#
# # 1.2 可变参数(以元组的形式接收参数)
# def add3(*args):
#     return args
# print(type(add3(1,2,3))) #<class 'tuple'>
#
# # 1.3 关键字参数(以字典的形式接收参数)
# def fun(**kwargs):
#     print(kwargs)
#     return kwargs
# print(type(fun(name='wd',age=18))) #<class 'dict'>

# # 1.4 变量作用域
# # global : 将局部变量变为全局变量
# # nonlocal : 修饰内层函数的变量,被修饰的变量同时作用于内部函数和外部函数
# def fun1():
#     global a
#     a = 2
#     return 1
# fun1()
# print(a)
#
# b = 5
# def outer():
#     b = 10
#     def inner():
#         nonlocal b
#         b = 20
#         print("inner中的b:",b)
#     inner()
#     print("outer中的b:",b)
# outer()
# print(b)

# # 1.5 匿名函数 函数名 = lambda 形参 : 返回值(返回值是一个表达式)
# add = lambda x, y: x + y
# print(add(1, 2))
#
# func = lambda name,age=18 : (name,age) # 函数返回值是一个元组,所以要加括号
# print(func('wd'))
#
# comp = lambda a,b : 'a>b' if a>b else 'a<=b'
# print(comp(10,20))

# # # 1.6 内置函数(大写字母开头是内置常量名,小写字母开头是函数名)
# # import builtins
# # print(dir(builtins))
# # # map(func,sequence),将可迭代对象依次执行func,返回出一个对象
# li = [1,2,3]
# obj = map(lambda x: x*2, li)
# print(list(obj))
#
# # # reduce(func,sequence) , 要求func必须是有两个参数的函数,将对象中两个值取出计算出结果作为第一个参数,然后再取一个值作为第二个参数,依次计算
# from functools import reduce
# print(reduce(lambda x,y: x+y, li))

# # 1.6拆包 对于函数的多个返回数据,去除元组,列表或者字典直接获取里边的数据
# li = [1,2,3]
# a,*b = li #可以把a,*b理解成函数形参
# print(a)
# print(b)
# dict1 = {'name':'wd','age':'18'}
# a,b = dict1
# print(a)
# print(b)


























