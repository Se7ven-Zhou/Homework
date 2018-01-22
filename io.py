# coding=utf-8


# 格式：open(文件地址，操作形式)
# """
# w:写入
# r:打开
# b：二进制
# a:追加写入（末尾加入内容）
# """

# content = open("D:/Python27/Case/Test/zj.txt","r")
#
# data = content.read()
#
# def test(*params):
#     print("参数的个数:",len(params))
#     print("第二个参数是" + params[1])
#
# # test(1,"曼联",3.14,4,5,6)
#
# def test1(name ="Bob",word ="hello"):
#     print(name + "->" + word)

def discount(price,rate):
    new_price = price * rate
    return new_price

old_price = input("请输入原价：")
count = input("请输入折扣：")
now_price = discount(old_price,count)

print(u"目前的价格是：",now_price)