number = 34
guess = 0
print("数字猜谜游戏")

while guess != number:
    guess = int(input("请输入你猜的数字:"))

    if guess == number:
        print("猜对了")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")