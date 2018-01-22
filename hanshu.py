#coding=utf-8

"""map()函数 and lambda函数"""
# map(function/none(函数名就行) , iterable)
# filter(function/none(函数名就行) , iterable)
# lambda x:x+2

# code = list(raw_input("请输入密码："))
#
# changeCode = list(map(lambda i:(int(i)+5)%10,code))
# finalCode = ""
# for i in changeCode[::-1]:
#     finalCode += str(i)
# print ("加密后：" + str(finalCode))

def odd(x):
    return x % 2

aa = odd(10)
print aa
# print filter(add,range(10))