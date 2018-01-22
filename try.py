#coding=utf=8

"""异常处理的格式"""
"""
try:
    程序
except Exception as 异常名称：
    异常处理部分
"""

# try:
#     for i in range(10):
#         print i
#         if(i==4):
#             print j
# except Exception as err:
#     print(err)

"""让异常后程序继续"""

for i in range(10):
    try:
        print i
        if(i==4):
            print j
    except Exception as err:
        pass
print("over")