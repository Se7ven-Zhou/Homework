#coding=utf-8

# 创建一个类
# class clas1:
#     pass
# 实例化一个类
# a = clas1()

"""
构造函数（构造方法）
__init__(参数)
self：在类中的方法必须加上self参数
构造函数实际意义：初始化
"""
# class clas2:
#     def __init__(self):
#         print("I'm clas2 self")
# b = clas2()
# print b

"""给类加上参数，给构造方法加上参数"""
# class clas3:
#     def __init__(self,name,job):
#         print("my name is "+name+",my job is "+job)
#
# c = clas3("seven","tester")

"""属性：类里面的变量：self.属性名"""
# class clas4:
#     def __init__(self,name,job):
#         self.myname = name
#         self.myjob = job
# d = clas4("seven","tester")
#
# print d.myname, d.myjob

"""方法：类里面的函数：def 函数名（self,参数）"""
# class clas5:
#     def myfunc1(self,name):
#         print("hello,"+name)
#
# f = clas5()
# f.myfunc1("seven")

"""类里面初始化参数可以随便调用"""
class clas6:
    def __init__(self,name):
        self.myname = name
    def myfunc2(self):
        print("hello "+self.myname)

e = clas6("seven")
e.myfunc2()
