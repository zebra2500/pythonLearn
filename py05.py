# # 1.异常
# # 1.1异常的处理
# try:
#     print(1/0)
# except ZeroDivisionError as e :
#     print("出现异常:",e)
# except Exception as b :
#     print(f"未知类型异常{b}")
# else:
#     print("无异常")
# finally:
#     print("无论有没有异常都会执行的代码块")

# # 1.2 自定义异常
# def login():
#     pwd = input("请输入密码：")
#     if len(pwd) >= 6 :
#         print("输入密码成功")
#     else:
#         raise Exception("密码长度不足")
#     return pwd
# try:
#     print(login())
# except Exception as e:
#     print(e)

# 2 模块
"""
一个py文件就是一个模块
使用pip工具可以自己下载很多模块 : pipl list  pip install packageName  pip uninstall packageName
"""
# import pytest
# # 2.1 导入模块
# import pytest
# pytest
# print(pytest.name)
# print(pytest.add(1,1))
#
# from pytest import *
# print(fun())
# print(add(1,2))
# pytest

# # 2.2 as 给模块起别名
# from pytest import add as add1
# print(add1(1,2))

# # 2.3内置全局变量 __name__ 用于py文件在不同场景(在内部执行or被导入)执行不同逻辑
# import pytest1
# pytest1.test()

# 2.4 包   有一个专门的Python Package选项,不是新建一个文件夹
# import packageTest #导包时会自动执行__init__.py中的代码,init的主要作用是导入当前包内的文件
from packageTest import * #必须在init文件中将所有模块定义在all变量中才可以调用当前包中所有模块
login.log()
testImport.initTest()















































































