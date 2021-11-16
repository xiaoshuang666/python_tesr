class Tool(object):
    count =0
    def __init__(self,name):
        self.name = name
        Tool.count += 1#类属性

#实例化输出类属性
tool1=Tool("斧头")
print(tool1.count)

tool2=Tool("斧子")
tool3=Tool("毛铁")
print(tool1.count)
#实例化输出类属性的缺点
tool1.count =99
print(tool1.count)
#标准输出
print(Tool.count)
