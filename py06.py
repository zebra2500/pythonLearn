# # 1. 斐波那契数列
# def feb(n):
#     if n<=2:
#         return 1
#     else:return feb(n-1)+feb(n-2)
# for i in range(1,10):
#     print(feb(i))



# # 2.闭包
# # 1.函数嵌套定义
# # 2.内层函数使用外层函数的局部变量
# # 3.外层函数的返回值是内层函数
#
# def outer(m) :
#     def inner(n):
#         print(m+n)
#     return inner
# print(outer(1)) # 返回内层函数的地址
# # 两种调用方法
# outer(1)(2)
# inr = outer(1)
# inr(2)

# 3.装饰器(将被装饰函数作为外层函数参数的闭包)
def test(m):
    print(m)
    return m
def wrapper(fn): # 装饰器传入被装饰的函数名
    def inner(*args,**kwargs): # args接收一个元组，kwargs是关键字
        print("f")   # 添加的功能
        fn(*args,**kwargs)  # 内层函数调用被装饰函数
        print("a")   # 添加的功能
    return inner
test = wrapper(test)  # 返回一个被装饰的函数
test(1)
# 另一种写法
@wrapper
def test1(m):
    print(m)
    return m

test1("test1")

# 3.1多个装饰器，谁离函数近谁先装饰 
def wrapper1(fn): # 装饰器传入被装饰的函数名
    def inner(*args,**kwargs): # args接收一个元组，kwargs是关键字
        print("f1")   # 添加的功能
        fn(*args,**kwargs)  # 内层函数调用被装饰函数
        print("a1")   # 添加的功能
    return inner
@wrapper1
@wrapper
def test2(m):
    print(m)
    return m
test2("test2")  # 先用wrapper装饰，然后用wrapper1装饰










