print("歡迎來到終極密碼大挑戰，請來挑戰你的運氣吧!")

import random

pwd = random.randint(1, 100)

maxN = 100
minN = 1

while True:
    guess = int(input("請輸入"+str(minN)+"~"+str(maxN)+"間的數字:"))
    if guess > maxN or guess < minN:
        print("猜測數字超過範圍,",end=" ")
        continue
    if guess == pwd:
        print("您猜對了，密碼就是",pwd)
        break
    if guess > pwd:
        maxN = guess - 1
    elif guess < pwd:
        minN = guess + 1
        