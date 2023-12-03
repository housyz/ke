import random
secret = random.randint(1,10)
print("欢迎来到紫薇的猜数游戏")
a = 0
guess = 0
while a < 4 and guess != secret:
    temp = input("请输入您猜的数：")
    guess = int(temp)
    if guess == secret:
        print("恭喜您猜对了！")
    else:
        if guess < secret:
            print("啊呀，小了小了！")
        else:
            print("啊呀，大了大了！")
        a += 1
if a == 4:
    print("很抱歉哦，您的笨蛋脑瓜不太够用<(￣︶￣)↗[GO!]")
print("客官，游戏已经结束了哦~~~")







