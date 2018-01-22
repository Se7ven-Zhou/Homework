#coding=utf-8

"""作业1：判断商场折扣"""
# while(1):
#     money = input("请输入金额：")
#     money = float(money)
#     if 50<=money<100:
#         final = money * 0.9
#         print("折扣10%，最终价格："+str(final))
#         continue
#     elif money>=100:
#         final = money * 0.8
#         print("折扣20%，最终价格：" + str(final))
#         continue
#     else:
#         print("无折扣，最终价："+str(money))
#         continue

"""作业2：输入一个数，判断是否能同时被3和5整除"""
# while(1):
#     num = input("请输入：")
#     if(num%3==0):
#         if(num%5==0):
#             print("Yes")
#             continue
#         else:
#             print("No")
#             continue
#     else:
#         print("No")
#         continue

"""作业3：筛选女足"""

# list = []
# for i in range(3):
#     name = raw_input("请输入姓名：")
#     sex = raw_input("请输入请别：")
#     age = input("请输入年龄：")
#
#     if (sex == "f" ):
#         if(10<=age<=12):
#             print ("符合要求")
#             list.append(name)
#             continue
#     else:
#         print ("不符合要求")
#         continue
# print list

"""作业4：加密"""

# code = list(raw_input("请输入密码："))
#
# change = []
# finalCode =""
#
# for i in code:
#     j = (int(i)+5)%10
#     change.append(j)
#
# for i in change:
#     finalCode += str(i)
#
# print int(finalCode)
"""加密函数"""
# def encrypt(code):
#     codeList = []
#     finalCodeList = []
#     finalCode =""
#     for i in code:
#         codeList.append(i)
#
#     for i in codeList:
#         j = (int(i)+5)%10
#         finalCodeList.append(j)
#
#     for i in finalCodeList[::-1]:
#         finalCode += str(i)
#
#     return finalCode
#
# while(1):
#     num = raw_input("请输入密码：").strip()
#     if num.isdigit():
#         str(num)
#         aa = encrypt(num)
#         break
#     else:
#         print("请输入整数！")
# print ("加密后："+ str(aa))
"""map()函数 and lambda函数"""
code = list(raw_input("请输入密码："))

changeCode = list(map(lambda i:(int(i)+5)%10,code))
finalCode = ""
for i in changeCode[::-1]:
    finalCode += str(i)
print ("加密后：" + str(finalCode))