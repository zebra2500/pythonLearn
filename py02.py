# 1. 列表(字符串本质上也是一个列表，所以字符串的操作跟列表很类似)
# #1.1 基本操作
# array = [1,2,'a',3,4]
# print(array[0:3]) #[1, 2, 'a'] 列表可以进行切片操作
# for i in array:
#     print(i)

# #1.2 append extend insert
# array = [1,2,'a',3,4]
# array.append([1,2,3])
# print(array) #[1, 2, 'a', 3, 4, [1, 2, 3]] append会整体添加
# array.extend([1,2,3])
# array.extend("test")
# print(array)  #[1, 2, 'a', 3, 4, [1, 2, 3], 1, 2, 3, 't', 'e', 's', 't'] extend会逐个添加
# # array.extend(1) #TypeError: 'int' object is not iterable extend只能添加可迭代对象
# array.insert(0,'test')
# print(array) #['test', 1, 2, 'a', 3, 4, [1, 2, 3], 1, 2, 3, 't', 'e', 's', 't']

# #1.3 修改 , in , not in 跟字符串操作一样
# name_list = ["bob","jack","rose","tom"]
#
# while True:
#     name = input('请输入昵称:')
#     if name not in name_list:
#         name_list.append(name)
#         break
#     print(f"昵称{name}已存在")
#
# print(f"注册成功,您的昵称为:{name}")

# #1.4del pop remove
# array = [1,2,3,4]
# # del array
# # print(array) # NameError: name 'array' is not defined. Did you forget to import 'array'?
# print(array.pop()) #4
# print(array) #[1, 2, 3]
# array.remove(1)
# print(array) #[2, 3]

# #1.5 sort reverse
# array = [3,2,5,1,4]
# array.sort()
# print(array)
# array.sort(reverse=True)
# print(array)

# #1.6 列表推导式
# # [表达式 for 变量 in 可迭代对象]
# array = [1,2,3,5]
# [print(i) for i in array]
# [array.append(i) for i in range(5)]
# print(array) #[1, 2, 3, 5, 0, 1, 2, 3, 4]
# [array.append(i) for i in range(5) if i%2==0]
# print(array) #[1, 2, 3, 5, 0, 1, 2, 3, 4, 0, 2, 4]


# # 2.元组
#
# #2.1 定义，当只有一个元素时，最后要加一个逗号，否则元组数据类型会变
# # 注:元组不支持增删改
# t = ()
# print(type(t))
# t = (1)
# print(type(t))
# t = (1,)
# print(type(t))
#
# # 2.2 应用场景
# # 函数参数与返回值
# # 格式化输出后边的括号本质是一个元组
# # 保护数据不被修改
# name = 'bob'
# age = 18
# print("%s的年龄是：%d" %(name,age))



# 3.字典

# # 3.1 定义
# dic = {'name':'bob','age':18}
# for k,v in dic.items():
#     print(k,v)
# dic.__setitem__('name','tom')
# print(dic) # 键是唯一的,添加相同的键会讲原来的值覆盖

# # 3.2 增删改查
# dic = {'name':'bob','age':18}
# print(dic['name'])
# print(dic.get('name'))
# print(dic.get('test','cn')) # 获取，如果获取不到返回自己设置
#
# dic.__setitem__('name','tom')
# print(dic)
#
# dic['age'] = 80
# print(dic)
#
# dic['addr'] = 'cn' # 通过[]获取值,如果不存在会自动新增
# print(dic)
#
# del dic['age']
# print(dic)
#
# dic.clear()
# print(dic)  # 清空,但不删除变量

# # 3.3 len(),keys(),values(),items()
# dic = {'name':'bob','age':18}
# print(len(dic))
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# for k in dic.keys():
#     print(k,dic.get(k))

# # 4. 集合
#
# # 4.1 基本特性：无序，去重
# s = {1,2,1,3}
# print(s) # {1, 2, 3}
# del s
#
# s= {} # 定义空字典
# print(type(s))
# del s
#
# s = set() # 定义空集合
# print(type(s))

# # 4.2 无序性
# s = {'a','b','c','d'}
# print(s) # 字母每次打印结果不一样
# s = {1,2,3,4}
# print(s)  # 数字每次打印结果都一样

# # 4.3 操作
# # add() 整体添加
# # update() 将传入的元素拆分逐个添加
# # remove() 删除一个元素,没有会报错 discard没有不会报错 pop()
# s = {1,2,3,4}
# s.add('test')
# print(s)
# s.update('test')
# print(s)
# s.remove('test')
# print(s)
# s.discard('t')
# print(s)

# # 5.交集与并集
# s1 = {1,2,3,4}
# s2 = {2,3,4,5}
# print(s1 & s2)
# print(s1 | s2)


































