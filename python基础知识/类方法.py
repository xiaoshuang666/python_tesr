class Tool(object):
    count =0
    #类方法
    # @classmethod
    # def show_tool_count(cls):
    #     print("工具数目 %d" %cls.count)
    def __init__(self,name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print("工具数目 %d" % cls.count)

tool1=Tool("斧头")
tool2=Tool("斧子")

#类.类方法
Tool.show_tool_count()