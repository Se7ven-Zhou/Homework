#coding=utf-8

"""继承（单继承，多继承）"""

"""
父亲会说话，母亲会写字
大儿子继承父亲说话
女儿继承父亲和母亲，并且有其他的方法
小儿子继承了父亲，但是优化了父亲的说话能力
"""

class father():
    def speak(self):
        print("I can speak !")
"""单继承"""
class son(father):
    pass

class mother():
    def write(self):
        print("I can write !")

"""多继承"""
class daughter(father,mother):
    def listen(self):
        print ("I can listen !")

"""继承（重写方法）"""
class son2(father):
    def speak(self):
        print ("I can speak too !")
Son2 = son2()
Son2.speak()