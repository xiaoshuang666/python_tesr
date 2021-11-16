class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")
        #返回 分配的空间
        return super().__new__(cls)
    def __init__(self):
        print("播放器初始化")
    # def __del__(self):
    #     return

player =MusicPlayer()
print(player)