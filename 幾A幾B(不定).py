import random

guessNum = int (input("請問你要猜測幾個數字的密碼:"))
pwd = random.sample(range(0,10),guessNum)

#print(pwd)

A = 0
B = 0

while A!=guessNum:
    num = input("請輸入"+str(guessNum)+"個數字:")
    while len(num) != guessNum or len(set(num))!=guessNum:
        num = input("請輸入"+str(guessNum)+"個數字，且數字勿重複:")
        
    list1 = list(map(int,list(num)))
    
    #print(list1)
    
    A = 0
    B = 0
    for i in list1:
        if i in pwd:
            if list1.index(i) == pwd.index(i):
                A += 1
            else:
                B += 1
    print(A,"A",B,"B",sep="")

print("你猜對了,密碼是",num)
