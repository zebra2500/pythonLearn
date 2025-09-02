# # 1.类型转换
# # int float str chr
# # eval() 计算字符串中有效的python表达式
# # tuple(),list() 将可迭代对象转换成元组/列表
#
# print(eval("10+10")) # 20 实现算数计算
# str1 = '[[1,2],[3,4]]'
# li = eval(str1)
# print(li,type(li)) #[[1, 2], [3, 4]] <class 'list'> #实现类型转换
#
# dic = {'name':'wang','age':'18'}
# li1 = list(dic)
# print(li1,type(li1))  #['name', 'age'] <class 'list'> 默认取键
# str2 = "test"
# li1 = list(str2)
# print(li1,type(li1))

# # 2.深浅拷贝
# import copy
# li = [1,2,3]
# li1 = li
# li[0] = 2
# print(li1)
# print(id(li1) == id(li)) #True
# li2 = copy.copy(li)
# print(id(li2) == id(li)) # False
#
# # 3.可变对象与不可变对象
# # 可变对象:list set dict
# # 不可变对象: 基础数据类型,str,tuple













