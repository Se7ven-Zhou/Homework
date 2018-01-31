#coding:utf-8

# 格式：open(文件地址，操作形式)

"""将文件以逗号隔开，保存到列表list中"""
# file_open = open('zj.txt','r+')
# file_content = str(file_open.read()).split(',')
# print file_content
# file_open.close()

"""文件每行都是一条请求数据，读取数据并保存到列表list中"""

file_dict = {}
file_open = open('url.txt','r')
file_content = str(file_open.read()).split(',')

print file_content

file_open.close()