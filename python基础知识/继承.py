class Animal(object):
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")
class Dog(Animal):


    def bark(self):
        print("吠")

class XiaoTianQuan(Dog):

    def fly(self):
        print("飞")
    def bark(self):
        print("喵喵叫")
        Dog.bark(self)#俩种方法调用父类方法
        super().bark()

xtq  = XiaoTianQuan()

xtq.eat()
xtq.drink()
xtq.run()
xtq.bark()
xtq.fly()