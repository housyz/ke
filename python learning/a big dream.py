class A:
    def __init__(self,gender,name,item,hp=100):
        self.hp = hp
        self.name = name
        self.gender = gender
        self.item = item

    def player_append(self,new_item):
        pass


class friend:
    def __init__(self, category, name, grade=1):
        self.name = name
        self.grade = grade
        self.category = category


def new_friend(category=0, name=0):
    print('现在，选择你的好伙伴吧，它将陪伴你闯荡这个世界！')
    choose = str(input('a 小火龙,b 小水龙'))
    if choose == 'a':
        friend_category = '小火龙'
    elif choose == 'b':
        friend_category = '小水龙'
    friend_name = str(input('它的名字'))
    FRIEND = friend(category=friend_category, name=friend_name)
    print('好的，', FRIEND.name, '从此就是你的最好的朋友了，赶紧培养它吧！')
    return FRIEND
#
#
# class animal:
#     def __init__(self, category, grade):
#         self.grade = grade
#         self.category = category


player_name = str(input('请输入您的名字：'))
player_gender = str(input('请输入您的性别：'))
item = {'新手指南': 1}
PLAYER = A(name=player_name, gender=player_gender, item=item)
print('你好'+PLAYER.name, '，欢迎来到新世界！')
print('在你的物品栏有一本新手指南，你可以阅读它来了解这个世界。')
FRIEND = new_friend()

