#动物类
class Animal(object):
    #实例化方法
    def __init__(self,name):
        self.name=name
    #自定义方法
    def saymyself(self):
        print("In_Animal_class:I am a {}".format(self.name))
#猫类
class Cat(Animal):
    #父类自定义方法的复写
    def saymyself(self):
        print("In_Cat_class: I am a {}".format(self.name))
#狗类
class Dog(Animal):
    # 父类自定义方法的复写
    def saymyself(self):
        print("In_Dot_class:I am a {}".format(self.name))
#函数方法
def testfun(obj):
    print("{} say".format(obj.name))
    obj.saymyself()
#实例化
if __name__ == "__main__":
    animanl1 = Animal("animal")
    cat1 = Cat("cat")
    dog1 =Dog("dog")
    lst =[animanl1,cat1,dog1]
    for i in lst:#遍历实例化对象
        print(i.name)
        testfun(i)

    print("变量的多态")
    print(isinstance(animanl1,Animal))
    # isinstance用来判断对象是否继承某个类
    print(isinstance(cat1,Animal))
    print(isinstance(cat1,Cat))

    print(isinstance(dog1, Animal))
    print(isinstance(dog1,Dog))
    print(isinstance(dog1,Cat))

