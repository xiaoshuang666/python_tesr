class Game(object):
    #类属性
    top_score=0
    #实例化方法
    def __init__(self,player_name):
        self.player_name=player_name
    #静态方法
    @staticmethod
    def show_help():
        print("帮助信息:拼尽全力干掉他们")
    #类方法
    @classmethod
    def show_top_score(cls):
        print("历史最高分 %d"% cls.top_score)

    def start_game(self):
        print("你的好友 %s 已上线了"% self.player_name)
#1.查看帮助信息
Game.show_help()
#查看最高分
Game.show_top_score()
#实例化对象
game=Game("xiaoming")
game.start_game()