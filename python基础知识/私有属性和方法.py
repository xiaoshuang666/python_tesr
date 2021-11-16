class Women(object):
    def __init__(self,name):
        self.name=name
        self.__age=18#私有属性

    def __secret(self):
        #对象的方法内部，可以访问私有属性
        print("%s 年龄是 %d"% (self.name,self.__age))

xiaofang =Women("小芳")#伪私有属性和方法
print(xiaofang._Women__age)
print(xiaofang._Women__secret())