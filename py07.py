# 1. 面向对象
# 直接定义的属性/方法名:都可以访问
# _xx :一般是为了避免与关键字冲突,不可以被外部导入,可以被子类继承
# __xx : 一般是python中有特殊含义的方法/属性,不推荐自定义
class Test:
    name = "tset" # 类属性 类似于java中的static修饰的属性
    __a = 10   # 私有属性,实例无法访问(本质上是将变量名改成了_类名__属性名,通过这个属性名也是可以访问的)
    def __init__(self,age):
        self.age = age # 实例属性
    def __del__(self): # 删除对象时默认调用
        print("Test对象已被销毁")

    def hello(self): # 实例方法必须有一个参数，代表当前对象，通常用self命名
        print(f"hello,{self.name},{self.age}")
test = Test(10)
test.hello()
test1 = Test(20)
print("代码结束") # 代码结束后,所有对象会被销毁,会执行Test的del函数


