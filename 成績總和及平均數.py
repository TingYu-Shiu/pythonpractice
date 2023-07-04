list1 = list()


for i in range(1,11):
    number = int(input("請輸入第"+str(i)+"個成績:"))
    list1.append(number)


max = max(list1)
min = min(list1)
sum = sum(list1)
avg = sum/10
   
print("最高分為:",max)
print("最低分為:",min)
print("總和成績為:",sum)
print("平均成績為:",avg)              