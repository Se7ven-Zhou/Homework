#coding=utf-8
"""自动贩卖机"""
"""
1.输入要的商品（定义产品以及价格）
2.输入钱币（只接受1,5,10）
3.判断金额大小
4.找零
"""
def buy(select):
    goods = {"orange":3.5, "coconut":4.0, "water":2.0, "milk":4.5}
    Sum = 0.0
    balance = 0.0
    while(1):
        money = raw_input("请投入钱币(仅限1/5/10元)：")
        if int(money)==1 or int(money)==5 or int(money)==10:
            Sum += float(money)
            if float(Sum) >= goods[select]:
                balance = float(Sum)-goods[select]
                break
            else:
                print("金额不够，请继续投币！！！")
        else:
            print ("请投入1/5/10元！！！")
    return balance

select = raw_input("请选择购买的商品(orange/coconut/water/milk)：")
final = buy(select)
print("购买"+str(select)+"成功，找零："+ str(final))

"""成绩判断函数"""

# def result(score):
#     while(1):
#         if score.isdigit() and 0 < int(score) <= 100:
#             if int(score) < 60:
#                 return "不及格"
#             elif 60<=int(score)<80:
#                 return "良好"
#             else:
#                 return "优秀"
#         else:
#             print("输入有误,请重新输入！")
#         score = raw_input("请输入分数：")
#
#
# score = raw_input("请输入分数：")
# print result(score)

"""取前两位长度的内容"""

# content = list(raw_input("请输入："))
# c = ""
# for i in content[0:2]:
#     c += str(i)

"""冒泡排序"""

a = [2,33,12,24,1,77,22,4]

for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]

print a