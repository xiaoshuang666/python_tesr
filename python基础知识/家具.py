#小猫爱吃鱼

# class Cat(object):
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#
# cat=Cat("Tom")
# print(cat.name)



#小明爱跑步
# class Person(object):
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#     def __str__(self):
#         return "我的名字叫%s,体重是%.2f公斤"%(self.name,self.weight)
#
#     def run(self):
#         print("%s爱跑步"%self.name)
#         self.weight-=0.5
#
#     def eat(self):
#         print("%s爱吃东西"%self.name)
#         self.weight+=1
#
# xiaoming=Person("小明",75.0)
# #注意体重变化
# xiaoming.eat()
# xiaoming.run()
# print(xiaoming)
#家具类开发
class HouseItem():
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return "[%s]占地%.2f"%(self.name,self.area)
class House():
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        #剩余面积
        self.free_area=area
        #家具列表
        self.item_list=[]
    def __str__(self):
        return ("户型：%s\n总面积；%.2f[剩余面积：%.2f]\n家具:%s"
                %(self.house_type,self.area,
                  self.free_area,self.item_list))

    def add_item(self,item):#添加家具
       print("要添加的家具 %s" % item)
        #1.判断家具面积
       if item.area > self.free_area:
           print("%s 面积太大，放不下"% item.name)
           return
       else:
        self.item_list.append(item.name)
        self.free_area -= item.area

#1,创建家具
bed=HouseItem("席梦思",400)
chest=HouseItem("衣柜",2)
table=HouseItem("餐桌",1.5)
print(bed)
print(chest)
print(table)
#2.创建房子
my_house=House("俩室一厅",60)

my_house.add_item(bed)
# my_house.add_item(chest)
# my_house.add_item(table)

print(my_house)