import random

secret = random.randint(1, 20)
win = False
i = 0
print('我已经想好了一个1到20之间的数字，猜猜是多少！(输入-1退出)')
while i < 6:
    guess = int(input())
    if guess == -1:
        print('退出游戏')
        break
    if guess < 1 or guess > 20:
        print('请输入1-20之间的数字')
        continue
    i = i + 1
    if guess > secret:
        print('猜大了')
    elif guess < secret:
        print('猜小了')
    else:
        print('猜对了！')
        win = True
        break
if not win and i == 6:
    print('6次机会用完，下次再玩吧~')
