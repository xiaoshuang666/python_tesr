class Dog(object):
    def __init__(self,name):
        self.name= name
    def game(self):
        print("%s在地上玩"%self.name)

class XianTianDog(Dog):
    def game(self):
        print("%s在天上遨游"% self.name)

class Person(object):
    def __init__(self,name):
        self.name=name
    def paly_with_dog(self,dog):
        print("%s 和 %s 一起玩"%(self.name,dog.name))
        dog.game()

xiaotianquan =XianTianDog("哮天犬")
xiaoming =Person("小明")
xiaoming.paly_with_dog(xiaotianquan)