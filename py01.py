# print("hello world")
#
# # 1. step：自定义输出参数之间的分隔符,默认为一个空格
# # end：以什么为结尾,默认为/n,可以拼接下一个print的内容
# print("1","2","3",sep=" | ")
# print("1","2","3",end=" ")
# print("1","2","3")

# # 2. 变量:可以被反复赋值,并且类型可以不一样
# # 标识符:
#     # 严格区分大小写(跟Java一样)
#     # Python3之后支持中文变量名,但是不推荐
#     # 规范:下划线分割,在面相对象中通常使用大驼峰
# a = 1
# print(a)
# a = "test"
# print(a)

# # 3. 数据类型
# # 检测类型type()
# print(True)
# print(True + False)  #算数运算会将布尔型变量变成数值类型
# print(type(2+3j)) # complex 复数类型(了解)
# # 4. 字符串:单引号或者双引号都可以,三引号可以表示多行内容,但是要跟多行注释区分开
# str = """ test
# """
# print(str)
# """
# 多行注释
# """

# 5. 占位符
"""
%c 格式化字符及其ASCII码
%s 格式化字符串
%d 格式化整数
%u 格式化无符号整型
%0 格式化无符号八进制数
%x 格式化无符号十六进割数
X 格式化无符号十六进制数（大写）》
%.6f 格式化浮点数字，可指定小数点后的精度,默认显示六位小数，四舍五入
第e 用科学计数法格式化浮点数
E 作用同%，用科学计数法格式化浮点数
%g %f和%e的简写
%G %F和%E的简写   
%p 用十六进制数格式化变里的地址
"""
# print("我的名字是:%s,我今年%4d岁" %("test",123))
# # 6. f{} 表达式
# name = "test"
# age = 23
# print(f"我叫{name},今年{age}岁了")

# # 7. 转义符
# print(r"\n") #取消转义


# # 8. 运算符
# print(7/2)  # 3.5
# print(7//2)  # 3
# print(7**2)  #49

# # 9. 输入函数
# name = input("请输入你的姓名：")
# print(name)



# # 10. if elif
# age = input("请输入年龄")
# if int(age) >= 18 or int(age) < 60:
#     print("成人票")
# else:
#     print("半价票")


# # 11. while条件: 循环体
# num = 1
# while num <= 10:
#     print(num)
#     num+=1

# # 12. for 临时变量 in 可迭代对象

# # 遍历列表
# for item in [1, 2, 3, 4]:
#     print(item)
#

# # 遍历字符串
# for char in "Hello":
#     print(char)

# # 遍历字典
# my_dict = {"a": 1, "b": 2, "c": 3}
# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")

# # 遍历一个数值序列 range(start,stop,step)
# for i in range(5):  # 默认从0开始，到4结束
#     print(i)
#
# # 从10开始，到15结束
# for i in range(10, 16):
#     print(i)
#
# # 指定步长
# for i in range(0, 10, 2):
#     print(i)  # 输出 0, 2, 4, 6, 8

# # 嵌套遍历列表
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for item in row:
#         print(item, end=" ")
#     print()  # 换行
# for i in range(5):
#     print(i)
# else:
#     print("循环正常结束")  # 如果没有遇到 break，else 会执行

# # 使用 break 跳出循环
# for i in range(5):
#     if i == 3:
#         break  # 当 i 为 3 时跳出循环
#     print(i)
#

# # 使用 continue 跳过当前循环
# for i in range(5):
#     if i == 3:
#         continue  # 跳过打印 3
#     print(i)

# # 13 字符串

# # encode decode
# a = '你好 '
# print(a,type(a)) # hello <class 'str'> 以字符为单位处理
# a1 = a.encode()
# print(a1,type(a1)) # b'hello' <class 'bytes'> 以字节为单位处理

# # + , * , [] , [开始:结束:步长] , in , not in , r/R
# a = 'hello'
# b = 'world'
# print(a + b)
# print(a*2)
# print(a[0])
# print(a[-1]) # 0
# print(a[1:3]) # el
# print(a[1:-1]) #ell
# print(a[1:]) #ello
# print(a[:3]) # hel
# print(a[0::2]) #hlo
# print(a[-1::-1]) #olleh
# print('h' in a)
# print('h' not in a)

# find index count replace(旧内容,新内容,替换个数) split
# startswith endswith isupper islower lower upper capitalize
a = 'hello'
print(a.find('b'))
print(a.index('h')) # find未找到返回-1 index未找到会报错
